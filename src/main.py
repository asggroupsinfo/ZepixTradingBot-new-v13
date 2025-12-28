#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import sys
import io
import asyncio
import uvicorn
import logging
import re
from logging.handlers import RotatingFileHandler
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime, date, timedelta, timezone
from typing import Dict, Any
from contextlib import suppress, asynccontextmanager
from dotenv import load_dotenv
import traceback

# Instrument sys.exit and global exception logging early
def _install_instrumentation():
    try:
        orig_exit = sys.exit
        def logged_exit(code=0):
            print(f"[EXIT-CALL] sys.exit({code}) invoked")
            print("[EXIT-CALL] Stack trace:")
            traceback.print_stack()
            orig_exit(code)
        sys.exit = logged_exit
        try:
            import builtins
            builtins.exit = logged_exit
        except Exception:
            pass
        def global_excepthook(exc_type, exc, tb):
            print(f"[UNCAUGHT-EXCEPTION] {exc_type.__name__}: {exc}")
            traceback.print_tb(tb)
        sys.excepthook = global_excepthook
        def threading_excepthook(args):
            print(f"[THREAD-EXCEPTION] {args.exc_type.__name__}: {args.exc_value}")
            traceback.print_tb(args.exc_traceback)
        try:
            import threading
            threading.excepthook = threading_excepthook
        except Exception:
            pass
    except Exception as e:
        print(f"[INSTRUMENTATION-ERROR] {e}")

_install_instrumentation()

# Fix Unicode encoding for Windows console
if sys.platform == 'win32':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass  # If already wrapped, ignore
    
    # Set Windows ProactorEventLoop for proper async handling on Windows
    if sys.platform.startswith('win'):
        try:
            asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
            print("[EVENT-LOOP] Set WindowsProactorEventLoopPolicy on Windows")
        except Exception as e:
            print(f"[EVENT-LOOP] Could not set ProactorEventLoop policy: {e}")


# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Load .env file before anything else (highest priority for credentials)
load_dotenv()

# Configure logging with rotation and spam protection
def setup_logging():
    """Setup logging with rotation and level filtering"""
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)
    
    # Setup root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)  # Root logger accepts all, handlers filter
    
    # Remove existing handlers
    root_logger.handlers.clear()
    
    # Load saved log level from config/logging_settings.json
    saved_log_level = logging.INFO
    try:
        if os.path.exists('config/logging_settings.json'):
            import json
            with open('config/logging_settings.json', 'r') as f:
                settings = json.load(f)
                saved_level = settings.get('log_level', 'INFO')
                if saved_level in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
                    print(f"[LOGGING CONFIG] Loaded saved log level: {saved_level}")
                    saved_log_level = getattr(logging, saved_level)
    except Exception as e:
        print(f"[LOGGING CONFIG] Could not load saved log level: {e}")
    
    # Load trading debug mode
    try:
        if os.path.exists('config/trading_debug.txt'):
            with open('config/trading_debug.txt', 'r') as f:
                debug_mode = f.read().strip().lower() == 'true'
                print(f"[LOGGING CONFIG] Loaded trading_debug: {debug_mode}")
    except Exception as e:
        print(f"[LOGGING CONFIG] Could not load trading_debug: {e}")
    
    # Create rotating file handler (max 2MB, keep 50 backup files)
    file_handler = RotatingFileHandler(
        'logs/bot.log',
        maxBytes=2*1024*1024,   # 2MB per file
        backupCount=50,         # Keep 50 backup files (no deletion for long time)
        encoding='utf-8'
    )
    file_handler.setLevel(saved_log_level)  # Use saved log level
    
    # Create console handler (use saved log level)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(saved_log_level)  # Use saved log level
    
    # Create formatter with colors for terminal
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    # Suppress noisy loggers
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("urllib3.connectionpool").setLevel(logging.WARNING)  # Suppress HTTP connection spam
    
    return root_logger

# Setup logging before importing other modules
setup_logging()

# Display active logging level at startup (from handlers, not root logger)
logger = logging.getLogger(__name__)
root_logger = logging.getLogger()

# Get actual effective level from handlers (not root logger which is always DEBUG)
if root_logger.handlers:
    # Use first handler's level as the effective level
    effective_level = root_logger.handlers[0].level
    level_name = logging.getLevelName(effective_level)
else:
    # Fallback to root logger level if no handlers
    level_name = logging.getLevelName(root_logger.level)

print(f"═══════════════════════════════════════")
print(f"🚀 BOT STARTING - LOGGING LEVEL: {level_name}")
print(f"═══════════════════════════════════════")
logger.info(f"Bot starting with logging level: {level_name}")

