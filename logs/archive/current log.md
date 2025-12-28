Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\WINDOWS\system32> cd "c:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main"
PS C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main> python src/main.py --host 0.0.0.0 --port 80
[EVENT-LOOP] Set WindowsProactorEventLoopPolicy on Windows
[LOGGING CONFIG] Loaded saved log level: DEBUG
[LOGGING CONFIG] Loaded trading_debug: True
═══════════════════════════════════════
🚀 BOT STARTING - LOGGING LEVEL: DEBUG
═══════════════════════════════════════
2025-12-19 01:25:37 - __main__ - INFO - Bot starting with logging level: DEBUG
[LOGGING CONFIG] Loaded saved log level: DEBUG
[LOGGING CONFIG] Loaded trading_debug: True
Config loaded - MT5 Login: 308646228, Server: XMGlobal-MT5 6
[INIT] Cleaning up webhooks on bot initialization...
2025-12-19 01:25:41 - src.clients.telegram_bot - INFO - [POLLING-INIT] Cleaning up any existing webhooks...
2025-12-19 01:25:43 - src.clients.telegram_bot - INFO - [POLLING-INIT] No webhook found on Telegram servers
2025-12-19 01:25:44 - src.clients.telegram_bot - INFO - [POLLING-INIT] Webhook deleted successfully
2025-12-19 01:25:44 - src.clients.telegram_bot - DEBUG - [POLLING-INIT] Waiting 3 seconds for webhook deletion to propagate...
2025-12-19 01:25:48 - src.clients.telegram_bot - INFO - [POLLING-INIT] ✅ Webhook cleanup verified - ready for polling
[INIT] Webhook cleanup complete
2025-12-19 01:25:48 - src.managers.session_manager - INFO - ✅ Recovered active session: SES_20251213_172949_08c3a6
DEBUG: TimeframeTrendManager using config file: C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main\config\timeframe_trends.json
SUCCESS: Loaded trends from C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main\config\timeframe_trends.json
DEBUG: Loaded MANUAL trend for AUDUSD 1h: BULLISH
DEBUG: Total manual trends loaded: 1
2025-12-19 01:25:48 - src.managers.recovery_window_monitor - INFO - ✅ RecoveryWindowMonitor initialized
2025-12-19 01:25:48 - src.managers.profit_protection_manager - INFO -
Profit Protection Settings Loaded:
├─ Enabled: True
├─ Mode: ⚖️ BALANCED
├─ Multiplier: 6.0x
├─ Min Threshold: $20.0
├─ Order A: ON ✅
└─ Order B: ON ✅

2025-12-19 01:25:48 - src.managers.profit_protection_manager - INFO - ✅ ProfitProtectionManager initialized
2025-12-19 01:25:48 - src.managers.sl_reduction_optimizer - INFO -
SL Reduction Settings Loaded:
├─ Enabled: True
├─ Strategy: ⚖️ BALANCED
├─ Reduction: 30%
└─ Description: Recommended for most conditions

