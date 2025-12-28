import asyncio
from datetime import datetime, timedelta
from typing import Dict, Any, List
import time
from src.models import Alert, Trade, ReEntryChain, ProfitBookingChain
from src.config import Config
from src.managers.risk_manager import RiskManager
from src.clients.mt5_client import MT5Client
from src.processors.alert_processor import AlertProcessor
from src.database import TradeDatabase
from src.utils.pip_calculator import PipCalculator
from src.managers.timeframe_trend_manager import TimeframeTrendManager
from src.managers.reentry_manager import ReEntryManager
from src.services.price_monitor_service import PriceMonitorService
from src.services.reversal_exit_handler import ReversalExitHandler
from src.managers.dual_order_manager import DualOrderManager
from src.managers.profit_booking_manager import ProfitBookingManager
from src.managers.profit_booking_reentry_manager import ProfitBookingReEntryManager
from src.managers.session_manager import SessionManager
from src.managers.autonomous_system_manager import AutonomousSystemManager
from src.utils.optimized_logger import logger
import json
import uuid

class TradingEngine:
    def __init__(self, config: Config, risk_manager: RiskManager, 
                 mt5_client: MT5Client, telegram_bot, 
                 alert_processor: AlertProcessor):
        self.config = config
        self.risk_manager = risk_manager
        self.mt5_client = mt5_client
        self.telegram_bot = telegram_bot
        self.alert_processor = alert_processor
        
        # Track bot uptime
        self.start_time = time.time()
        
        # Circuit breaker for infinite loop protection
        self.monitor_error_count = 0
        self.max_monitor_errors = 10
        
        # Risk manager ko MT5 client set karo
        self.risk_manager.set_mt5_client(mt5_client)
        
        # Database for trade history
        self.db = TradeDatabase()
        
        # Initialize Session Manager (NEW)
        self.session_manager = SessionManager(config, self.db, mt5_client)
        
        # Core managers
        self.pip_calculator = PipCalculator(config)
        self.trend_manager = TimeframeTrendManager()
        self.reentry_manager = ReEntryManager(config, mt5_client)
        
        # NEW: Dual order and profit booking managers
        self.profit_booking_manager = ProfitBookingManager(
            config, mt5_client, self.pip_calculator, risk_manager, self.db
        )
        # Pass profit SL calculator to dual order manager for Order B
        self.dual_order_manager = DualOrderManager(
            config, risk_manager, mt5_client, self.pip_calculator,
            profit_sl_calculator=self.profit_booking_manager.profit_sl_calculator
        )
        
        # New Profit Booking Re-entry Manager
        self.profit_booking_reentry_manager = ProfitBookingReEntryManager(
            config, self.profit_booking_manager, mt5_client, self.reentry_manager.trend_analyzer
        )

        # Initialize Autonomous System Manager
        self.autonomous_manager = AutonomousSystemManager(
            config, self.reentry_manager, self.profit_booking_manager,
            self.profit_booking_reentry_manager, mt5_client, telegram_bot,
            self.risk_manager
        )
        
        # NEW: Advanced re-entry and exit handlers
        self.price_monitor = PriceMonitorService(
            config, mt5_client, self.reentry_manager, 
            self.trend_manager, self.pip_calculator, self
        )
        self.reversal_handler = ReversalExitHandler(
            config, mt5_client, telegram_bot, self.db, price_monitor=self.price_monitor
        )
        
        # Current signals per symbol
        self.current_signals = {}
        
        # Initialize logger
        self.logger = logger
        
        self.open_trades: List[Trade] = []
        self.is_paused = False
        self.trade_count = 0
        
        # Logic control flags
        self.logic1_enabled = True
        self.logic2_enabled = True  
        self.logic3_enabled = True
    
    def get_open_trades(self) -> List[Trade]:
        """Get list of currently open trades"""
        return self.open_trades
    
    @property
    def trading_enabled(self) -> bool:
        """Check if trading is enabled (not paused)"""
        return not self.is_paused

    async def initialize(self):
        """Initialize the trading engine"""
        success = self.mt5_client.initialize()
        if success:
            self.telegram_bot.send_message("✅ MT5 Connection Established")
            self.telegram_bot.set_trend_manager(self.trend_manager)
            
            # DIAGNOSTIC: Log re-entry configuration on startup
            re_entry_config = self.config.get("re_entry_config", {})
            import logging
            logger = logging.getLogger(__name__)
            logger.info(
                f"📋 [RE-ENTRY_CONFIG] Startup Configuration:\n"
                f"  SL Hunt Enabled: {re_entry_config.get('sl_hunt_reentry_enabled', False)}\n"
                f"  TP Re-entry Enabled: {re_entry_config.get('tp_reentry_enabled', False)}\n"
                f"  Exit Continuation Enabled: {re_entry_config.get('exit_continuation_enabled', False)}\n"
                f"  Monitor Interval: {re_entry_config.get('price_monitor_interval_seconds', 30)}s\n"
                f"  SL Hunt Offset: {re_entry_config.get('sl_hunt_offset_pips', 1.0)} pips\n"
                f"  TP Continuation Gap: {re_entry_config.get('tp_continuation_price_gap_pips', 2.0)} pips\n"
                f"  Max Chain Levels: {re_entry_config.get('max_chain_levels', 2)}\n"
                f"  SL Reduction Per Level: {re_entry_config.get('sl_reduction_per_level', 0.5)}"
            )
            
            # Start background price monitor
            await self.price_monitor.start()
            
            # DIAGNOSTIC: Verify service started
            if self.price_monitor.is_running:
                logger.info("✅ Price Monitor Service confirmed running after initialization")
            else:
                logger.error("❌ Price Monitor Service NOT running after initialization")
            
            # Recover profit booking chains from database
            if self.profit_booking_manager.is_enabled():
                self.profit_booking_manager.recover_chains_from_database(self.open_trades)
                # Handle orphaned orders
                self.profit_booking_manager.handle_orphaned_orders(self.open_trades)
                # Clean up stale chains (fixes infinite loop spam)
                self.profit_booking_manager.cleanup_stale_chains()
            
            print("SUCCESS: Trading engine initialized successfully")
            print("SUCCESS: Price monitor service started")
            if self.profit_booking_manager.is_enabled():
                print("SUCCESS: Profit booking manager initialized")
        return success

    def initialize_symbol_signals(self, symbol: str):
        """Initialize signal tracking for a new symbol"""
        if symbol not in self.current_signals:
            self.current_signals[symbol] = {
                '5m': None,
                '15m': None,
                '1h': None,
                '1d': None
            }

    async def process_alert(self, data: Dict[str, Any]) -> bool:
        """Process incoming alert from webhook"""
        try:
            alert = Alert(**data)
            symbol = alert.symbol
            
            # Initialize symbol signals if not exists
            self.initialize_symbol_signals(symbol)
            
            # NEW: Check for reversal exit FIRST before processing other alerts
            if alert.type in ['reversal', 'trend', 'entry', 'exit']:
                trades_to_close = await self.reversal_handler.check_reversal_exit(
                    alert, self.open_trades
                )
                
                
                for close_info in trades_to_close:
                    # FIX #10: Skip if trade already closed
                    if close_info['trade'].status == "closed":
                        continue
                    
                    await self.reversal_handler.execute_reversal_exit(
                        close_info['trade'],
                        close_info['exit_price'],
                        close_info['exit_reason']
                    )
                    # Remove from open trades
                    if close_info['trade'] in self.open_trades:
                        self.open_trades.remove(close_info['trade'])
                        self.risk_manager.remove_open_trade(close_info['trade'])
                    
                    # Stop TP continuation monitoring for this symbol (opposite signal received)
                    self.price_monitor.stop_tp_continuation(
                        close_info['trade'].symbol, 
                        f"Exit due to {close_info['exit_reason']}"
                    )
            
            # Update based on alert type
            if alert.type == 'bias':
                # Check if trend is manually locked before updating/notifying
                mode = self.trend_manager.get_mode(symbol, alert.tf)
                current_trend = self.trend_manager.get_trend(symbol, alert.tf)
                
                if mode == "MANUAL":
                    # Trend is locked - signal received but ignored
                    self.telegram_bot.send_message(
                        f"🔒 {symbol} {alert.tf.upper()} Signal Received: {alert.signal.upper()}\n"
                        f"Trend Locked: {current_trend} (Manual Mode)\n"
                        f"Signal ignored - trend will not change"
                    )
                else:
                    # Auto mode - update trend and notify
                    self.trend_manager.update_trend(symbol, alert.tf, alert.signal)
                    self.current_signals[symbol][alert.tf] = alert.signal
                    self.telegram_bot.send_message(
                        f"📊 {symbol} {alert.tf.upper()} Bias Updated: {alert.signal.upper()}"
                    )
                
            elif alert.type == 'trend':
                # Check if trend is manually locked before updating/notifying
                mode = self.trend_manager.get_mode(symbol, alert.tf)
                current_trend = self.trend_manager.get_trend(symbol, alert.tf)
                
                if mode == "MANUAL":
                    # Trend is locked - signal received but ignored
                    self.telegram_bot.send_message(
                        f"🔒 {symbol} {alert.tf.upper()} Signal Received: {alert.signal.upper()}\n"
                        f"Trend Locked: {current_trend} (Manual Mode)\n"
                        f"Signal ignored - trend will not change"
                    )
                else:
                    # Auto mode - update trend and notify
                    self.trend_manager.update_trend(symbol, alert.tf, alert.signal)
                    self.current_signals[symbol][alert.tf] = alert.signal
                    self.telegram_bot.send_message(
                        f"📊 {symbol} {alert.tf.upper()} Trend Updated: {alert.signal.upper()}"
                    )
            
            elif alert.type == 'entry':
                # NEW: Create session on entry signal
                direction = "BUY" if alert.signal == "buy" else "SELL"
                signal_type = "BULLISH" if alert.signal == "buy" else "BEARISH"
                self.session_manager.create_session(alert.symbol, direction, signal_type)
                
                # Execute trade based on entry signal
                await self.execute_trades(alert)
            
            elif alert.type == 'reversal':
                # Reversal alerts are handled above in exit check
                self.telegram_bot.send_message(f"🔄 {symbol} Reversal Signal: {alert.signal.upper()}")
            
            elif alert.type == 'exit':
                # Exit Appeared alerts are handled above in exit check
                exit_direction = "Bullish" if alert.signal == 'bull' else "Bearish"
                self.telegram_bot.send_message(f"⚠️ {symbol} Exit Appeared: {exit_direction}")
            
            return True
            
        except Exception as e:
            error_msg = f"Alert processing error: {str(e)}"
            self.telegram_bot.send_message(f"❌ {error_msg}")
            print(f"Error: {e}")
            return False

    async def execute_trades(self, alert: Alert):
        """Execute trades based on current mode and alert"""
        try:
            if self.is_paused:
                return
                
            symbol = alert.symbol
            
            # Check if specific logic is enabled
            if alert.tf == '5m' and not self.logic1_enabled:
                return
            if alert.tf == '15m' and not self.logic2_enabled:
                return
            if alert.tf == '1h' and not self.logic3_enabled:
                return
            
            # Determine which logic this trade belongs to
            if alert.tf == '5m':
                logic = "LOGIC1"
            elif alert.tf == '15m':
                logic = "LOGIC2"
            elif alert.tf == '1h':
                logic = "LOGIC3"
            else:
                return
            
            logger.log_system_event(f"Processing {alert.type} alert", f"Symbol: {symbol}, TF: {alert.tf}")
            
            # Check risk limits before trading
            can_trade = self.risk_manager.can_trade()
            logger.log_trading_debug(alert, {"aligned": False, "direction": "PENDING"}, "PENDING", logic)
            
            if not can_trade:
                logger.log_trading_error(f"Risk check failed - trading blocked", alert)
                self.telegram_bot.send_message("⛔ Trading paused due to risk limits")
                return
            
            # Check trend alignment for the logic
            alignment = self.trend_manager.check_logic_alignment(symbol, logic)
            logger.log_trading_debug(alert, alignment, "PENDING", logic)
            
            if not alignment["aligned"]:
                logger.log_trading_error(f"Trend not aligned for {logic}: {alignment}", alert)
                return
            
            # Check if signal matches the aligned direction
            signal_direction = "BULLISH" if alert.signal == "buy" else "BEARISH"
            logger.log_trading_debug(alert, alignment, signal_direction, logic)
            
            if alignment["direction"] == signal_direction:
                logger.log_system_event("Trade execution starting", f"Symbol: {symbol}, Direction: {signal_direction}")
                
                # CRITICAL LOGIC FIX: 
                # Disable Signal Hijack for Re-entries.
                # Fresh signals must ALWAYS trigger fresh dual orders.
                # Re-entries are handled autonomously by PriceMonitorService.
                
                # Old Logic (Removed):
                # reentry_info = self.reentry_manager.check_reentry_opportunity(...)
                # if reentry_info["is_reentry"]: await place_reentry_order(...)
                
                # New Logic: Always Place Fresh Order
                logger.log_system_event("Executing Fresh Order", f"Symbol: {symbol} (Signal Hijack Disabled)")
                await self.place_fresh_order(alert, logic)
            else:
                error_msg = f"Signal {signal_direction} doesn't match trend {alignment['direction']}"
                logger.log_trading_error(error_msg, alert)
                
        except Exception as e:
            logger.log_trading_error(f"Trade execution error: {str(e)}", alert)
            logger.error(f"Trade execution exception: {str(e)}", exc_info=True)

    async def place_fresh_order(self, alert: Alert, strategy: str):
        """Place a new trade order - now with dual orders (Order A: TP Trail, Order B: Profit Trail)"""
        try:
            # Get account balance and lot size
            account_balance = self.mt5_client.get_account_balance()
            lot_size = self.risk_manager.get_lot_size_for_logic(account_balance, logic=strategy)
            
            if lot_size <= 0:
                self.telegram_bot.send_message("⚠️ Invalid lot size")
                return
            
            # Check if dual orders enabled
            # Get active session ID
            session_id = self.session_manager.get_active_session()
            
            if self.dual_order_manager.is_enabled():
                # Create dual orders
                dual_result = self.dual_order_manager.create_dual_orders(alert, strategy, account_balance)
                
                # Assign session ID to dual orders
                if session_id:
                    if dual_result.get("order_a"):
                        dual_result["order_a"].session_id = session_id
                    if dual_result.get("order_b"):
                        dual_result["order_b"].session_id = session_id
                
                # 🆕 CREATE SHARED REENTRY CHAIN FIRST (100% FIX for SL Hunt)
                # This ensures both Order A and Order B share the SAME chain_id
                # that actually exists in active_chains dictionary
                shared_chain = None
                shared_chain_id = None
                
                if dual_result.get("order_a") and dual_result.get("order_b"):
                    # Create reentry chain BEFORE assigning to orders
                    order_a_temp = dual_result["order_a"]
                    
                    # Create chain using Order A as template
                    shared_chain = self.reentry_manager.create_chain(order_a_temp)
                    shared_chain_id = shared_chain.chain_id  # e.g., "XAUUSD_0e558f1c"
                    
                    # Assign SAME chain_id to BOTH orders
                    dual_result["order_a"].chain_id = shared_chain_id
                    dual_result["order_b"].chain_id = shared_chain_id
                    
                    self.logger.info(
                        f"[DUAL_ORDER_CHAIN] ✅ Created shared reentry chain {shared_chain_id} for BOTH orders"
                    )
                elif dual_result.get("order_a"):
                    dual_result["order_a"].chain_id = None  # Will be set by create_chain below
                elif dual_result.get("order_b"):
                    dual_result["order_b"].chain_id = None
                
                # Handle Order A (TP Trail)
                if dual_result["order_a_placed"] and dual_result["order_a"]:
                    order_a = dual_result["order_a"]
                    
                    # Use existing shared chain if dual orders, otherwise create new
                    if shared_chain is None:
                        chain = self.reentry_manager.create_chain(order_a)
                    else:
                        chain = shared_chain
                        # Update chain with Order A's trade_id
                        if order_a.trade_id and order_a.trade_id not in chain.trades:
                            chain.trades.append(order_a.trade_id)
                            chain.last_update = datetime.now().isoformat()
                    
                    # Register for SL hunt monitoring
                    if self.config.get("re_entry_config", {}).get("sl_hunt_reentry_enabled", True):
                        self.price_monitor.register_sl_hunt(order_a, strategy)
                    self.open_trades.append(order_a)
                    self.risk_manager.add_open_trade(order_a)
                    self.db.save_trade(order_a)
                    self.trade_count += 1
                
                # Handle Order B (Profit Trail)
                if dual_result["order_b_placed"] and dual_result["order_b"]:
                    order_b = dual_result["order_b"]
                    
                    # 🆕 ADD Order B TO SHARED REENTRY CHAIN
                    if shared_chain is not None:
                        if order_b.trade_id and order_b.trade_id not in shared_chain.trades:
                            shared_chain.trades.append(order_b.trade_id)
                            shared_chain.last_update = datetime.now().isoformat()
                        
                        self.logger.info(
                            f"[DUAL_ORDER_CHAIN] ✅ Order B #{order_b.trade_id} added to shared chain {shared_chain_id}"
                        )
                    
                    # Register Order B for SL hunt monitoring
                    if self.config.get("re_entry_config", {}).get("sl_hunt_reentry_enabled", True):
                        self.price_monitor.register_sl_hunt(order_b, strategy)
                    
                    # Create profit booking chain for Order B
                    if self.profit_booking_manager.is_enabled():
                        profit_chain = self.profit_booking_manager.create_profit_chain(order_b)
                        if profit_chain:
                            order_b.profit_chain_id = profit_chain.chain_id
                            order_b.profit_level = 0
                    self.open_trades.append(order_b)
                    self.risk_manager.add_open_trade(order_b)
                    self.db.save_trade(order_b)
                
                # FIX #4: Send detailed notification with individual order prices
                rr_ratio = self.config.get("rr_ratio", 1.0)
                
                # Get timeframe adjustments for display
                tf_details = ""
                timeframe_config = self.config.get("timeframe_specific_config", {})
                if timeframe_config.get("enabled", False) and strategy in timeframe_config:
                    logic_config = timeframe_config[strategy]
                    lot_mult = logic_config.get("lot_multiplier", 1.0)
                    sl_mult = logic_config.get("sl_multiplier", 1.0)
                    
                    # Calculate base values for display
                    base_lot = lot_size / lot_mult if lot_mult != 0 else lot_size
                    # Approx base SL (not exact due to pip calculation complexity, but good for display)
                    
                    tf_details = (
                        f"\n⏱️ Timeframe Logic: {strategy} ({logic_config.get('timeframe', 'N/A')})\n"
                        f"   Lot Mult: {lot_mult}x (Base: {base_lot:.2f})\n"
                        f"   SL Mult: {sl_mult}x"
                    )
                
                # Highlight Smart Adjustment in Notification
                if dual_result.get("smart_adjustment_info"):
                    tf_details += f"\n\n{dual_result['smart_adjustment_info']}"
                
                # 🆕 SCHEDULE ASYNCHRONOUS QUICK-CLOSE CHECK (100% FIX)
                # Non-blocking background task to check if Order B closes within 3 seconds
                if dual_result["order_b_placed"] and dual_result["order_b"]:
                    order_b_trade_id = dual_result["order_b"].trade_id
                    symbol = alert.symbol
                    
                    # Define async background check function
                    async def check_order_b_quick_close():
                        await asyncio.sleep(3)  # Non-blocking wait for 3 seconds
                        
                        import MetaTrader5 as mt5
                        position_b = mt5.positions_get(ticket=order_b_trade_id)
                        
                        if not position_b or len(position_b) == 0:
                            # Order B closed within 3 seconds - send follow-up notification
                            self.telegram_bot.send_message(
                                f"⚠️ ORDER B UPDATE: #{order_b_trade_id}\n"
                                f"Symbol: {symbol}\n"
                                f"Status: CLOSED IMMEDIATELY (within 3 seconds)\n"
                                f"Reason: Profit Trail SL too tight\n"
                                f"Note: Spread/slippage triggered instant close"
                            )
                    
                    # Schedule task in background (non-blocking)
                    asyncio.create_task(check_order_b_quick_close())

                if dual_result["order_a_placed"] and dual_result["order_b_placed"]:
                    order_a = dual_result["order_a"]
                    order_b = dual_result["order_b"]
                    message = (
                        f"🎯 DUAL ORDER PLACED #{self.trade_count}\n"
                        f"Strategy: {strategy}\n"
                        f"Symbol: {alert.symbol}\n"
                        f"Direction: {alert.signal.upper()}{tf_details}\n\n"
                        f"📈 Order A (TP Trail):\n"
                        f"  Entry: {order_a.entry:.5f}\n"
                        f"  SL: {order_a.sl:.5f}\n"
                        f"  TP: {order_a.tp:.5f}\n"
                        f"  Lots: {order_a.lot_size:.2f}\n\n"
                        f"💰 Order B (Profit Trail):\n"
                        f"  Entry: {order_b.entry:.5f}\n"
                        f"  SL: {order_b.sl:.5f}\n"
                        f"  TP: {order_b.tp:.5f}\n"
                        f"  Lots: {order_b.lot_size:.2f}\n\n"
                        f"Risk: 1:{rr_ratio} RR\n"
                        f"📌 Monitoring Order B for quick-close (will notify if closed < 3s)"
                    )
                elif dual_result["order_a_placed"]:
                    message = (
                        f"🎯 ORDER A PLACED #{self.trade_count}\n"
                        f"Strategy: {strategy}\n"
                        f"Symbol: {alert.symbol}\n"
                        f"Direction: {alert.signal.upper()}\n"
                        f"Entry: {alert.price:.5f}\n"
                        f"Order A (TP Trail): ✅\n"
                        f"Order B (Profit Trail): ❌ Failed\n"
                        f"Lots: {lot_size:.2f}\n"
                        f"Risk: 1:{rr_ratio} RR"
                    )
                elif dual_result["order_b_placed"]:
                    message = (
                        f"🎯 ORDER B PLACED #{self.trade_count}\n"
                        f"Strategy: {strategy}\n"
                        f"Symbol: {alert.symbol}\n"
                        f"Direction: {alert.signal.upper()}\n"
                        f"Entry: {alert.price:.5f}\n"
                        f"Order A (TP Trail): ❌ Failed\n"
                        f"Order B (Profit Trail): ✅\n"
                        f"Lots: {lot_size:.2f}\n"
                        f"Risk: 1:{rr_ratio} RR"
                    )
                else:
                    message = f"❌ Both orders failed for {alert.symbol}"
                    if dual_result.get("errors"):
                        message += f"\nErrors: {', '.join(dual_result['errors'])}"
                
                self.telegram_bot.send_message(message)
                
                # Log errors if any
                if dual_result.get("errors"):
                    for error in dual_result["errors"]:
                        print(f"WARNING: Dual order error: {error}")
                
                # CRITICAL FIX: Store entry alert ONLY after successful order execution
                # This prevents failed orders from blocking future legitimate alerts as "duplicates"
                if dual_result["order_a_placed"] or dual_result["order_b_placed"]:
                    self.alert_processor.store_entry_alert(alert)
                
                return
            
            # Fallback: Single order (if dual orders disabled)
            # Get symbol config for logging
            symbol_config = self.config["symbol_config"][alert.symbol]
            account_tier = self.pip_calculator._get_account_tier(account_balance)
            
            # Calculate SL and TP using pip calculator
            sl_price, sl_distance = self.pip_calculator.calculate_sl_price(
                alert.symbol, alert.price, alert.signal, lot_size, account_balance,
                logic=strategy
            )
            
            tp_price = self.pip_calculator.calculate_tp_price(
                alert.price, sl_price, alert.signal, self.config.get("rr_ratio", 1.0)
            )
            
            # Log SL/TP calculation details
            sl_pips = abs(alert.price - sl_price) / symbol_config["pip_size"]
            tp_pips = abs(tp_price - alert.price) / symbol_config["pip_size"]
            print(f"SL/TP Calculation:")
            print(f"   Symbol: {alert.symbol} | Lot: {lot_size:.2f}")
            print(f"   Entry: {alert.price:.5f}")
            print(f"   SL: {sl_price:.5f} ({sl_pips:.1f} pips)")
            print(f"   TP: {tp_price:.5f} ({tp_pips:.1f} pips)")
            print(f"   Risk: ${account_tier} tier | Volatility: {symbol_config['volatility']}")
            
            # Validate trade risk before execution
            validation = self.pip_calculator.validate_trade_risk(
                alert.symbol, lot_size, sl_pips, account_balance
            )
            print(f"   {validation['message']}")
            
            if not validation["valid"]:
                warning = (
                    f"⚠️ RISK VALIDATION WARNING\n"
                    f"Symbol: {alert.symbol}\n"
                    f"Expected Loss: ${validation['expected_loss']:.2f}\n"
                    f"Risk Cap: ${validation['risk_cap']:.2f}\n"
                    f"Trade will proceed but check SL system config!"
                )
                self.telegram_bot.send_message(warning)
            
            # Create trade object
            trade = Trade(
                symbol=alert.symbol,
                entry=alert.price,
                sl=sl_price,
                tp=tp_price,
                lot_size=lot_size,
                direction=alert.signal,
                strategy=strategy,
                open_time=datetime.now().isoformat(),
                original_entry=alert.price,
                original_sl_distance=sl_distance,
                session_id=session_id
            )
            
            # Execute trade
            if not self.config.get("simulate_orders", False):
                trade_id = self.mt5_client.place_order(
                    symbol=alert.symbol,
                    order_type=alert.signal,
                    lot_size=lot_size,
                    price=alert.price,
                    sl=sl_price,
                    tp=tp_price,
                    comment=f"{strategy}_FRESH"
                )
                if trade_id:
                    trade.trade_id = trade_id
                else:
                    self.telegram_bot.send_message(f"❌ Order placement failed for {alert.symbol}")
                    return
            
            # Create re-entry chain for this trade
            chain = self.reentry_manager.create_chain(trade)
            
            # Register for SL hunt monitoring
            if self.config.get("re_entry_config", {}).get("sl_hunt_reentry_enabled", True):
                self.price_monitor.register_sl_hunt(trade, strategy)
            
            self.open_trades.append(trade)
            self.risk_manager.add_open_trade(trade)
            self.db.save_trade(trade)
            self.trade_count += 1
            
            # Send notification
            rr_ratio = self.config.get("rr_ratio", 1.0)
            
            # Get timeframe adjustments for display
            tf_details = ""
            timeframe_config = self.config.get("timeframe_specific_config", {})
            if timeframe_config.get("enabled", False) and strategy in timeframe_config:
                logic_config = timeframe_config[strategy]
                lot_mult = logic_config.get("lot_multiplier", 1.0)
                sl_mult = logic_config.get("sl_multiplier", 1.0)
                
                # Calculate base values for display
                base_lot = lot_size / lot_mult if lot_mult != 0 else lot_size
                
                tf_details = (
                    f"\n⏱️ Timeframe Logic: {strategy} ({logic_config.get('timeframe', 'N/A')})\n"
                    f"   Lot Mult: {lot_mult}x (Base: {base_lot:.2f})\n"
                    f"   SL Mult: {sl_mult}x"
                )
                
            message = (
                f"🎯 NEW TRADE #{self.trade_count}\n"
                f"Strategy: {strategy}\n"
                f"Symbol: {alert.symbol}\n"
                f"Direction: {alert.signal.upper()}{tf_details}\n"
                f"Entry: {alert.price:.5f}\n"
                f"SL: {sl_price:.5f}\n"
                f"TP: {tp_price:.5f}\n"
                f"Lots: {lot_size:.2f}\n"
                f"Risk: 1:{rr_ratio} RR"
            )
            self.telegram_bot.send_message(message)
            
            # CRITICAL FIX: Store entry alert after successful execution
            self.alert_processor.store_entry_alert(alert)
            
        except Exception as e:
            error_msg = f"Trade execution error: {str(e)}"
            self.telegram_bot.send_message(f"❌ {error_msg}")
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()

    async def place_reentry_order(self, alert: Alert, strategy: str, reentry_info: Dict):
        """Place a re-entry trade - now with dual orders (Order A: TP Trail, Order B: Profit Trail)"""
        try:
            # Get account balance and lot size
            account_balance = self.mt5_client.get_account_balance()
            lot_size = self.risk_manager.get_lot_size_for_logic(account_balance, logic=strategy)
            
            # Get active session ID
            session_id = self.session_manager.get_active_session()
            
            # Get original SL distance from chain
            chain = self.reentry_manager.active_chains.get(reentry_info["chain_id"])
            if not chain:
                # No chain found, place fresh order instead
                await self.place_fresh_order(alert, strategy)
                return
            
            # Calculate adjusted SL distance for re-entry level
            adjusted_sl_distance = self.pip_calculator.adjust_sl_for_reentry(
                chain.original_sl_distance, 
                reentry_info["level"],
                self.config.get("re_entry_config", {}).get("sl_reduction_per_level", 0.2)
            )
            
            # Calculate SL and TP prices with configured RR ratio
            rr_ratio = self.config.get("rr_ratio", 1.0)
            if alert.signal == "buy":
                sl_price = alert.price - adjusted_sl_distance
                tp_price = alert.price + (adjusted_sl_distance * rr_ratio)
            else:
                sl_price = alert.price + adjusted_sl_distance
                tp_price = alert.price - (adjusted_sl_distance * rr_ratio)
            
            # Check if dual orders enabled
            if self.dual_order_manager.is_enabled():
                # Create Order A (TP Trail) for re-entry
                order_a = Trade(
                    symbol=alert.symbol,
                    entry=alert.price,
                    sl=sl_price,
                    tp=tp_price,
                    lot_size=lot_size,
                    direction=alert.signal,
                    strategy=strategy,
                    open_time=datetime.now().isoformat(),
                    chain_id=reentry_info["chain_id"],
                    chain_level=reentry_info["level"],
                    is_re_entry=True,
                    original_entry=chain.original_entry,
                    original_sl_distance=chain.original_sl_distance,
                    order_type="TP_TRAIL",
                    session_id=session_id
                )
                
                # Place Order A
                order_a_placed = False
                if not self.config.get("simulate_orders", False):
                    trade_id_a = self.mt5_client.place_order(
                        symbol=alert.symbol,
                        order_type=alert.signal,
                        lot_size=lot_size,
                        price=alert.price,
                        sl=sl_price,
                        tp=tp_price,
                        comment=f"{strategy}_RE{reentry_info['level']}_TP"
                    )
                    if trade_id_a:
                        order_a.trade_id = trade_id_a
                        order_a_placed = True
                else:
                    # Simulation mode
                    order_a.trade_id = int(datetime.now().timestamp() * 1000) % 1000000
                    order_a_placed = True
                
                # Create Order B (Profit Trail) for re-entry
                order_b = Trade(
                    symbol=alert.symbol,
                    entry=alert.price,
                    sl=sl_price,
                    tp=tp_price,
                    lot_size=lot_size,
                    direction=alert.signal,
                    strategy=strategy,
                    open_time=datetime.now().isoformat(),
                    chain_id=reentry_info["chain_id"],
                    chain_level=reentry_info["level"],
                    is_re_entry=True,
                    original_entry=chain.original_entry,
                    original_sl_distance=chain.original_sl_distance,
                    order_type="PROFIT_TRAIL",
                    session_id=session_id
                )
                
                # Place Order B independently
                order_b_placed = False
                if not self.config.get("simulate_orders", False):
                    trade_id_b = self.mt5_client.place_order(
                        symbol=alert.symbol,
                        order_type=alert.signal,
                        lot_size=lot_size,
                        price=alert.price,
                        sl=sl_price,
                        tp=tp_price,
                        comment=f"{strategy}_RE{reentry_info['level']}_PROFIT"
                    )
                    if trade_id_b:
                        order_b.trade_id = trade_id_b
                        order_b_placed = True
                else:
                    # Simulation mode
                    order_b.trade_id = int(datetime.now().timestamp() * 1000) % 1000000 + 1
                    order_b_placed = True
                
                # Handle Order A
                if order_a_placed:
                    # Update chain with Order A
                    self.reentry_manager.update_chain_level(reentry_info["chain_id"], order_a.trade_id)
                    self.open_trades.append(order_a)
                    self.risk_manager.add_open_trade(order_a)
                    self.db.save_trade(order_a)
                    self.trade_count += 1
                
                # Handle Order B
                if order_b_placed:
                    # Create profit booking chain for Order B if enabled
                    if self.profit_booking_manager.is_enabled():
                        profit_chain = self.profit_booking_manager.create_profit_chain(order_b)
                        if profit_chain:
                            order_b.profit_chain_id = profit_chain.chain_id
                            order_b.profit_level = 0
                    self.open_trades.append(order_b)
                    self.risk_manager.add_open_trade(order_b)
                    self.db.save_trade(order_b)
                
                # Send notification
                re_type = "TP Continuation" if reentry_info.get("type") == "tp_continuation" else "SL Recovery"
                if order_a_placed and order_b_placed:
                    message = (
                        f"🔄 DUAL RE-ENTRY TRADE #{self.trade_count}\n"
                        f"Type: {re_type} (Level {reentry_info['level']})\n"
                        f"Strategy: {strategy}\n"
                        f"Symbol: {alert.symbol}\n"
                        f"Direction: {alert.signal.upper()}\n"
                        f"Entry: {alert.price:.5f}\n"
                        f"Order A (TP Trail): ✅\n"
                        f"Order B (Profit Trail): ✅\n"
                        f"SL: {sl_price:.5f} (Reduced {int((1-reentry_info.get('sl_adjustment', 1.0))*100)}%)\n"
                        f"TP: {tp_price:.5f}\n"
                        f"Lots Each: {lot_size:.2f}"
                    )
                elif order_a_placed:
                    message = (
                        f"🔄 RE-ENTRY TRADE #{self.trade_count}\n"
                        f"Type: {re_type} (Level {reentry_info['level']})\n"
                        f"Strategy: {strategy}\n"
                        f"Symbol: {alert.symbol}\n"
                        f"Direction: {alert.signal.upper()}\n"
                        f"Entry: {alert.price:.5f}\n"
                        f"Order A (TP Trail): ✅\n"
                        f"Order B (Profit Trail): ❌ Failed\n"
                        f"SL: {sl_price:.5f}\n"
                        f"TP: {tp_price:.5f}\n"
                        f"Lots: {lot_size:.2f}"
                    )
                elif order_b_placed:
                    message = (
                        f"🔄 RE-ENTRY TRADE #{self.trade_count}\n"
                        f"Type: {re_type} (Level {reentry_info['level']})\n"
                        f"Strategy: {strategy}\n"
                        f"Symbol: {alert.symbol}\n"
                        f"Direction: {alert.signal.upper()}\n"
                        f"Entry: {alert.price:.5f}\n"
                        f"Order A (TP Trail): ❌ Failed\n"
                        f"Order B (Profit Trail): ✅\n"
                        f"SL: {sl_price:.5f}\n"
                        f"TP: {tp_price:.5f}\n"
                        f"Lots: {lot_size:.2f}"
                    )
                else:
                    message = f"❌ Both re-entry orders failed for {alert.symbol}"
                
                self.telegram_bot.send_message(message)
                
                # CRITICAL FIX: Store entry alert after successful re-entry execution
                if order_a_placed or order_b_placed:
                    self.alert_processor.store_entry_alert(alert)
                
                return
            
            # Fallback: Single order (if dual orders disabled)
            # Create trade object
            trade = Trade(
                symbol=alert.symbol,
                entry=alert.price,
                sl=sl_price,
                tp=tp_price,
                lot_size=lot_size,
                direction=alert.signal,
                strategy=strategy,
                open_time=datetime.now().isoformat(),
                chain_id=reentry_info["chain_id"],
                chain_level=reentry_info["level"],
                is_re_entry=True,
                original_entry=chain.original_entry,
                original_sl_distance=chain.original_sl_distance
            )
            
            # Execute trade
            if not self.config.get("simulate_orders", False):
                trade_id = self.mt5_client.place_order(
                    symbol=alert.symbol,
                    order_type=alert.signal,
                    lot_size=lot_size,
                    price=alert.price,
                    sl=sl_price,
                    tp=tp_price,
                    comment=f"{strategy}_RE{reentry_info['level']}"
                )
                if trade_id:
                    trade.trade_id = trade_id
                else:
                    self.telegram_bot.send_message(f"❌ Re-entry order failed for {alert.symbol}")
                    return
            else:
                # Simulation mode: generate pseudo trade ID
                trade.trade_id = int(datetime.now().timestamp() * 1000) % 1000000
            
            # Update chain with new trade (both live and simulation modes)
            self.reentry_manager.update_chain_level(reentry_info["chain_id"], trade.trade_id)
            
            self.open_trades.append(trade)
            self.risk_manager.add_open_trade(trade)
            self.db.save_trade(trade)
            self.trade_count += 1
            
            # Send notification
            re_type = "TP Continuation" if reentry_info.get("type") == "tp_continuation" else "SL Recovery"
            message = (
                f"🔄 RE-ENTRY TRADE #{self.trade_count}\n"
                f"Type: {re_type} (Level {reentry_info['level']})\n"
                f"Strategy: {strategy}\n"
                f"Symbol: {alert.symbol}\n"
                f"Direction: {alert.signal.upper()}\n"
                f"Entry: {alert.price:.5f}\n"
                f"SL: {sl_price:.5f} (Reduced {int((1-reentry_info.get('sl_adjustment', 1.0))*100)}%)\n"
                f"TP: {tp_price:.5f}\n"
                f"Lots: {lot_size:.2f}"
            )
            self.telegram_bot.send_message(message)
            
            # CRITICAL FIX: Store entry alert after successful re-entry execution
            self.alert_processor.store_entry_alert(alert)
            
        except Exception as e:
            error_msg = f"Re-entry execution error: {str(e)}"
            self.telegram_bot.send_message(f"❌ {error_msg}")
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()

    async def reconcile_with_mt5(self):
        """Sync bot's trade list with MT5 positions - auto-close orphaned trades"""
        try:
            import MetaTrader5 as mt5
            
            # Get all open positions from MT5
            mt5_positions = mt5.positions_get()
            mt5_ticket_ids = {pos.ticket for pos in mt5_positions} if mt5_positions else set()
            
            # Check each bot trade against MT5
            for trade in self.open_trades[:]:  # Use slice to avoid modifying list during iteration
                if trade.status == "closed":
                    continue
                    
                if trade.trade_id and trade.trade_id not in mt5_ticket_ids:
                    # Position doesn't exist in MT5 - was auto-closed by TP/SL
                    current_price = self.mt5_client.get_current_price(trade.symbol)
                    
                    # FIX #8: Determine close reason from PnL (positive = TP, negative = SL)
                    # Use actual profit from MT5 history if available
                    pnl = self.mt5_client.get_closed_trade_profit(trade.trade_id)
                    
                    if pnl is None:
                        # Fallback: Manual calculation (only if history fetch fails)
                        pnl = (current_price - trade.entry) * trade.lot_size * 100 if trade.direction == "buy" else (trade.entry - current_price) * trade.lot_size * 100
                    
                    if pnl > 0:
                        close_reason = "TP_HIT_AUTO_CLOSED"
                        print(f"Auto-reconciliation: Position {trade.trade_id} closed by Take Profit (PnL: ${pnl:.2f})")
                    else:
                        close_reason = "SL_HIT_AUTO_CLOSED"
                        print(f"Auto-reconciliation: Position {trade.trade_id} closed by Stop Loss (PnL: ${pnl:.2f})")
                    
                    await self.close_trade(trade, close_reason, current_price)
                    
                    # NEW: Check for Profit Order SL Hit
                    if close_reason == "SL_HIT_AUTO_CLOSED" and trade.profit_chain_id:
                        # Register for recovery re-entry
                        self.profit_booking_reentry_manager.register_sl_hit(
                            trade.profit_chain_id,
                            trade.symbol,
                            trade.direction,
                            trade.profit_level,
                            trade.sl,
                            pnl # Negative value
                        )
                        # Notify
                        self.telegram_bot.send_profit_hunt_notification(
                            trade.symbol, 
                            trade.profit_chain_id, 
                            trade.profit_level, 
                            pnl, 
                            abs(current_price - trade.sl)/self.pip_calculator.get_pip_size(trade.symbol)
                        )
                    
        except Exception as e:
            print(f"WARNING: Reconciliation error: {e}")
    
    async def manage_open_trades(self):
        """Monitor and manage open trades with circuit breaker"""
        while True:
            try:
                # MT5 Reconciliation - Check if positions still exist in MT5
                if not self.config["simulate_orders"]:
                    await self.reconcile_with_mt5()
                
                # 🔄 RUN AUTONOMOUS CHECKS (TP Continuation, Profit Checks)
                if hasattr(self, 'autonomous_manager') and self.autonomous_manager:
                    await self.autonomous_manager.run_autonomous_checks(self.open_trades, self)
                
                # Remove closed trades from list
                self.open_trades = [t for t in self.open_trades if t.status != "closed"]
                
                # Check if session should end (all positions closed)
                closed_session = self.session_manager.check_session_end(self.open_trades)
                
                if closed_session:
                    pnl = closed_session.get('total_pnl', 0)
                    win_rate = closed_session.get('breakdown', {}).get('win_rate', 0)
                    s_id = closed_session.get('session_id')
                    icon = "💰" if pnl > 0 else "❌"
                    
                    self.telegram_bot.send_message(
                        f"{icon} <b>SESSION COMPLETED #{s_id.split('_')[-1]}</b>\n"
                        f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
                        f"💵 P&L: ${pnl:.2f}\n"
                        f"🎯 Win Rate: {win_rate:.1f}%\n"
                        f"📝 Trades: {closed_session.get('total_trades', 0)}\n\n"
                        f"See report: /session_report_{s_id}"
                    )
                    
                    # CRITICAL FIX #5: Zombie Chains
                    # When session ends, clear all background monitoring
                    self.price_monitor.clear_all_monitoring()
                    logger.info("✅ Session Closed -> Monitoring Cleared (Clean Slate)")
                
                for trade in self.open_trades:
                    if trade.status == "closed":
                        continue
                    
                    # Get current price
                    current_price = self.mt5_client.get_current_price(trade.symbol)
                    if current_price == 0:
                        continue
                    
                    # Check SL hit
                    if ((trade.direction == "buy" and current_price <= trade.sl) or
                        (trade.direction == "sell" and current_price >= trade.sl)):
                        await self.close_trade(trade, "SL_HIT", current_price)
                        self.reentry_manager.record_sl_hit(trade)
                        
                        # NEW: Register for SL hunt re-entry monitoring via AUTONOMOUS SYSTEM
                        # REROUTED: Uses 1s precision monitor & symbol-specific windows
                        # NEW: Register for SL hunt re-entry monitoring via AUTONOMOUS SYSTEM
                        # REROUTED: Uses 1s precision monitor & symbol-specific windows
                        if hasattr(self, 'autonomous_manager') and self.autonomous_manager:
                            self.autonomous_manager.register_sl_recovery(trade, trade.strategy)
                        # Fallback for legacy support
                        elif self.config["re_entry_config"]["sl_hunt_reentry_enabled"]:
                            self.price_monitor.register_sl_hunt(trade, trade.strategy)
                        continue
                    
                    # Check TP hit
                    if ((trade.direction == "buy" and current_price >= trade.tp) or
                        (trade.direction == "sell" and current_price <= trade.tp)):
                        # BACKGROUND LOOP - Silenced for clean logs (only Telegram notification sent)
                        # TP hit detected, closing trade and processing re-entry if enabled
                        
                        await self.close_trade(trade, "TP_HIT", current_price)
                        self.reentry_manager.record_tp_hit(trade, current_price)
                        
                        # Register for TP continuation re-entry monitoring if enabled
                        tp_reentry_enabled = self.config["re_entry_config"].get("tp_reentry_enabled", False)
                        if tp_reentry_enabled:
                            self.price_monitor.register_tp_continuation(trade, current_price, trade.strategy)
                        continue
                    
                    # Check trend reversal exit
                    if self.should_exit_by_trend_reversal(trade):
                        await self.close_trade(trade, "TREND_REVERSAL", current_price)
                        continue
                
                await asyncio.sleep(5)
                self.monitor_error_count = 0  # Reset on success
                
            except asyncio.CancelledError:
                logger.info("Trade monitor cancelled - graceful shutdown")
                break
            except Exception as e:
                self.monitor_error_count += 1
                logger.error(f"Trade monitor error #{self.monitor_error_count}: {str(e)}")
                
                if self.monitor_error_count >= self.max_monitor_errors:
                    logger.critical("🚨 Too many monitor errors - stopping trade monitoring")
                    self.telegram_bot.send_message("🚨 CRITICAL: Trade monitor stopped due to repeated errors")
                    break
                await asyncio.sleep(30)

    def should_exit_by_trend_reversal(self, trade: Trade) -> bool:
        """Check if we should exit due to trend reversal"""
        # Grace period: Don't exit trades within first 5 minutes of entry
        # This prevents premature exits when signals are still arriving
        try:
            from datetime import datetime, timedelta
            trade_open_time = datetime.fromisoformat(trade.open_time)
            time_since_open = datetime.now() - trade_open_time
            
            if time_since_open < timedelta(minutes=5):
                return False  # Grace period - don't check trend reversal yet
        except:
            pass  # If parsing fails, proceed with normal check
        
        alignment = self.trend_manager.check_logic_alignment(trade.symbol, trade.strategy)
        
        # Only exit if trend is CLEARLY reversed (not just neutral)
        if not alignment["aligned"]:
            return False  # Don't exit on neutral - only on clear reversal
        
        trade_direction = "BULLISH" if trade.direction == "buy" else "BEARISH"
        if alignment["direction"] != trade_direction:
            return True  # Exit on OPPOSITE direction
        
        return False

    async def close_trade(self, trade: Trade, reason: str, current_price: float):
        """Close a trade"""
        notification_sent = False
        try:
            # FIX #5: Add retry logic with exponential backoff for MT5 close
            if not self.config["simulate_orders"] and trade.trade_id:
                import MetaTrader5 as mt5
                import asyncio
                
                max_retries = 3
                retry_delay = 1  # seconds
                success = False
                
                for attempt in range(max_retries):
                    # Check if position still exists before attempting close
                    position = mt5.positions_get(ticket=trade.trade_id)
                    
                    if not position:
                        # Get actual PnL from MT5 history
                        closed_profit = self.mt5_client.get_closed_trade_profit(trade.trade_id)
                        
                        print(f"Position {trade.trade_id} already closed externally")
                        
                        # 🆕 SEND TELEGRAM NOTIFICATION FOR MANUAL CLOSE
                        self.telegram_bot.send_message(
                            f"📊 MANUAL CLOSE DETECTED\n"
                            f"Order: #{trade.trade_id}\n"
                            f"Symbol: {trade.symbol}\n"
                            f"Direction: {trade.direction.upper()}\n"
                            f"Entry: {trade.entry:.5f}\n"
                            f"Close: {current_price:.5f}\n"
                            f"PnL: ${closed_profit:.2f}\n"
                            f"Reason: Closed outside bot (MT5 app)"
                        )
                        notification_sent = True
                        
                        success = True  # Position already closed, consider it success
                        break
                    
                    # Attempt to close
                    success = self.mt5_client.close_position(trade.trade_id)
                    
                    if success:
                        print(f"Position {trade.trade_id} closed successfully")
                        break
                    else:
                        if attempt < max_retries - 1:
                            print(f"Close failed (attempt {attempt+1}/{max_retries}), retrying in {retry_delay}s...")
                            await asyncio.sleep(retry_delay)
                            retry_delay *= 2  # Exponential backoff
                        else:
                            error_msg = f"Failed to close trade {trade.trade_id} after {max_retries} attempts"
                            print(f"ERROR: {error_msg}")
                            self.telegram_bot.send_message(f"⚠️ {error_msg} - manual intervention may be required")
                            return  # Don't mark as closed if MT5 close failed
                
                if not success:
                    return  # Exit early if all retries failed
            
            # Only mark as closed if MT5 close succeeded or we're in simulation
            trade.status = "closed"
            trade.close_time = datetime.now().isoformat()
            self.risk_manager.remove_open_trade(trade)
            
            # 🆕 REVERSE SHIELD HOOK: Detect if shield trade closed
            if hasattr(self, 'autonomous_manager') and \
               hasattr(self.autonomous_manager, 'reverse_shield_manager') and \
               self.autonomous_manager.reverse_shield_manager:
                self.autonomous_manager.reverse_shield_manager.on_shield_close(trade.trade_id)
            
            # Remove from open trades list immediately
            if trade in self.open_trades:
                self.open_trades.remove(trade)
            
            # Calculate PnL: Use ACTUAL profit from MT5 history
            # This ensures we account for commission, swap, and broker-specific contract sizes
            if trade.trade_id and not self.config["simulate_orders"]:
                # Fetch real profit from MT5 history
                pnl = self.mt5_client.get_closed_trade_profit(trade.trade_id)
                
                if pnl is None:
                    # Fallback: Try to get from last position info if history deal missing
                    pnl = self._calculate_pnl_fallback(trade, current_price)
            else:
                # Simulation mode: Use manual calculation
                pnl = self._calculate_pnl_fallback(trade, current_price)
            
            trade.pnl = pnl
            
            # Calculate pips moved for logging
            try:
                price_diff = abs(current_price - trade.entry)
                pip_size = 0.01 if "JPY" in trade.symbol else 0.0001
                pips_moved = price_diff / pip_size
            except:
                pips_moved = 0.0  # Fallback to prevent error
            
            # Log closure details
            print(f"Trade Closed: {trade.symbol} {trade.direction.upper()}")
            print(f"   Entry: {trade.entry:.5f} -> Close: {current_price:.5f}")
            print(f"   Pips: {pips_moved:.1f} | PnL: ${pnl:.2f}")
            print(f"   Reason: {reason}")
            
            # Update risk manager
            self.risk_manager.update_pnl(pnl)
            
            # Update trade in database
            self.db.save_trade(trade)
            
            # FIX #3: Add order_type label to distinguish Order A vs Order B
            order_label = ""
            if hasattr(trade, 'order_type') and trade.order_type:
                if trade.order_type == "TP_TRAIL":
                    order_label = " [Order A - TP Trail]"
                elif trade.order_type == "PROFIT_TRAIL":
                    order_label = " [Order B - Profit Trail]"
            
            # Send notification
            # FIX: Suppress duplicate notifications
            # 1. If notification_sent is True (Manual Close), don't send again
            # 2. If it's a Profit Booking chain and PnL > 0, suppress individual "TRADE CLOSED"
            #    (Rely on "LEVEL UP" message from ProfitBookingManager to avoid spam)
            should_notify = not notification_sent
            if should_notify and trade.profit_chain_id and pnl > 0:
                should_notify = False
            
            if should_notify:
                emoji = "✅" if pnl >= 0 else "❌"
                chain_info = f" (Chain Level {trade.chain_level})" if trade.is_re_entry else ""
                
                message = (
                    f"{emoji} TRADE CLOSED{chain_info}{order_label}\n"
                    f"Reason: {reason}\n"
                    f"Symbol: {trade.symbol}\n"
                    f"Strategy: {trade.strategy}\n"
                    f"PnL: ${pnl:.2f}"
                )
                self.telegram_bot.send_message(message)
            
            # 🔗 AUTONOMOUS SYSTEM HOOKS (NEW)
            
            # 1. Handle SL Hunt Recovery Outcome
            if hasattr(trade, 'order_type') and trade.order_type == "SL_RECOVERY":
                if pnl >= 0:
                    self.autonomous_manager.handle_recovery_success(trade.chain_id, trade)
                else:
                    self.autonomous_manager.handle_recovery_failure(trade.chain_id, trade)
            
            # 2. Handle Profit Booking Outcome
            if hasattr(trade, 'profit_chain_id') and trade.profit_chain_id:
                # Notify Profit Manager
                if hasattr(self.profit_booking_manager, 'handle_trade_close'):
                    await self.profit_booking_manager.handle_trade_close(trade, self.open_trades, self)
                else:
                    # Fallback if method doesn't exist yet (will implement next)
                    # For now just trigger progress check
                    chain = self.profit_booking_manager.get_chain(trade.profit_chain_id)
                    if chain:
                        await self.profit_booking_manager.check_and_progress_chain(
                            chain, self.open_trades, self
                        )
            
            # 3. Handle Exit Continuation Monitoring
            if reason in ["TREND_REVERSAL", "MANUAL_EXIT", "Exit Appeared"] or "MANUAL" in reason.upper():
                self.autonomous_manager.register_exit_continuation(trade, reason)
            
        except Exception as e:
            error_msg = f"Trade close error: {str(e)}"
            self.telegram_bot.send_message(f"❌ {error_msg}")

    # Logic control methods
    def enable_logic(self, logic_number: int):
        if logic_number == 1:
            self.logic1_enabled = True
        elif logic_number == 2:
            self.logic2_enabled = True
        elif logic_number == 3:
            self.logic3_enabled = True

    def disable_logic(self, logic_number: int):
        if logic_number == 1:
            self.logic1_enabled = False
        elif logic_number == 2:
            self.logic2_enabled = False
        elif logic_number == 3:
            self.logic3_enabled = False

    def get_logic_status(self) -> Dict[str, bool]:
        return {
            "logic1": self.logic1_enabled,
            "logic2": self.logic2_enabled,
            "logic3": self.logic3_enabled
        }
    def _calculate_pnl_fallback(self, trade: Trade, current_price: float) -> float:
        """
        Fallback P&L calculation for simulation mode only.
        Also used as last resort if MT5 history is unavailable.
        """
        try:
            symbol_config = self.config["symbol_config"][trade.symbol]
            pip_size = symbol_config["pip_size"]
            pip_value_per_std_lot = symbol_config["pip_value_per_std_lot"]
            
            # Calculate price difference in pips
            price_diff = current_price - trade.entry if trade.direction == "buy" else trade.entry - current_price
            pips_moved = price_diff / pip_size
            
            # Calculate PnL: pips   pip_value   lot_size
            pip_value = pip_value_per_std_lot * trade.lot_size
            return pips_moved * pip_value
        except Exception as e:
            print(f"Error in manual P&L calculation: {e}")
            return 0.0