from src.config import Config
from src.core.trading_engine import TradingEngine
from src.managers.risk_manager import RiskManager
from src.clients.mt5_client import MT5Client
from src.clients.telegram_bot import TelegramBot
from src.processors.alert_processor import AlertProcessor
from src.services.analytics_engine import AnalyticsEngine 
from src.models import Alert

# Initialize components
config = Config()
risk_manager = RiskManager(config)
mt5_client = MT5Client(config)
telegram_bot = TelegramBot(config)
alert_processor = AlertProcessor(config)

# Initialize trading engine with all components
trading_engine = TradingEngine(config, risk_manager, mt5_client, telegram_bot, alert_processor)

# Set dependencies IMMEDIATELY - before any initialization
telegram_bot.set_dependencies(risk_manager, trading_engine)
# Also set directly to ensure they're always available
telegram_bot.risk_manager = risk_manager
telegram_bot.trading_engine = trading_engine
# Store global references for dependency retrieval
telegram_bot._global_trading_engine = trading_engine
telegram_bot._global_risk_manager = risk_manager
print("[OK] Dependencies set immediately in TelegramBot")

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Modern lifespan context manager for FastAPI startup/shutdown"""
    # Startup
    print("="*70)
    print("STARTING ZEPIX TRADING BOT v2.0")
    print("="*70)
    print("Initializing components...")
    telegram_bot.set_dependencies(risk_manager, trading_engine)

    init_ok = False
    try:
        init_ok = await trading_engine.initialize()
    except SystemExit as se:
        print(f"[STARTUP-SYSTEMEXIT] code={se.code}")
        raise
    except Exception as e:
        print(f"[STARTUP-EXCEPTION] {e}")
        traceback.print_exc()
        init_ok = False
    if not init_ok:
        if not config.get('simulate_orders', False):
            print("[WARN] Live init failed - enabling simulation mode")
            config.update('simulate_orders', True)
            try:
                if not await trading_engine.initialize():
                    telegram_bot.send_message("❌ Bot failed to initialize")
                    raise RuntimeError("Trading engine could not initialize")
            except Exception as e:
                print(f"[SIMULATION-INIT-ERROR] {e}")
                traceback.print_exc()
                telegram_bot.send_message("❌ Bot failed to initialize")
                raise RuntimeError("Trading engine could not initialize (simulation attempt)")
        else:
            telegram_bot.send_message("❌ Bot failed to initialize")
            raise RuntimeError("Trading engine could not initialize")

    # IMPORTANT: Inject dependencies into alert_processor
    # This must be done AFTER trading_engine is created and initialized
    alert_processor.trend_manager = trading_engine.trend_manager
    alert_processor.telegram_bot = telegram_bot
    print("[OK] Injected trend_manager and telegram_bot into alert_processor")

    mode = "SIMULATION" if config.get('simulate_orders', False) else "LIVE TRADING"
    
    # REPLY KEYBOARD - Bottom (auto-hides after click)
    reply_menu = {
        "keyboard": [
            [{"text": "📊 Dashboard"}, {"text": "⏸️ Pause/Resume"}],
            [{"text": "📈 Active Trades"}, {"text": "💰 Performance"}],
            [{"text": "💱 Trading"}, {"text": "⏱️ Timeframe"}],
            [{"text": "🔄 Re-entry"}, {"text": "📍 Trends"}],
            [{"text": "🛡️ Risk"}, {"text": "⚙️ SL System"}],
            [{"text": "📦 Orders"}, {"text": "📈 Profit"}],
            [{"text": "⚙️ Settings"}, {"text": "🔬 Diagnostics"}],
            [{"text": "⚡ Fine-Tune"}, {"text": "🆘 Help"}],
            [{"text": "🔄 Refresh"}, {"text": "🚨 PANIC CLOSE"}]
        ],
        "resize_keyboard": True,
        "one_time_keyboard": True  # Auto-hide after click
    }

    startup_msg = (
        f"🤖 *Bot Ready!*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"Mode: *{mode}*\n"
        f"✅ **Click button → Menu auto-hides**\n"
        f"📱 Click 'Show Menu' to reopen"
    )
    telegram_bot.send_message(startup_msg, reply_markup=reply_menu)

    app.state.background_tasks = []
    try:
        trade_task = asyncio.create_task(trading_engine.manage_open_trades())
        app.state.background_tasks.append(trade_task)
        print("[OK] Trade monitor started")
    except Exception as e:
        print(f"[ERROR] Could not start trade monitor: {e}")
        raise

    import threading
    polling_started = threading.Event()
    
    def _poll_wrapper():
        try:
            print("[POLLING-THREAD] Polling thread started")
            polling_started.set()
            telegram_bot.start_polling()
        except SystemExit as se:
            print(f"[POLLING-SYSTEMEXIT] code={se.code}")
            raise
        except Exception as e:
            print(f"[POLLING-EXCEPTION] {e}")
            traceback.print_exc()
        finally:
            print("[POLLING-THREAD] Polling thread exited")
    
    polling_thread = threading.Thread(target=_poll_wrapper, daemon=True)
    polling_thread.start()
    app.state.polling_thread = polling_thread
    
    # Wait for polling to actually start
    if not polling_started.wait(timeout=5):
        print("[WARN] Polling thread did not start within 5 seconds")
    
    print("[OK] Telegram polling thread started")
    
    # Application is running
    print("[LIFESPAN] Yielding control - bot is now running")
    print("="*70)
    print("✅✅✅ BOT IS LIVE NOW - READY FOR TELEGRAM COMMANDS ✅✅✅")
    print("="*70)
    sys.stdout.flush()
    
    # Create a shutdown event to keep lifespan alive until CTRL+C
    shutdown_event = asyncio.Event()
    app.state.shutdown_event = shutdown_event
    
    # Yield to allow the application to run
    yield
    
    # This code runs on shutdown - signal the event first
    print("[LIFESPAN] Shutdown signal received - cleaning up...")
    shutdown_event.set()  # Signal any waiting tasks
    sys.stdout.flush()
    
    # Shutdown
    print("[SHUTDOWN] Stopping Telegram polling...")
    telegram_bot.stop_polling()
    print("[SHUTDOWN] Cancelling background tasks...")
    for task in getattr(app.state, 'background_tasks', []):
        print(f"[SHUTDOWN] Cancelling task: {task}")
        if not task.done():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                print(f"[SHUTDOWN] Task cancelled: {task}")
    print("[SHUTDOWN] Background tasks cancelled. Shutdown complete.")

app = FastAPI(title="Zepix Automated Trading Bot v2.0", lifespan=lifespan)

@app.middleware("http")
async def filter_scanner_requests(request: Request, call_next):
    """Filter out security scanner requests to reduce log noise"""
    path = request.url.path
    scanner_patterns = [
        r'/vendor/phpunit', r'/\.env', r'/\.git', r'/admin', r'/cgi-bin',
        r'/phpunit', r'/eval-stdin', r'/.git/config'
    ]
    
    if any(re.search(pattern, path) for pattern in scanner_patterns):
        # Return 404 without logging to reduce noise
        return JSONResponse(status_code=404, content={"detail": "Not found"})
    
    response = await call_next(request)
    return response

@app.post("/webhook")
async def handle_webhook(request: Request):
    """Handle incoming webhook alerts from TradingView/Zepix"""
    try:
        data = await request.json()
        
        print(f"Webhook received: {json.dumps(data, indent=2)}")
        
        # Validate alert
        if not alert_processor.validate_alert(data):
            return JSONResponse(content={"status": "rejected", "message": "Alert validation failed"})
        
        # Process alert
        result = await trading_engine.process_alert(data)
        
        if result:
            return JSONResponse(content={"status": "success", "message": "Alert processed"})
        else:
            return JSONResponse(content={"status": "rejected", "message": "Alert processing failed"})
            
    except Exception as e:
        error_msg = f"Webhook processing error: {str(e)}"
        telegram_bot.send_message(f"ERROR: {error_msg}")
        raise HTTPException(status_code=400, detail=error_msg)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": "2.0",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "daily_loss": risk_manager.daily_loss,
        "lifetime_loss": risk_manager.lifetime_loss,
        "mt5_connected": mt5_client.initialized,
        "features": {
            "fixed_lots": True,
            "reentry_system": True,
            "sl_hunting_protection": True,
            "1_1_rr": True
        }
    }

@app.get("/stats")
async def get_stats():
    """Get current statistics"""
    stats = risk_manager.get_stats()
    return {
        "daily_profit": stats["daily_profit"],
        "daily_loss": stats["daily_loss"],
        "lifetime_loss": stats["lifetime_loss"],
        "total_trades": stats["total_trades"],
        "winning_trades": stats["winning_trades"],
        "win_rate": stats["win_rate"],
        "current_risk_tier": stats["current_risk_tier"],
        "risk_parameters": stats["risk_parameters"],
        "trading_paused": trading_engine.is_paused,
        "simulation_mode": config["simulate_orders"],
        "lot_size": stats["current_lot_size"],
        "balance": stats["account_balance"]
    }

@app.post("/pause")
async def pause_trading():
    """Pause trading"""
    trading_engine.is_paused = True
    return {"status": "success", "message": "Trading paused"}

@app.post("/resume")
async def resume_trading():
    """Resume trading"""
    trading_engine.is_paused = False
    return {"status": "success", "message": "Trading resumed"}

@app.get("/trends")
async def get_trends():
    """Get all trends (15m, 1h, 1d only - 5m not used by bot)"""
    # FIX #1: Force reload trends from file for real-time data
    trading_engine.trend_manager.load_trends()
    
    trends = {}
    symbols = ["XAUUSD", "EURUSD", "GBPUSD", "USDJPY", "USDCAD", 
               "AUDUSD", "NZDUSD", "EURJPY", "GBPJPY", "AUDJPY"]
    
    # FIX #1: Only fetch 15m, 1h, 1d (5m not needed - avoid waste computation)
    for symbol in symbols:
        trends[symbol] = {
            "15m": trading_engine.trend_manager.get_trend(symbol, "15m") or "NEUTRAL",
            "1h": trading_engine.trend_manager.get_trend(symbol, "1h") or "NEUTRAL",
            "1d": trading_engine.trend_manager.get_trend(symbol, "1d") or "NEUTRAL"
        }
    
    return {"status": "success", "trends": trends}

@app.post("/set_trend")
async def set_trend_api(symbol: str, timeframe: str, trend: str, mode: str = "MANUAL"):
    """Set trend via API"""
    try:
        trading_engine.trend_manager.update_trend(symbol, timeframe, trend.lower(), mode)
        return {"status": "success", "message": f"Trend set for {symbol} {timeframe}: {trend}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/chains")
async def get_reentry_chains():
    """Get active re-entry chains"""
    chains = []
    for chain_id, chain in trading_engine.reentry_manager.active_chains.items():
        chains.append(chain.dict())
    return {"status": "success", "chains": chains}

@app.get("/lot_config")
async def get_lot_config():
    """Get lot size configuration"""
    return {
        "fixed_lots": config["fixed_lot_sizes"],
        "manual_overrides": config.get("manual_lot_overrides", {}),
        "current_balance": mt5_client.get_account_balance(),
        "current_lot": risk_manager.get_fixed_lot_size(mt5_client.get_account_balance())
    }

@app.post("/set_lot_size")
async def set_lot_size(tier: int, lot_size: float):
    """Set manual lot size override"""
    try:
        risk_manager.set_manual_lot_size(tier, lot_size)
        return {"status": "success", "message": f"Lot size set: ${tier} → {lot_size}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/reset_stats")
async def reset_stats():
    """Reset risk manager stats (for testing only)"""
    try:
        risk_manager.daily_loss = 0.0
        risk_manager.daily_profit = 0.0
        risk_manager.lifetime_loss = 0.0
        risk_manager.total_trades = 0
        risk_manager.winning_trades = 0
        risk_manager.save_stats()
        return {"status": "success", "message": "Stats reset successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/status")
async def get_status():
    """Get bot status with open trades"""
    stats = risk_manager.get_stats()
    open_trades_data = []
    for trade in trading_engine.open_trades:
        open_trades_data.append(trade.to_dict())
    
    return {
        "status": "running",
        "trading_paused": trading_engine.is_paused,
        "simulation_mode": config["simulate_orders"],
        "daily_profit": stats["daily_profit"],
        "daily_loss": stats["daily_loss"],
        "lifetime_loss": stats["lifetime_loss"],
        "total_trades": stats["total_trades"],
        "winning_trades": stats["winning_trades"],
        "win_rate": stats["win_rate"],
        "open_trades": open_trades_data,
        "open_trades_count": len(trading_engine.open_trades),
        "mt5_connected": mt5_client.initialized,
        "dual_orders_enabled": config.get("dual_order_config", {}).get("enabled", True),
        "profit_booking_enabled": config.get("profit_booking_config", {}).get("enabled", True)
    }

def check_port_available(host: str, port: int) -> bool:
    """Check if port is available"""
    import socket
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            return True
    except OSError:
        return False

def kill_process_on_port(port: int) -> bool:
    """Kill process using the specified port (Windows)"""
    import subprocess
    try:
        # Find process using port
        result = subprocess.run(
            ["netstat", "-ano"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        for line in result.stdout.split('\n'):
            if f':{port}' in line and 'LISTENING' in line:
                parts = line.split()
                if len(parts) >= 5:
                    pid = parts[-1]
                    try:
                        # Kill the process
                        subprocess.run(
                            ["taskkill", "/F", "/PID", pid],
                            capture_output=True,
                            timeout=5
                        )
                        print(f"Killed process {pid} using port {port}")
                        return True
                    except Exception as e:
                        print(f"WARNING: Could not kill process {pid}: {e}")
                        return False
        return False
    except Exception as e:
        print(f"WARNING: Could not check port {port}: {e}")
        return False

if __name__ == "__main__":
    import argparse
    import socket
    import subprocess
    import time
    parser = argparse.ArgumentParser(description="Zepix Trading Bot v2.0")
    parser.add_argument("--host", default="0.0.0.0", help="Host address")
    parser.add_argument("--port", default=80, type=int, help="Port number (default: 80 for Windows VM)")
    args = parser.parse_args()
    
    # Skip port checking - bot works without web server binding
    # The bot operates via Telegram and MT5, web server is optional
    print(f"[INFO] Web server port {args.port} will be used if available")
    
    rr_ratio = config.get("rr_ratio", 1.0)
    print("=" * 50)
    print("ZEPIX TRADING BOT v2.0")
    print("=" * 50)
    print(f"Starting server on {args.host}:{args.port}")
    print("Features enabled:")
    print("+ Fixed lot sizes")
    print("+ Re-entry system") 
    print("+ SL hunting protection")
    print(f"+ 1:{rr_ratio} Risk-Reward")
    print("+ Progressive SL reduction")
    print("=" * 50)
    
    # DEBUG: verify menu keys (User Verification Request)
    try:
        from src.menu.menu_constants import REPLY_MENU_MAP
        print(f"[DEBUG-MENU] Active Menu Keys ({len(REPLY_MENU_MAP)}):")
        print(list(REPLY_MENU_MAP.keys()))
    except Exception as e:
        print(f"[DEBUG-MENU] Error loading menu map: {e}")
    
    # Start uvicorn server with automatic port permission handling
    try:
        print("[UVICORN] Starting Uvicorn server...")
        
        # Check if port 80 requires elevation and handle it
        needs_elevation = False
        if args.port < 1024 and sys.platform == 'win32':
            import ctypes
            try:
                is_admin = ctypes.windll.shell32.IsUserAnAdmin()
                if not is_admin:
                    needs_elevation = True
                    print(f"[WARN] Port {args.port} requires Administrator privileges on Windows")
                    print(f"[WARN] Attempting to grant permission automatically...")
                    
                    # Try to grant permission via netsh
                    import subprocess
                    try:
                        cmd = f'netsh http add urlacl url=http://+:{args.port}/ user=Everyone'
                        result = subprocess.run(
                            ['powershell', '-Command', f'Start-Process', 'netsh', '-ArgumentList', 
                             f'"http add urlacl url=http://+:{args.port}/ user=Everyone"', 
                             '-Verb', 'RunAs', '-WindowStyle', 'Hidden', '-Wait'],
                            capture_output=True,
                            text=True,
                            timeout=10
                        )
                        if result.returncode == 0:
                            print(f"[SUCCESS] Port {args.port} permission granted!")
                        else:
                            print(f"[INFO] Permission grant may have failed - trying to start anyway")
                    except Exception as perm_error:
                        print(f"[INFO] Could not auto-grant permission: {perm_error}")
            except Exception as admin_check_error:
                print(f"[INFO] Could not check admin status: {admin_check_error}")
        
        # Try to start the server
        try:
            # Simple uvicorn.run() call - let uvicorn handle everything
            print("[UVICORN] Starting Uvicorn with default settings...")
            sys.stdout.flush()
            uvicorn.run(
                app,
                host=args.host,
                port=args.port
            )
        except OSError as os_error:
            if os_error.errno == 10013 or 'permission' in str(os_error).lower():
                print(f"\n{'='*70}")
                print(f"❌ ERROR: Permission denied for port {args.port}")
                print(f"{'='*70}")
                print(f"\n🔧 SOLUTION:")
                print(f"   Run this command in PowerShell as Administrator (ONE TIME):")
                print(f"\n   netsh http add urlacl url=http://+:{args.port}/ user=Everyone\n")
                print(f"   Then restart the bot with:")
                print(f"   python src/main.py --host {args.host} --port {args.port}")
                print(f"\n{'='*70}\n")
                sys.exit(1)
            else:
                raise
                
    except KeyboardInterrupt:
        print("\n[INFO] Bot stopped by user")
    except Exception as e:
        print(f"[ERROR] Server error: {e}")
        import traceback
        traceback.print_exc()