2025-12-19 01:25:48 - src.managers.sl_reduction_optimizer - INFO - ✅ SLReductionOptimizer initialized
✅ Fine-Tune managers initialized (Recovery Monitor, Profit Protection, SL Optimizer)
✅ Autonomous System Manager initialized
2025-12-19 01:25:48 - src.menu.fine_tune_menu_handler - INFO - ✅ FineTuneMenuHandler initialized (Compatible Mode)
✅ TelegramBot: Fine-Tune Menu Handler initialized
✅ TelegramBot: Re-entry Menu Handler initialized
✅ TelegramBot: Profit Booking Menu Handler initialized
[OK] Dependencies set immediately in TelegramBot
[INFO] Web server port 80 will be used if available
==================================================
ZEPIX TRADING BOT v2.0
==================================================
Starting server on 0.0.0.0:80
Features enabled:
+ Fixed lot sizes
+ Re-entry system
+ SL hunting protection
+ 1:1.5 Risk-Reward
+ Progressive SL reduction
==================================================
[UVICORN] Starting Uvicorn server...
[UVICORN] Starting Uvicorn with default settings...
C:\Users\Ansh Shivaay Gupta\AppData\Roaming\Python\Python312\site-packages\telegram\utils\request.py:49: UserWarning: python-telegram-bot is using upstream urllib3. This is allowed but not supported by python-telegram-bot maintainers.
  warnings.warn(
2025-12-19 01:25:48 - asyncio - DEBUG - Using proactor: IocpProactor
←[32mINFO←[0m:     Started server process [←[36m12476←[0m]
←[32mINFO←[0m:     Waiting for application startup.
======================================================================
STARTING ZEPIX TRADING BOT v2.0
======================================================================
Initializing components...
2025-12-19 01:25:48 - src.menu.fine_tune_menu_handler - INFO - ✅ FineTuneMenuHandler initialized (Compatible Mode)
✅ TelegramBot: Fine-Tune Menu Handler initialized
✅ TelegramBot: Re-entry Menu Handler initialized
✅ TelegramBot: Profit Booking Menu Handler initialized
SUCCESS: MT5 connection established
Account Balance: $9358.79
Account: 308646228 | Server: XMGlobal-MT5 6
2025-12-19 01:25:50 - src.clients.telegram_bot - INFO - SUCCESS: Trend manager set in Telegram bot
2025-12-19 01:25:50 - src.core.trading_engine - INFO - 📋 [RE-ENTRY_CONFIG] Startup Configuration:
  SL Hunt Enabled: True
  TP Re-entry Enabled: True
  Exit Continuation Enabled: True
  Monitor Interval: 2s
  SL Hunt Offset: 1.0 pips
  TP Continuation Gap: 2.0 pips
  Max Chain Levels: 5
  SL Reduction Per Level: 0.3
2025-12-19 01:25:50 - src.services.price_monitor_service - INFO - ✅ Price Monitor Service started successfully - Task created: <Task pending name='Task-3' coro=<PriceMonitorService._monitor_loop() running at C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main\src\services\price_monitor_service.py:129>>, is_running: True
2025-12-19 01:25:50 - src.core.trading_engine - INFO - ✅ Price Monitor Service confirmed running after initialization
2025-12-19 01:25:50 - src.managers.profit_booking_manager - INFO - SUCCESS: Recovered 0 profit booking chains from database
SUCCESS: Trading engine initialized successfully
SUCCESS: Price monitor service started
SUCCESS: Profit booking manager initialized
[OK] Injected trend_manager and telegram_bot into alert_processor
[OK] Trade monitor started
[POLLING-THREAD] Polling thread started
[OK] Telegram polling thread started
[LIFESPAN] Yielding control - bot is now running
======================================================================
✅✅✅ BOT IS LIVE NOW - READY FOR TELEGRAM COMMANDS ✅✅✅
======================================================================
2025-12-19 01:25:52 - src.services.price_monitor_service - DEBUG - 🔄 Monitor loop started - Interval: 2s, Config: SL Hunt=True, TP=True, Exit=True
2025-12-19 01:25:52 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] poll_commands() started, stop_event=False
2025-12-19 01:25:52 - src.clients.telegram_bot - INFO - SUCCESS: Telegram bot polling started
[POLLING-THREAD] Polling thread exited
2025-12-19 01:25:52 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:25:52 - src.clients.telegram_bot - INFO - [POLLING] Starting polling loop...
←[32mINFO←[0m:     Application startup complete.
2025-12-19 01:25:52 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 1 starting...
←[32mINFO←[0m:     Uvicorn running on ←[1mhttp://0.0.0.0:80←[0m (Press CTRL+C to quit)
2025-12-19 01:25:52 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 01:25:52 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-1] Making request to Telegram...
2025-12-19 01:25:54 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:25:56 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:25:58 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:00 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:02 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:04 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:06 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:08 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:10 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:10 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9358.79 | Equity: $9358.79 | Used: $0.00
2025-12-19 01:26:12 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:14 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:16 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:18 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:20 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:22 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:23 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 01:26:23 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-1] Got response: status=200
2025-12-19 01:26:23 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-1] No new updates (updates array empty)
2025-12-19 01:26:23 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 2 starting...
2025-12-19 01:26:23 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 01:26:23 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-2] Making request to Telegram...
2025-12-19 01:26:24 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:26 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:28 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:30 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:30 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9358.79 | Equity: $9358.79 | Used: $0.00
2025-12-19 01:26:32 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:34 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:36 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:38 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:40 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:42 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:52372 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 01:26:44 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:46 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:48 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:50 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:50 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9358.79 | Equity: $9358.79 | Used: $0.00
2025-12-19 01:26:52 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:53 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 01:26:53 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-2] Got response: status=200
2025-12-19 01:26:53 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-2] No new updates (updates array empty)
2025-12-19 01:26:53 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 3 starting...
2025-12-19 01:26:53 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 01:26:53 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-3] Making request to Telegram...
2025-12-19 01:26:54 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
Webhook received: {
  "type": "entry",
  "symbol": "XAUUSD",
  "signal": "sell",
  "tf": "5m",
  "price": 4323.21,
  "strategy": "ZepixPremium"
}
ALERT: Received alert: {'type': 'entry', 'symbol': 'XAUUSD', 'signal': 'sell', 'tf': '5m', 'price': 4323.21, 'strategy': 'ZepixPremium'}
INFO: Entry alert validated but NOT stored (will store after execution)
SUCCESS: Alert validation successful
2025-12-19 01:26:55 - src.managers.session_manager - WARNING - Session already active: SES_20251213_172949_08c3a6
[2025-12-19 01:26:55] 🔔 Processing entry alert | Symbol: XAUUSD, TF: 5m
[2025-12-19 01:26:55] 🔍 TRADING_DEBUG: Alert=sell, TF=5m, Symbol=XAUUSD
[2025-12-19 01:26:55] 🔍 TRADING_DEBUG: Alignment={'aligned': False, 'direction': 'PENDING'}
[2025-12-19 01:26:55] 🔍 TRADING_DEBUG: SignalDir=PENDING, Logic=LOGIC1
2025-12-19 01:26:55 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BEARISH, 15M=BEARISH, Direction=BEARISH)
[2025-12-19 01:26:55] 🔍 TRADING_DEBUG: Alert=sell, TF=5m, Symbol=XAUUSD
[2025-12-19 01:26:55] 🔍 TRADING_DEBUG: Alignment={'aligned': True, 'direction': 'BEARISH', 'details': {'1h': 'BEARISH', '15m': 'BEARISH'}, 'failure_reason': None}
[2025-12-19 01:26:55] 🔍 TRADING_DEBUG: SignalDir=PENDING, Logic=LOGIC1
[2025-12-19 01:26:55] 🔍 TRADING_DEBUG: Alert=sell, TF=5m, Symbol=XAUUSD
[2025-12-19 01:26:55] 🔍 TRADING_DEBUG: Alignment={'aligned': True, 'direction': 'BEARISH', 'details': {'1h': 'BEARISH', '15m': 'BEARISH'}, 'failure_reason': None}
[2025-12-19 01:26:55] 🔍 TRADING_DEBUG: SignalDir=BEARISH, Logic=LOGIC1
[2025-12-19 01:26:55] 🔔 Trade execution starting | Symbol: XAUUSD, Direction: BEARISH
2025-12-19 01:26:55 - src.managers.dual_order_manager - DEBUG - [DUAL_ORDER_LOT_SIZE] Symbol=XAUUSD Balance=$9358.79 Requested Lot=0.06
2025-12-19 01:26:55 - src.managers.dual_order_manager - WARNING - 🔧 SMART ADJUSTMENT: Lot reduced 0.062 -> 0.05 to fit daily limit (Risk: $124.00 -> $100.00)
2025-12-19 01:26:55 - src.managers.dual_order_manager - INFO - 🔧 SMART ADJUSTMENT: Lot reduced 0.06 -> 0.05 to fit daily limit.
2025-12-19 01:26:55 - src.managers.dual_order_manager - DEBUG - [DUAL_ORDER_RISK] Symbol=XAUUSD Valid=True Reason=Auto-adjusted lot to 0.05 to fit daily limit
2025-12-19 01:26:55 - src.clients.mt5_client - DEBUG - Symbol mapping: XAUUSD -> GOLD
2025-12-19 01:26:55 - src.clients.mt5_client - INFO - VALIDATION DEBUG: Symbol=XAUUSD, OrderType=sell, Price=4322.88, SL=4333.21, TP=4308.21
2025-12-19 01:26:55 - src.clients.mt5_client - INFO - VALIDATION: Symbol mapped XAUUSD -> GOLD
2025-12-19 01:26:55 - src.clients.mt5_client - INFO - VALIDATION: Symbol info retrieved for GOLD - Visible=True, Digits=2
2025-12-19 01:26:55 - src.clients.mt5_client - INFO - VALIDATION: StopsLevel=0, Point=0.01, MinDistance=0.10000
2025-12-19 01:26:55 - src.clients.mt5_client - INFO - VALIDATION: SELL order SL distance=10.33000, MinRequired=0.10000
2025-12-19 01:26:55 - src.clients.mt5_client - INFO - VALIDATION: SELL order TP distance=14.67000, MinRequired=0.10000
2025-12-19 01:26:55 - src.clients.mt5_client - INFO - VALIDATION PASSED: All checks passed for XAUUSD (GOLD)
SUCCESS: Order placed successfully: Ticket #493984941
2025-12-19 01:26:55 - src.clients.mt5_client - INFO - VALIDATION DEBUG: Symbol=XAUUSD, OrderType=sell, Price=4322.88, SL=4325.21, TP=4320.21
2025-12-19 01:26:55 - src.clients.mt5_client - INFO - VALIDATION: Symbol mapped XAUUSD -> GOLD
2025-12-19 01:26:55 - src.clients.mt5_client - INFO - VALIDATION: Symbol info retrieved for GOLD - Visible=True, Digits=2
2025-12-19 01:26:55 - src.clients.mt5_client - INFO - VALIDATION: StopsLevel=0, Point=0.01, MinDistance=0.10000
2025-12-19 01:26:55 - src.clients.mt5_client - INFO - VALIDATION: SELL order SL distance=2.33000, MinRequired=0.10000
2025-12-19 01:26:55 - src.clients.mt5_client - INFO - VALIDATION: SELL order TP distance=2.67000, MinRequired=0.10000
2025-12-19 01:26:55 - src.clients.mt5_client - INFO - VALIDATION PASSED: All checks passed for XAUUSD (GOLD)
SUCCESS: Order placed successfully: Ticket #493984942
2025-12-19 01:26:56 - src.managers.dual_order_manager - INFO - SUCCESS: Both orders placed: XAUUSD SELL
[2025-12-19 01:26:56] [DUAL_ORDER_CHAIN] ✅ Assigned chain_id dc4fd453-c04... to BOTH orders for SL Hunt
2025-12-19 01:26:56 - src.services.price_monitor_service - INFO - 📝 [SL_HUNT_REGISTRATION] Trade 493984941: Symbol=XAUUSD Direction=sell SL=4333.21000 Offset=1.0pips Target=4333.20000 Chain=XAUUSD_0e558f1c Logic=LOGIC1
2025-12-19 01:26:56 - src.services.price_monitor_service - INFO - ✅ REGISTERED: SL Hunt monitoring registered: XAUUSD @ 4333.20000 (Total pending: 1)
2025-12-19 01:26:56 - src.services.price_monitor_service - INFO - 📝 [SL_HUNT_REGISTRATION] Trade 493984942: Symbol=XAUUSD Direction=sell SL=4325.21000 Offset=1.0pips Target=4325.20000 Chain=dc4fd453-c04a-446d-894c-b78f8bf515c8 Logic=LOGIC1
2025-12-19 01:26:56 - src.services.price_monitor_service - INFO - ✅ REGISTERED: SL Hunt monitoring registered: XAUUSD @ 4325.20000 (Total pending: 1)
2025-12-19 01:26:56 - src.managers.profit_booking_manager - DEBUG - Chain PROFIT_XAUUSD_f49d62ce synced with MT5: Order 493984942 verified
2025-12-19 01:26:56 - src.managers.profit_booking_manager - INFO - SUCCESS: Profit booking chain created: PROFIT_XAUUSD_f49d62ce for XAUUSD
INFO: Entry alert stored after successful execution for duplicate detection
2025-12-19 01:26:57 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 1, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:26:57 - src.services.price_monitor_service - DEBUG - [SL_HUNT] XAUUSD SELL: Current=4323.27000 Target=4325.20000 SL=4325.21000 Gap=1.93000
2025-12-19 01:26:57 - src.services.price_monitor_service - DEBUG - 🔍 [SL_HUNT_PRICE_CHECK] XAUUSD SELL: Current=4323.27000 Target=4325.20000 SL=4325.21000 Diff=1.93000 Reached=✅ YES
2025-12-19 01:26:57 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BEARISH, 15M=BEARISH, Direction=BEARISH)
2025-12-19 01:26:57 - src.services.price_monitor_service - DEBUG - 🔍 [SL_HUNT_ALIGNMENT] XAUUSD LOGIC1: Aligned=✅ YES, Direction=BEARISH, Details={'1h': 'BEARISH', '15m': 'BEARISH'}, Failure=None
2025-12-19 01:26:57 - src.services.price_monitor_service - INFO - TRIGGERED: SL Hunt Re-Entry Triggered: XAUUSD @ 4323.27
←[32mINFO←[0m:     52.32.178.7:0 - "←[1mPOST /webhook HTTP/1.1←[0m" ←[32m200 OK←[0m
2025-12-19 01:26:59 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:01 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:03 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:05 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:07 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:09 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:11 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:11 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 43200.32% | Free: $9313.98 | Equity: $9335.59 | Used: $21.61
2025-12-19 01:27:12 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 493984942: $-11.60
Auto-reconciliation: Position 493984942 closed by Stop Loss (PnL: $-11.60)
Position 493984942 already closed externally
2025-12-19 01:27:12 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 493984942: $-11.60
Trade Closed: XAUUSD SELL
   Entry: 4323.21000 -> Close: 4325.11500
2025-12-19 01:27:14 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 0 @ 4325.21
2025-12-19 01:27:14 - src.managers.profit_booking_reentry_manager - INFO - 🔄 Profit Chain PROFIT_XAUUSD_f49d62ce Entered Recovery Mode (Attempt 1/1)
2025-12-19 01:27:15 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:15 - src.managers.profit_booking_manager - WARNING - Chain PROFIT_XAUUSD_f49d62ce has missing order: 493984942 (check 1/3)
2025-12-19 01:27:17 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:19 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:19 - src.managers.profit_booking_manager - WARNING - Marking chain PROFIT_XAUUSD_f49d62ce as STALE - all orders missing after 3 checks
2025-12-19 01:27:19 - src.managers.profit_booking_manager - INFO - STOPPED: Chain PROFIT_XAUUSD_f49d62ce stopped: All orders missing - marked stale
2025-12-19 01:27:21 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:23 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:24 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 01:27:24 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-3] Got response: status=200
2025-12-19 01:27:24 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-3] No new updates (updates array empty)
2025-12-19 01:27:24 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 4 starting...
2025-12-19 01:27:24 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 01:27:24 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-4] Making request to Telegram...
2025-12-19 01:27:25 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:27 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:29 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:31 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:33 - src.services.price_monitor_service - DEBUG - 💓 Monitor loop heartbeat - Cycle #50, Running: True, Pending: SL Hunt=0, TP=0, Exit=0
2025-12-19 01:27:33 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:33 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 43220.92% | Free: $9318.43 | Equity: $9340.04 | Used: $21.61
2025-12-19 01:27:35 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:37 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:39 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:41 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:43 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:52388 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 01:27:45 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:47 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:49 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:51 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:53 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:53 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 43198.24% | Free: $9313.53 | Equity: $9335.14 | Used: $21.61
2025-12-19 01:27:54 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 01:27:54 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-4] Got response: status=200
2025-12-19 01:27:54 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-4] No new updates (updates array empty)
2025-12-19 01:27:54 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 5 starting...
2025-12-19 01:27:54 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 01:27:54 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-5] Making request to Telegram...
2025-12-19 01:27:55 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:57 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:27:59 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:01 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:03 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:05 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:07 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:09 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:11 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:13 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:13 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 43202.17% | Free: $9314.38 | Equity: $9335.99 | Used: $21.61
2025-12-19 01:28:15 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:17 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:19 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:21 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:23 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:24 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 01:28:24 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-5] Got response: status=200
2025-12-19 01:28:24 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-5] No new updates (updates array empty)
2025-12-19 01:28:24 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 6 starting...
2025-12-19 01:28:24 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 01:28:24 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-6] Making request to Telegram...
2025-12-19 01:28:25 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:27 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:29 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:32 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:34 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:34 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 43204.95% | Free: $9314.98 | Equity: $9336.59 | Used: $21.61
2025-12-19 01:28:36 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:38 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:40 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:42 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:44 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:62136 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 01:28:46 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:48 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:50 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:52 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:54 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:54 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 43198.24% | Free: $9313.53 | Equity: $9335.14 | Used: $21.61
2025-12-19 01:28:54 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 01:28:54 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-6] Got response: status=200
2025-12-19 01:28:54 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-6] No new updates (updates array empty)
2025-12-19 01:28:54 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 7 starting...
2025-12-19 01:28:54 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 01:28:54 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-7] Making request to Telegram...
2025-12-19 01:28:56 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:28:58 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:00 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:02 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:04 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:06 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:08 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:10 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:12 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:14 - src.services.price_monitor_service - DEBUG - 💓 Monitor loop heartbeat - Cycle #100, Running: True, Pending: SL Hunt=0, TP=0, Exit=0
2025-12-19 01:29:14 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:14 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 43201.48% | Free: $9314.23 | Equity: $9335.84 | Used: $21.61
2025-12-19 01:29:16 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:18 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:20 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:22 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:24 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:25 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 01:29:25 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-7] Got response: status=200
2025-12-19 01:29:25 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-7] No new updates (updates array empty)
2025-12-19 01:29:25 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 8 starting...
2025-12-19 01:29:25 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 01:29:25 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-8] Making request to Telegram...
2025-12-19 01:29:26 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:28 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:30 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:32 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:34 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:34 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 43191.07% | Free: $9311.98 | Equity: $9333.59 | Used: $21.61
2025-12-19 01:29:36 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:38 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:40 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:42 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:44 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:63225 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 01:29:46 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:48 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:50 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:52 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:54 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:54 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 43192.46% | Free: $9312.28 | Equity: $9333.89 | Used: $21.61
2025-12-19 01:29:55 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 01:29:55 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-8] Got response: status=200
2025-12-19 01:29:55 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-8] No new updates (updates array empty)
2025-12-19 01:29:55 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 9 starting...
2025-12-19 01:29:55 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 01:29:55 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-9] Making request to Telegram...
2025-12-19 01:29:56 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:29:58 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:00 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:02 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:04 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:06 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:08 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:10 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:12 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:14 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:14 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 43197.08% | Free: $9313.28 | Equity: $9334.89 | Used: $21.61
2025-12-19 01:30:16 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:18 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:20 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:22 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:24 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:25 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 01:30:25 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-9] Got response: status=200
2025-12-19 01:30:25 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-9] No new updates (updates array empty)
2025-12-19 01:30:25 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 10 starting...
2025-12-19 01:30:25 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 01:30:25 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-10] Making request to Telegram...
2025-12-19 01:30:26 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:28 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:30 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:32 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:34 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:34 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 43158.68% | Free: $9304.98 | Equity: $9326.59 | Used: $21.61
2025-12-19 01:30:36 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:38 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:40 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:42 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:44 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:63234 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 01:30:46 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:48 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:50 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:52 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:52 - src.managers.profit_booking_manager - INFO - Removed stale chain: PROFIT_XAUUSD_f49d62ce
2025-12-19 01:30:52 - src.managers.profit_booking_manager - INFO - Cleaned up 1 stale chain(s)
2025-12-19 01:30:54 - src.services.price_monitor_service - DEBUG - 💓 Monitor loop heartbeat - Cycle #150, Running: True, Pending: SL Hunt=0, TP=0, Exit=0
2025-12-19 01:30:54 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:54 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 43129.52% | Free: $9298.68 | Equity: $9320.29 | Used: $21.61
2025-12-19 01:30:55 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 01:30:55 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-10] Got response: status=200
2025-12-19 01:30:55 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-10] No new updates (updates array empty)
2025-12-19 01:30:55 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 11 starting...
2025-12-19 01:30:55 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 01:30:55 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-11] Making request to Telegram...
2025-12-19 01:30:56 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:30:58 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:00 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:02 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:04 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:06 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:08 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:10 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:12 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:14 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:14 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 43123.28% | Free: $9297.33 | Equity: $9318.94 | Used: $21.61
2025-12-19 01:31:16 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:18 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:20 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:22 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:24 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:26 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 01:31:26 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-11] Got response: status=200
2025-12-19 01:31:26 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-11] No new updates (updates array empty)
2025-12-19 01:31:26 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 12 starting...
2025-12-19 01:31:26 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 01:31:26 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-12] Making request to Telegram...
2025-12-19 01:31:26 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:28 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:30 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:32 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:34 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:34 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 43128.14% | Free: $9298.38 | Equity: $9319.99 | Used: $21.61
2025-12-19 01:31:36 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:38 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:40 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:42 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:44 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:46 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 493984941: $-27.70
Auto-reconciliation: Position 493984941 closed by Stop Loss (PnL: $-27.70)
Position 493984941 already closed externally
2025-12-19 01:31:46 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 493984941: $-27.70
Trade Closed: XAUUSD SELL
   Entry: 4323.21000 -> Close: 4327.94000
2025-12-19 01:31:47 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:62981 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 01:31:49 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:51 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:53 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:55 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:55 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9319.49 | Equity: $9319.49 | Used: $0.00
2025-12-19 01:31:56 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 01:31:56 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-12] Got response: status=200
2025-12-19 01:31:56 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-12] No new updates (updates array empty)
2025-12-19 01:31:56 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 13 starting...
2025-12-19 01:31:56 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 01:31:56 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-13] Making request to Telegram...
2025-12-19 01:31:57 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:31:59 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:32:01 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:32:03 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:32:05 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:32:07 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:32:09 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:32:11 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:32:13 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     Shutting down
←[32mINFO←[0m:     Waiting for application shutdown.
[LIFESPAN] Shutdown signal received - cleaning up...
[SHUTDOWN] Stopping Telegram polling...
2025-12-19 01:32:15 - src.clients.telegram_bot - INFO - [POLLING] Stopping polling thread...
2025-12-19 01:32:20 - src.clients.telegram_bot - INFO - [POLLING] Polling thread stopped
[SHUTDOWN] Cancelling background tasks...
[SHUTDOWN] Cancelling task: <Task pending name='Task-4' coro=<TradingEngine.manage_open_trades() running at C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main\src\core\trading_engine.py:1016> wait_for=<Future pending cb=[Task.task_wakeup()]>>
[2025-12-19 01:32:20] Trade monitor cancelled - graceful shutdown
[SHUTDOWN] Background tasks cancelled. Shutdown complete.
2025-12-19 01:32:20 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 01:32:20 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9319.49 | Equity: $9319.49 | Used: $0.00
←[32mINFO←[0m:     Application shutdown complete.
←[32mINFO←[0m:     Finished server process [←[36m12476←[0m]
2025-12-19 01:32:20 - src.services.price_monitor_service - INFO - Monitor loop cancelled
2025-12-19 01:32:20 - src.services.price_monitor_service - DEBUG - Monitor loop stopped after 190 cycles
PS C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main>