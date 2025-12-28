Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\WINDOWS\system32> cd "c:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main"
PS C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main> python src/main.py --host 0.0.0.0 --port 80
[EVENT-LOOP] Set WindowsProactorEventLoopPolicy on Windows
[LOGGING CONFIG] Loaded saved log level: DEBUG
[LOGGING CONFIG] Loaded trading_debug: True
═══════════════════════════════════════
🚀 BOT STARTING - LOGGING LEVEL: DEBUG
═══════════════════════════════════════
2025-12-19 02:05:48 - __main__ - INFO - Bot starting with logging level: DEBUG
[LOGGING CONFIG] Loaded saved log level: DEBUG
[LOGGING CONFIG] Loaded trading_debug: True
Config loaded - MT5 Login: 308646228, Server: XMGlobal-MT5 6
[INIT] Cleaning up webhooks on bot initialization...
2025-12-19 02:05:48 - src.clients.telegram_bot - INFO - [POLLING-INIT] Cleaning up any existing webhooks...
2025-12-19 02:05:49 - src.clients.telegram_bot - INFO - [POLLING-INIT] No webhook found on Telegram servers
2025-12-19 02:05:50 - src.clients.telegram_bot - INFO - [POLLING-INIT] Webhook deleted successfully
2025-12-19 02:05:50 - src.clients.telegram_bot - DEBUG - [POLLING-INIT] Waiting 3 seconds for webhook deletion to propagate...
2025-12-19 02:05:54 - src.clients.telegram_bot - INFO - [POLLING-INIT] ✅ Webhook cleanup verified - ready for polling
[INIT] Webhook cleanup complete
2025-12-19 02:05:54 - src.managers.session_manager - INFO - ✅ Recovered active session: SES_20251213_172949_08c3a6
DEBUG: TimeframeTrendManager using config file: C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main\config\timeframe_trends.json
SUCCESS: Loaded trends from C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main\config\timeframe_trends.json
DEBUG: Loaded MANUAL trend for AUDUSD 1h: BULLISH
DEBUG: Total manual trends loaded: 1
2025-12-19 02:05:54 - src.managers.recovery_window_monitor - INFO - ✅ RecoveryWindowMonitor initialized
2025-12-19 02:05:54 - src.managers.profit_protection_manager - INFO -
Profit Protection Settings Loaded:
├─ Enabled: True
├─ Mode: ⚖️ BALANCED
├─ Multiplier: 6.0x
├─ Min Threshold: $20.0
├─ Order A: ON ✅
└─ Order B: ON ✅

2025-12-19 02:05:54 - src.managers.profit_protection_manager - INFO - ✅ ProfitProtectionManager initialized
2025-12-19 02:05:54 - src.managers.sl_reduction_optimizer - INFO -
SL Reduction Settings Loaded:
├─ Enabled: True
├─ Strategy: ⚖️ BALANCED
├─ Reduction: 30%
└─ Description: Recommended for most conditions

2025-12-19 02:05:54 - src.managers.sl_reduction_optimizer - INFO - ✅ SLReductionOptimizer initialized
✅ Fine-Tune managers initialized (Recovery Monitor, Profit Protection, SL Optimizer)
✅ Autonomous System Manager initialized
2025-12-19 02:05:54 - src.menu.fine_tune_menu_handler - INFO - ✅ FineTuneMenuHandler initialized (Compatible Mode)
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
2025-12-19 02:05:54 - asyncio - DEBUG - Using proactor: IocpProactor
←[32mINFO←[0m:     Started server process [←[36m5376←[0m]
←[32mINFO←[0m:     Waiting for application startup.
======================================================================
STARTING ZEPIX TRADING BOT v2.0
======================================================================
Initializing components...
2025-12-19 02:05:54 - src.menu.fine_tune_menu_handler - INFO - ✅ FineTuneMenuHandler initialized (Compatible Mode)
✅ TelegramBot: Fine-Tune Menu Handler initialized
✅ TelegramBot: Re-entry Menu Handler initialized
✅ TelegramBot: Profit Booking Menu Handler initialized
SUCCESS: MT5 connection established
Account Balance: $9319.49
Account: 308646228 | Server: XMGlobal-MT5 6
2025-12-19 02:05:55 - src.clients.telegram_bot - INFO - SUCCESS: Trend manager set in Telegram bot
2025-12-19 02:05:55 - src.core.trading_engine - INFO - 📋 [RE-ENTRY_CONFIG] Startup Configuration:
  SL Hunt Enabled: True
  TP Re-entry Enabled: True
  Exit Continuation Enabled: True
  Monitor Interval: 2s
  SL Hunt Offset: 1.0 pips
  TP Continuation Gap: 2.0 pips
  Max Chain Levels: 5
  SL Reduction Per Level: 0.3
2025-12-19 02:05:55 - src.services.price_monitor_service - INFO - ✅ Price Monitor Service started successfully - Task created: <Task pending name='Task-3' coro=<PriceMonitorService._monitor_loop() running at C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main\src\services\price_monitor_service.py:129>>, is_running: True
2025-12-19 02:05:55 - src.core.trading_engine - INFO - ✅ Price Monitor Service confirmed running after initialization
2025-12-19 02:05:55 - src.managers.profit_booking_manager - INFO - SUCCESS: Recovered 0 profit booking chains from database
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
2025-12-19 02:05:57 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] poll_commands() started, stop_event=False
2025-12-19 02:05:57 - src.clients.telegram_bot - INFO - SUCCESS: Telegram bot polling started
[POLLING-THREAD] Polling thread exited
2025-12-19 02:05:57 - src.services.price_monitor_service - DEBUG - 🔄 Monitor loop started - Interval: 2s, Config: SL Hunt=True, TP=True, Exit=True
2025-12-19 02:05:57 - src.clients.telegram_bot - INFO - [POLLING] Starting polling loop...
2025-12-19 02:05:57 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:05:57 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 1 starting...
←[32mINFO←[0m:     Application startup complete.
2025-12-19 02:05:57 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:05:57 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-1] Making request to Telegram...
←[32mINFO←[0m:     Uvicorn running on ←[1mhttp://0.0.0.0:80←[0m (Press CTRL+C to quit)
2025-12-19 02:05:59 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:01 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:03 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:05 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:07 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:09 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:60973 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:06:11 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:13 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:15 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:15 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9319.49 | Equity: $9319.49 | Used: $0.00
2025-12-19 02:06:17 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:19 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:21 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:23 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:25 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:27 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:28 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:06:28 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-1] Got response: status=200
2025-12-19 02:06:28 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-1] No new updates (updates array empty)
2025-12-19 02:06:28 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 2 starting...
2025-12-19 02:06:28 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:06:28 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-2] Making request to Telegram...
2025-12-19 02:06:29 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:31 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:33 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:35 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:35 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9319.49 | Equity: $9319.49 | Used: $0.00
2025-12-19 02:06:37 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:39 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:41 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:43 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:45 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:47 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:49 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:51 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:53 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:55 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:55 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9319.49 | Equity: $9319.49 | Used: $0.00
2025-12-19 02:06:57 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:06:58 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:06:58 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-2] Got response: status=200
2025-12-19 02:06:58 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-2] No new updates (updates array empty)
2025-12-19 02:06:58 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 3 starting...
2025-12-19 02:06:58 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:06:58 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-3] Making request to Telegram...
2025-12-19 02:06:59 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:01 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:03 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:05 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:07 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:09 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:62152 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:07:11 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:13 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:15 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:15 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9319.49 | Equity: $9319.49 | Used: $0.00
2025-12-19 02:07:17 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:19 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:21 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:23 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:25 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:27 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:28 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:07:28 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-3] Got response: status=200
2025-12-19 02:07:28 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-3] No new updates (updates array empty)
2025-12-19 02:07:28 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 4 starting...
2025-12-19 02:07:28 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:07:28 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-4] Making request to Telegram...
2025-12-19 02:07:29 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:31 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:33 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:35 - src.services.price_monitor_service - DEBUG - 💓 Monitor loop heartbeat - Cycle #50, Running: True, Pending: SL Hunt=0, TP=0, Exit=0
2025-12-19 02:07:35 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:35 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9319.49 | Equity: $9319.49 | Used: $0.00
2025-12-19 02:07:37 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:39 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:41 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:43 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:45 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:47 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:49 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:51 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:53 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:55 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:55 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9319.49 | Equity: $9319.49 | Used: $0.00
2025-12-19 02:07:57 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:07:58 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:07:58 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-4] Got response: status=200
2025-12-19 02:07:58 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-4] No new updates (updates array empty)
2025-12-19 02:07:58 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 5 starting...
2025-12-19 02:07:58 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:07:58 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-5] Making request to Telegram...
2025-12-19 02:07:59 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:01 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
Webhook received: {
  "type": "trend",
  "symbol": "XAUUSD",
  "signal": "bull",
  "tf": "1h",
  "price": 4337.075,
  "strategy": "ZepixPremium"
}
ALERT: Received alert: {'type': 'trend', 'symbol': 'XAUUSD', 'signal': 'bull', 'tf': '1h', 'price': 4337.075, 'strategy': 'ZepixPremium'}
INFO: Stored trend alert for duplicate detection
SUCCESS: Alert validation successful
SUCCESS: Trend updated: XAUUSD 1h -> BULLISH (AUTO)
2025-12-19 02:08:03 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     52.32.178.7:0 - "←[1mPOST /webhook HTTP/1.1←[0m" ←[32m200 OK←[0m
2025-12-19 02:08:05 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:07 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:09 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:50867 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:08:11 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:13 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:15 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:15 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9319.49 | Equity: $9319.49 | Used: $0.00
2025-12-19 02:08:17 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:19 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
Webhook received: {
  "type": "trend",
  "symbol": "XAUUSD",
  "signal": "bull",
  "tf": "15m",
  "price": 4336.45,
  "strategy": "ZepixPremium"
}
ALERT: Received alert: {'type': 'trend', 'symbol': 'XAUUSD', 'signal': 'bull', 'tf': '15m', 'price': 4336.45, 'strategy': 'ZepixPremium'}
INFO: Stored trend alert for duplicate detection
SUCCESS: Alert validation successful
SUCCESS: Trend updated: XAUUSD 15m -> BULLISH (AUTO)
2025-12-19 02:08:23 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     34.212.75.30:0 - "←[1mPOST /webhook HTTP/1.1←[0m" ←[32m200 OK←[0m
2025-12-19 02:08:25 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:27 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:29 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:08:29 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-5] Got response: status=200
2025-12-19 02:08:29 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-5] No new updates (updates array empty)
2025-12-19 02:08:29 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 6 starting...
2025-12-19 02:08:29 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:08:29 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-6] Making request to Telegram...
2025-12-19 02:08:29 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:31 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
Webhook received: {
  "type": "entry",
  "symbol": "XAUUSD",
  "signal": "buy",
  "tf": "5m",
  "price": 4335.495,
  "strategy": "ZepixPremium"
}
ALERT: Received alert: {'type': 'entry', 'symbol': 'XAUUSD', 'signal': 'buy', 'tf': '5m', 'price': 4335.495, 'strategy': 'ZepixPremium'}
INFO: Entry alert validated but NOT stored (will store after execution)
SUCCESS: Alert validation successful
2025-12-19 02:08:32 - src.managers.session_manager - WARNING - Session already active: SES_20251213_172949_08c3a6
[2025-12-19 02:08:32] 🔔 Processing entry alert | Symbol: XAUUSD, TF: 5m
[2025-12-19 02:08:32] 🔍 TRADING_DEBUG: Alert=buy, TF=5m, Symbol=XAUUSD
[2025-12-19 02:08:32] 🔍 TRADING_DEBUG: Alignment={'aligned': False, 'direction': 'PENDING'}
[2025-12-19 02:08:32] 🔍 TRADING_DEBUG: SignalDir=PENDING, Logic=LOGIC1
2025-12-19 02:08:32 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
[2025-12-19 02:08:32] 🔍 TRADING_DEBUG: Alert=buy, TF=5m, Symbol=XAUUSD
[2025-12-19 02:08:32] 🔍 TRADING_DEBUG: Alignment={'aligned': True, 'direction': 'BULLISH', 'details': {'1h': 'BULLISH', '15m': 'BULLISH'}, 'failure_reason': None}
[2025-12-19 02:08:32] 🔍 TRADING_DEBUG: SignalDir=PENDING, Logic=LOGIC1
[2025-12-19 02:08:32] 🔍 TRADING_DEBUG: Alert=buy, TF=5m, Symbol=XAUUSD
[2025-12-19 02:08:32] 🔍 TRADING_DEBUG: Alignment={'aligned': True, 'direction': 'BULLISH', 'details': {'1h': 'BULLISH', '15m': 'BULLISH'}, 'failure_reason': None}
[2025-12-19 02:08:32] 🔍 TRADING_DEBUG: SignalDir=BULLISH, Logic=LOGIC1
[2025-12-19 02:08:32] 🔔 Trade execution starting | Symbol: XAUUSD, Direction: BULLISH
2025-12-19 02:08:32 - src.managers.dual_order_manager - DEBUG - [DUAL_ORDER_LOT_SIZE] Symbol=XAUUSD Balance=$9319.49 Requested Lot=0.06
2025-12-19 02:08:32 - src.managers.dual_order_manager - WARNING - 🔧 SMART ADJUSTMENT: Lot reduced 0.062 -> 0.05 to fit daily limit (Risk: $124.00 -> $100.00)
2025-12-19 02:08:32 - src.managers.dual_order_manager - INFO - 🔧 SMART ADJUSTMENT: Lot reduced 0.06 -> 0.05 to fit daily limit.
2025-12-19 02:08:32 - src.managers.dual_order_manager - DEBUG - [DUAL_ORDER_RISK] Symbol=XAUUSD Valid=True Reason=Auto-adjusted lot to 0.05 to fit daily limit
2025-12-19 02:08:32 - src.clients.mt5_client - DEBUG - Symbol mapping: XAUUSD -> GOLD
2025-12-19 02:08:32 - src.clients.mt5_client - INFO - VALIDATION DEBUG: Symbol=XAUUSD, OrderType=buy, Price=4335.81, SL=4325.49, TP=4350.49
2025-12-19 02:08:32 - src.clients.mt5_client - INFO - VALIDATION: Symbol mapped XAUUSD -> GOLD
2025-12-19 02:08:32 - src.clients.mt5_client - INFO - VALIDATION: Symbol info retrieved for GOLD - Visible=True, Digits=2
2025-12-19 02:08:32 - src.clients.mt5_client - INFO - VALIDATION: StopsLevel=0, Point=0.01, MinDistance=0.10000
2025-12-19 02:08:32 - src.clients.mt5_client - INFO - VALIDATION: BUY order SL distance=10.32000, MinRequired=0.10000
2025-12-19 02:08:32 - src.clients.mt5_client - INFO - VALIDATION: BUY order TP distance=14.68000, MinRequired=0.10000
2025-12-19 02:08:32 - src.clients.mt5_client - INFO - VALIDATION PASSED: All checks passed for XAUUSD (GOLD)
SUCCESS: Order placed successfully: Ticket #494006570
2025-12-19 02:08:32 - src.clients.mt5_client - INFO - VALIDATION DEBUG: Symbol=XAUUSD, OrderType=buy, Price=4335.74, SL=4333.49, TP=4338.49
2025-12-19 02:08:32 - src.clients.mt5_client - INFO - VALIDATION: Symbol mapped XAUUSD -> GOLD
2025-12-19 02:08:32 - src.clients.mt5_client - INFO - VALIDATION: Symbol info retrieved for GOLD - Visible=True, Digits=2
2025-12-19 02:08:32 - src.clients.mt5_client - INFO - VALIDATION: StopsLevel=0, Point=0.01, MinDistance=0.10000
2025-12-19 02:08:32 - src.clients.mt5_client - INFO - VALIDATION: BUY order SL distance=2.25000, MinRequired=0.10000
2025-12-19 02:08:32 - src.clients.mt5_client - INFO - VALIDATION: BUY order TP distance=2.75000, MinRequired=0.10000
2025-12-19 02:08:32 - src.clients.mt5_client - INFO - VALIDATION PASSED: All checks passed for XAUUSD (GOLD)
SUCCESS: Order placed successfully: Ticket #494006573
2025-12-19 02:08:32 - src.managers.dual_order_manager - INFO - SUCCESS: Both orders placed: XAUUSD BUY
[2025-12-19 02:08:32] [DUAL_ORDER_CHAIN] ✅ Created shared reentry chain XAUUSD_4c28161b for BOTH orders
2025-12-19 02:08:32 - src.services.price_monitor_service - INFO - 📝 [SL_HUNT_REGISTRATION] Trade 494006570: Symbol=XAUUSD Direction=buy SL=4325.49500 Offset=1.0pips Target=4325.50500 Chain=XAUUSD_4c28161b Logic=LOGIC1
2025-12-19 02:08:32 - src.services.price_monitor_service - INFO - ✅ REGISTERED: SL Hunt monitoring registered: XAUUSD @ 4325.50500 (Total pending: 1)
[2025-12-19 02:08:32] [DUAL_ORDER_CHAIN] ✅ Order B #494006573 added to shared chain XAUUSD_4c28161b
2025-12-19 02:08:32 - src.services.price_monitor_service - INFO - 📝 [SL_HUNT_REGISTRATION] Trade 494006573: Symbol=XAUUSD Direction=buy SL=4333.49500 Offset=1.0pips Target=4333.50500 Chain=XAUUSD_4c28161b Logic=LOGIC1
2025-12-19 02:08:32 - src.services.price_monitor_service - INFO - ✅ REGISTERED: SL Hunt monitoring registered: XAUUSD @ 4333.50500 (Total pending: 1)
2025-12-19 02:08:32 - src.managers.profit_booking_manager - DEBUG - Chain PROFIT_XAUUSD_1a7bfc2e synced with MT5: Order 494006573 verified
2025-12-19 02:08:32 - src.managers.profit_booking_manager - INFO - SUCCESS: Profit booking chain created: PROFIT_XAUUSD_1a7bfc2e for XAUUSD
WARNING: Parse mode 'HTML' error, retrying without formatting...
INFO: Entry alert stored after successful execution for duplicate detection
2025-12-19 02:08:35 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 1, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:35 - src.services.price_monitor_service - DEBUG - [SL_HUNT] XAUUSD BUY: Current=4335.52500 Target=4333.50500 SL=4333.49500 Gap=2.02000
2025-12-19 02:08:35 - src.services.price_monitor_service - DEBUG - 🔍 [SL_HUNT_PRICE_CHECK] XAUUSD BUY: Current=4335.52500 Target=4333.50500 SL=4333.49500 Diff=2.02000 Reached=✅ YES
2025-12-19 02:08:35 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:08:35 - src.services.price_monitor_service - DEBUG - 🔍 [SL_HUNT_ALIGNMENT] XAUUSD LOGIC1: Aligned=✅ YES, Direction=BULLISH, Details={'1h': 'BULLISH', '15m': 'BULLISH'}, Failure=None
2025-12-19 02:08:35 - src.services.price_monitor_service - INFO - TRIGGERED: SL Hunt Re-Entry Triggered: XAUUSD @ 4335.525
2025-12-19 02:08:35 - src.services.price_monitor_service - INFO - ✅ [SL_HUNT_RECOVERY_START] XAUUSD: Chain valid, executing re-entry...
2025-12-19 02:08:35 - src.clients.mt5_client - INFO - VALIDATION DEBUG: Symbol=XAUUSD, OrderType=buy, Price=4335.76, SL=4328.52, TP=4346.02
2025-12-19 02:08:35 - src.clients.mt5_client - INFO - VALIDATION: Symbol mapped XAUUSD -> GOLD
2025-12-19 02:08:35 - src.clients.mt5_client - INFO - VALIDATION: Symbol info retrieved for GOLD - Visible=True, Digits=2
2025-12-19 02:08:35 - src.clients.mt5_client - INFO - VALIDATION: StopsLevel=0, Point=0.01, MinDistance=0.10000
2025-12-19 02:08:35 - src.clients.mt5_client - INFO - VALIDATION: BUY order SL distance=7.24000, MinRequired=0.10000
2025-12-19 02:08:35 - src.clients.mt5_client - INFO - VALIDATION: BUY order TP distance=10.26000, MinRequired=0.10000
2025-12-19 02:08:35 - src.clients.mt5_client - INFO - VALIDATION PASSED: All checks passed for XAUUSD (GOLD)
ERROR: Order failed: Invalid volume (Error code: 10014)
Request details: Symbol=GOLD, Lot=0.062, Price=4335.76, SL=4328.52, TP=4346.02
2025-12-19 02:08:35 - src.services.price_monitor_service - ERROR - ❌ [SL_HUNT_ORDER_FAILED] XAUUSD: MT5 order placement returned None
2025-12-19 02:08:38 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:40 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:40 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 21481.07% | Free: $9270.83 | Equity: $9314.19 | Used: $43.36
2025-12-19 02:08:42 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:44 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:46 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:48 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:51 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:53 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:55 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:57 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:59 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:08:59 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:08:59 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-6] Got response: status=200
2025-12-19 02:08:59 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-6] No new updates (updates array empty)
2025-12-19 02:08:59 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 7 starting...
2025-12-19 02:08:59 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:08:59 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-7] Making request to Telegram...
2025-12-19 02:09:01 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:01 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 21491.44% | Free: $9275.33 | Equity: $9318.69 | Used: $43.36
2025-12-19 02:09:03 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:05 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:07 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:09 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:49675 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:09:11 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:13 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:15 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:17 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:19 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:21 - src.services.price_monitor_service - DEBUG - 💓 Monitor loop heartbeat - Cycle #100, Running: True, Pending: SL Hunt=0, TP=0, Exit=0
2025-12-19 02:09:21 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:21 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 21492.83% | Free: $9275.93 | Equity: $9319.29 | Used: $43.36
2025-12-19 02:09:23 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:25 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:27 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:29 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:29 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:09:29 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-7] Got response: status=200
2025-12-19 02:09:29 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-7] No new updates (updates array empty)
2025-12-19 02:09:29 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 8 starting...
2025-12-19 02:09:29 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:09:29 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-8] Making request to Telegram...
2025-12-19 02:09:31 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:33 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:35 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:37 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:39 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:41 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:41 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 21479.68% | Free: $9270.23 | Equity: $9313.59 | Used: $43.36
2025-12-19 02:09:43 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:45 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:47 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:49 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:51 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:53 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:55 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:57 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:59 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:09:59 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:09:59 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-8] Got response: status=200
2025-12-19 02:09:59 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-8] No new updates (updates array empty)
2025-12-19 02:09:59 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 9 starting...
2025-12-19 02:09:59 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:09:59 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-9] Making request to Telegram...
2025-12-19 02:10:01 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:01 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 21493.75% | Free: $9276.33 | Equity: $9319.69 | Used: $43.36
2025-12-19 02:10:03 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:05 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:07 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:09 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:11 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:49700 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:10:13 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:15 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:17 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:19 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:21 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:21 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 21484.99% | Free: $9272.53 | Equity: $9315.89 | Used: $43.36
2025-12-19 02:10:23 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:25 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:27 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:29 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:30 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:10:30 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-9] Got response: status=200
2025-12-19 02:10:30 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-9] No new updates (updates array empty)
2025-12-19 02:10:30 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 10 starting...
2025-12-19 02:10:30 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:10:30 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-10] Making request to Telegram...
2025-12-19 02:10:31 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:33 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:35 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:37 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:39 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:41 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:41 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 21514.74% | Free: $9285.43 | Equity: $9328.79 | Used: $43.36
2025-12-19 02:10:43 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:43 - src.managers.profit_booking_manager - DEBUG - [PROFIT_BOOKING] Order 494006573 should be booked: PnL=$8.05 >= $7.00
2025-12-19 02:10:43 - src.managers.profit_booking_manager - INFO - ✅ Order 494006573 ready to book: Chain PROFIT_XAUUSD_1a7bfc2e Level 0 - PnL=$8.05 >= $7.00
SUCCESS: Position 494006573 closed successfully
Position 494006573 closed successfully
2025-12-19 02:10:43 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494006573: $5.60
Trade Closed: XAUUSD BUY
   Entry: 4335.49500 -> Close: 4337.10500
2025-12-19 02:10:44 - src.managers.profit_booking_manager - INFO - ✅ Individual order booked: Trade 494006573 Chain PROFIT_XAUUSD_1a7bfc2e Level 0 Profit: $8.05
2025-12-19 02:10:44 - src.services.price_monitor_service - INFO - ✅ Order 494006573 booked: Chain PROFIT_XAUUSD_1a7bfc2e Level 0
2025-12-19 02:10:44 - src.managers.profit_booking_manager - INFO - ✅ All orders closed in Level 0, progressing to Level 1
2025-12-19 02:10:44 - src.clients.mt5_client - INFO - VALIDATION DEBUG: Symbol=XAUUSD, OrderType=buy, Price=4337.27, SL=4335.07, TP=4340.07
2025-12-19 02:10:44 - src.clients.mt5_client - INFO - VALIDATION: Symbol mapped XAUUSD -> GOLD
2025-12-19 02:10:44 - src.clients.mt5_client - INFO - VALIDATION: Symbol info retrieved for GOLD - Visible=True, Digits=2
2025-12-19 02:10:44 - src.clients.mt5_client - INFO - VALIDATION: StopsLevel=0, Point=0.01, MinDistance=0.10000
2025-12-19 02:10:44 - src.clients.mt5_client - INFO - VALIDATION: BUY order SL distance=2.20000, MinRequired=0.10000
2025-12-19 02:10:44 - src.clients.mt5_client - INFO - VALIDATION: BUY order TP distance=2.80000, MinRequired=0.10000
2025-12-19 02:10:44 - src.clients.mt5_client - INFO - VALIDATION PASSED: All checks passed for XAUUSD (GOLD)
SUCCESS: Order placed successfully: Ticket #494007108
2025-12-19 02:10:45 - src.clients.mt5_client - INFO - VALIDATION DEBUG: Symbol=XAUUSD, OrderType=buy, Price=4337.26, SL=4335.07, TP=4340.07
2025-12-19 02:10:45 - src.clients.mt5_client - INFO - VALIDATION: Symbol mapped XAUUSD -> GOLD
2025-12-19 02:10:45 - src.clients.mt5_client - INFO - VALIDATION: Symbol info retrieved for GOLD - Visible=True, Digits=2
2025-12-19 02:10:45 - src.clients.mt5_client - INFO - VALIDATION: StopsLevel=0, Point=0.01, MinDistance=0.10000
2025-12-19 02:10:45 - src.clients.mt5_client - INFO - VALIDATION: BUY order SL distance=2.19000, MinRequired=0.10000
2025-12-19 02:10:45 - src.clients.mt5_client - INFO - VALIDATION: BUY order TP distance=2.81000, MinRequired=0.10000
2025-12-19 02:10:45 - src.clients.mt5_client - INFO - VALIDATION PASSED: All checks passed for XAUUSD (GOLD)
SUCCESS: Order placed successfully: Ticket #494007110
2025-12-19 02:10:46 - src.managers.profit_booking_manager - INFO - ✅ Chain progressed: PROFIT_XAUUSD_1a7bfc2e Level 0 → 1, Orders placed: 2
2025-12-19 02:10:46 - src.services.price_monitor_service - WARNING - ⚠️ Monitor cycle took 3.39s (longer than interval 2s)
2025-12-19 02:10:48 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:50 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:52 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:54 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:56 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:10:58 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:00 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:11:00 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-10] Got response: status=200
2025-12-19 02:11:00 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-10] No new updates (updates array empty)
2025-12-19 02:11:00 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 11 starting...
2025-12-19 02:11:00 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:11:00 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-11] Making request to Telegram...
2025-12-19 02:11:00 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:02 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:04 - src.services.price_monitor_service - DEBUG - 💓 Monitor loop heartbeat - Cycle #150, Running: True, Pending: SL Hunt=0, TP=0, Exit=0
2025-12-19 02:11:04 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:04 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14333.04% | Free: $9258.59 | Equity: $9323.64 | Used: $65.05
2025-12-19 02:11:06 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:08 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:10 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:50489 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:11:12 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:14 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:16 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:18 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:20 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:22 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:24 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:24 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14336.73% | Free: $9260.99 | Equity: $9326.04 | Used: $65.05
2025-12-19 02:11:26 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:28 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:30 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:11:30 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-11] Got response: status=200
2025-12-19 02:11:30 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-11] No new updates (updates array empty)
2025-12-19 02:11:30 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 12 starting...
2025-12-19 02:11:30 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:11:30 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-12] Making request to Telegram...
2025-12-19 02:11:30 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:32 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:34 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:36 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:38 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:40 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:42 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:44 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:44 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14356.56% | Free: $9273.89 | Equity: $9338.94 | Used: $65.05
2025-12-19 02:11:46 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:48 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:50 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:52 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:54 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:56 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:11:58 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:00 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:12:00 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-12] Got response: status=200
2025-12-19 02:12:00 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-12] No new updates (updates array empty)
2025-12-19 02:12:00 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 13 starting...
2025-12-19 02:12:00 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:12:00 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-13] Making request to Telegram...
2025-12-19 02:12:00 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:02 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:04 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:04 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14348.02% | Free: $9268.34 | Equity: $9333.39 | Used: $65.05
2025-12-19 02:12:06 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:08 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:10 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:50497 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:12:12 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:14 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:16 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:18 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:20 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:22 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:24 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:24 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14359.09% | Free: $9275.54 | Equity: $9340.59 | Used: $65.05
2025-12-19 02:12:26 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:28 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:30 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:12:30 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-13] Got response: status=200
2025-12-19 02:12:30 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-13] No new updates (updates array empty)
2025-12-19 02:12:30 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 14 starting...
2025-12-19 02:12:30 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:12:30 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-14] Making request to Telegram...
2025-12-19 02:12:30 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:32 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:34 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:36 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:38 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:41 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:43 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:45 - src.services.price_monitor_service - DEBUG - 💓 Monitor loop heartbeat - Cycle #200, Running: True, Pending: SL Hunt=0, TP=0, Exit=0
2025-12-19 02:12:45 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:45 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14359.09% | Free: $9275.54 | Equity: $9340.59 | Used: $65.05
2025-12-19 02:12:47 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:49 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:51 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:53 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:55 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:57 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:12:59 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:01 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:01 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:13:01 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-14] Got response: status=200
2025-12-19 02:13:01 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-14] No new updates (updates array empty)
2025-12-19 02:13:01 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 15 starting...
2025-12-19 02:13:01 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:13:01 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-15] Making request to Telegram...
2025-12-19 02:13:03 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:05 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:05 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14336.26% | Free: $9260.69 | Equity: $9325.74 | Used: $65.05
2025-12-19 02:13:07 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:09 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:11 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:13 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:50506 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:13:15 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:17 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:19 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:21 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:23 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:25 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:25 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14330.73% | Free: $9257.09 | Equity: $9322.14 | Used: $65.05
2025-12-19 02:13:27 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:29 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:31 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:31 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:13:31 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-15] Got response: status=200
2025-12-19 02:13:31 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-15] No new updates (updates array empty)
2025-12-19 02:13:31 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 16 starting...
2025-12-19 02:13:31 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:13:31 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-16] Making request to Telegram...
2025-12-19 02:13:33 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:35 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:36 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:13:36 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:13:37 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:39 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:41 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:41 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:13:41 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:13:43 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:45 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:45 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14337.19% | Free: $9261.29 | Equity: $9326.34 | Used: $65.05
2025-12-19 02:13:46 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:13:46 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:13:47 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:49 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:51 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:51 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:13:51 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:13:53 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:55 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:56 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:13:56 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:13:57 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:13:59 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:01 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:01 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:14:01 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-16] Got response: status=200
2025-12-19 02:14:01 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-16] No new updates (updates array empty)
2025-12-19 02:14:01 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 17 starting...
2025-12-19 02:14:01 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:14:01 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-17] Making request to Telegram...
2025-12-19 02:14:01 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:14:01 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:14:03 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:05 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:05 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14335.34% | Free: $9260.09 | Equity: $9325.14 | Used: $65.05
2025-12-19 02:14:06 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:14:06 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:14:07 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:09 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:11 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:11 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:14:11 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:14:13 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:59254 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:14:15 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:16 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:14:16 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:14:17 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:19 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:21 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:21 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:14:21 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:14:23 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:25 - src.services.price_monitor_service - DEBUG - 💓 Monitor loop heartbeat - Cycle #250, Running: True, Pending: SL Hunt=0, TP=0, Exit=0
2025-12-19 02:14:25 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:25 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14324.50% | Free: $9253.04 | Equity: $9318.09 | Used: $65.05
2025-12-19 02:14:26 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:14:26 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:14:27 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:29 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:31 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:31 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:14:31 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-17] Got response: status=200
2025-12-19 02:14:31 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-17] No new updates (updates array empty)
2025-12-19 02:14:32 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 18 starting...
2025-12-19 02:14:32 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:14:32 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-18] Making request to Telegram...
2025-12-19 02:14:32 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:14:32 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:14:33 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:35 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:37 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:14:37 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:14:37 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:39 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:41 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:42 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:14:42 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:14:43 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:45 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:45 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14311.59% | Free: $9244.64 | Equity: $9309.69 | Used: $65.05
2025-12-19 02:14:47 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:14:47 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:14:47 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:49 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:51 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:52 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:14:52 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:14:53 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:55 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:57 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:14:57 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:14:57 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:14:59 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:01 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:02 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:02 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:02 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:15:02 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-18] Got response: status=200
2025-12-19 02:15:02 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-18] No new updates (updates array empty)
2025-12-19 02:15:02 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 19 starting...
2025-12-19 02:15:02 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:15:02 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-19] Making request to Telegram...
2025-12-19 02:15:03 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:05 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:05 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14317.36% | Free: $9248.39 | Equity: $9313.44 | Used: $65.05
2025-12-19 02:15:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:07 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:09 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:11 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:12 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:12 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:13 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:59262 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:15:15 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:17 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:17 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:17 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:19 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:21 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:22 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:22 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:23 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:25 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:25 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14315.51% | Free: $9247.19 | Equity: $9312.24 | Used: $65.05
2025-12-19 02:15:27 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:27 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:27 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:29 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:31 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:32 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:32 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:32 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:15:32 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-19] Got response: status=200
2025-12-19 02:15:32 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-19] No new updates (updates array empty)
2025-12-19 02:15:32 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 20 starting...
2025-12-19 02:15:32 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:15:32 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-20] Making request to Telegram...
2025-12-19 02:15:33 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:35 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:37 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:37 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:37 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:39 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:41 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:42 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:42 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:43 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:45 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:45 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14299.14% | Free: $9236.54 | Equity: $9301.59 | Used: $65.05
2025-12-19 02:15:47 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:47 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:47 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:47 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:47 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:47 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:47 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:49 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:51 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:52 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:52 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:52 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:52 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:52 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:52 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:53 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:55 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:57 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:57 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:57 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:57 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:57 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:15:57 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:15:57 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:15:59 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:01 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:02 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:02 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:02 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:02 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:02 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:02 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:02 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:16:02 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-20] Got response: status=200
2025-12-19 02:16:02 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-20] No new updates (updates array empty)
2025-12-19 02:16:02 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 21 starting...
2025-12-19 02:16:02 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:16:02 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-21] Making request to Telegram...
2025-12-19 02:16:03 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:05 - src.services.price_monitor_service - DEBUG - 💓 Monitor loop heartbeat - Cycle #300, Running: True, Pending: SL Hunt=0, TP=0, Exit=0
2025-12-19 02:16:05 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:05 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14307.44% | Free: $9241.94 | Equity: $9306.99 | Used: $65.05
2025-12-19 02:16:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:07 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:09 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:11 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:12 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:12 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:12 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:12 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:12 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:12 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:13 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:64927 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:16:15 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:17 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:17 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:17 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:17 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:17 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:17 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:17 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:19 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:21 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:22 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:22 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:22 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:22 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:22 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:22 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:23 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:25 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:25 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14308.59% | Free: $9242.69 | Equity: $9307.74 | Used: $65.05
2025-12-19 02:16:27 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:27 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:27 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:27 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:27 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:27 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:27 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:29 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:31 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:32 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:32 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:32 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:32 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:32 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:32 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:33 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:16:33 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-21] Got response: status=200
2025-12-19 02:16:33 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-21] No new updates (updates array empty)
2025-12-19 02:16:33 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 22 starting...
2025-12-19 02:16:33 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:16:33 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-22] Making request to Telegram...
2025-12-19 02:16:33 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:35 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:37 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:37 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:37 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:37 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:37 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:37 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:37 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:39 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:41 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:42 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:42 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:42 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:42 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:42 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:42 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:43 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:45 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:45 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14316.20% | Free: $9247.64 | Equity: $9312.69 | Used: $65.05
2025-12-19 02:16:47 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:47 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:47 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:47 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:47 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:47 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:48 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:50 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:52 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:52 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:52 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:52 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:52 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:52 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:52 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:54 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:56 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:16:57 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:57 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:57 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:57 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:57 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:16:57 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:16:58 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:00 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:02 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:02 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:02 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:02 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:02 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:02 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:02 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:03 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:17:03 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-22] Got response: status=200
2025-12-19 02:17:03 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-22] No new updates (updates array empty)
2025-12-19 02:17:03 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 23 starting...
2025-12-19 02:17:03 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:17:03 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-23] Making request to Telegram...
2025-12-19 02:17:04 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:06 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:06 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14315.05% | Free: $9246.89 | Equity: $9311.94 | Used: $65.05
2025-12-19 02:17:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:08 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:10 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:12 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:12 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:12 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:12 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:12 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:12 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:12 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:14 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:16 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:64936 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:17:17 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:17 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:17 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:17 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:17 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:17 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:18 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:20 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:22 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:22 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:22 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:22 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:22 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:22 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:22 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:24 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:26 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:26 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 14304.67% | Free: $9240.14 | Equity: $9305.19 | Used: $65.05
2025-12-19 02:17:27 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:27 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:27 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:27 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:27 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:27 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:28 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:30 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:32 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:32 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:32 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:32 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:32 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:32 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:32 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:33 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:17:33 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-23] Got response: status=200
2025-12-19 02:17:33 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-23] No new updates (updates array empty)
2025-12-19 02:17:33 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 24 starting...
2025-12-19 02:17:33 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:17:33 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-24] Making request to Telegram...
2025-12-19 02:17:34 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:36 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:37 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:37 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:37 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:37 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:37 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:37 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:38 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:40 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:42 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:42 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:17:43 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:17:43 - src.managers.profit_booking_reentry_manager - INFO - 🔄 Profit Chain PROFIT_XAUUSD_1a7bfc2e Entered Recovery Mode (Attempt 1/1)
2025-12-19 02:17:45 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:17:46 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:17:46 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:17:48 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:48 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:48 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:48 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:48 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:48 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:17:48 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:50 - src.services.price_monitor_service - DEBUG - 💓 Monitor loop heartbeat - Cycle #350, Running: True, Pending: SL Hunt=0, TP=0, Exit=0
2025-12-19 02:17:50 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:50 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 42892.71% | Free: $9277.46 | Equity: $9299.14 | Used: $21.68
2025-12-19 02:17:52 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:17:53 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:17:54 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:17:54 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:17:56 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:17:57 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:17:57 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:17:59 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:17:59 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:18:01 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:18:03 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:18:03 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:18:04 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:18:04 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-24] Got response: status=200
2025-12-19 02:18:04 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-24] No new updates (updates array empty)
2025-12-19 02:18:04 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 25 starting...
2025-12-19 02:18:04 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:18:04 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-25] Making request to Telegram...
2025-12-19 02:18:05 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:18:07 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:18:08 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:18:09 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:18:09 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:18:10 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:18:12 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:18:12 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:18:13 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:18:13 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:18:13 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:18:13 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:18:13 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:18:13 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:18:13 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:18:15 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:64959 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:18:17 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:18:18 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:18:20 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:18:20 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:18:21 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:18:23 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:18:23 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:18:24 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:18:24 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:18:26 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:18:28 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:18:28 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:18:30 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:18:32 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:18:32 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 42874.03% | Free: $9273.41 | Equity: $9295.09 | Used: $21.68
2025-12-19 02:18:33 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:18:34 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:18:34 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-25] Got response: status=200
2025-12-19 02:18:34 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-25] No new updates (updates array empty)
2025-12-19 02:18:34 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 26 starting...
2025-12-19 02:18:34 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:18:34 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-26] Making request to Telegram...
2025-12-19 02:18:34 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:18:34 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:18:36 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:18:37 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:18:37 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:18:39 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:18:39 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:18:40 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:18:42 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:18:42 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:18:44 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:18:46 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:18:47 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:18:48 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:18:48 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:18:50 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:18:51 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:18:51 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:18:53 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:18:53 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:18:54 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:18:56 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:18:56 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:18:58 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:19:00 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:19:01 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:19:02 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:19:02 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:19:04 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:19:04 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:19:04 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-26] Got response: status=200
2025-12-19 02:19:04 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-26] No new updates (updates array empty)
2025-12-19 02:19:04 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 27 starting...
2025-12-19 02:19:04 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:19:04 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-27] Making request to Telegram...
2025-12-19 02:19:05 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:19:05 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:19:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:19:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:19:08 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:19:10 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:19:10 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:19:12 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:19:14 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:19:15 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:19:17 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:19:17 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:19:18 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:19:20 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:19:20 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:19:21 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:19:21 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:19:23 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:19:24 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:19:24 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:19:24 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 42867.34% | Free: $9271.96 | Equity: $9293.64 | Used: $21.68
←[32mINFO←[0m:     127.0.0.1:65001 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:19:26 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:19:28 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:19:29 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:19:31 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:19:31 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:19:32 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:19:34 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:19:34 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:19:34 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:19:34 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-27] Got response: status=200
2025-12-19 02:19:34 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-27] No new updates (updates array empty)
2025-12-19 02:19:34 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 28 starting...
2025-12-19 02:19:34 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:19:34 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-28] Making request to Telegram...
2025-12-19 02:19:35 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:19:35 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:19:37 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:19:38 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:19:38 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:19:40 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:19:42 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:19:43 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:19:45 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:19:45 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:19:47 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:19:48 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:19:48 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:19:50 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:19:50 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:19:50 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:19:50 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:19:50 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:19:50 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:19:50 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:19:52 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:19:54 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:19:55 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:19:56 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:19:56 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:19:57 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:19:59 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:19:59 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:20:01 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:20:01 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:20:01 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:20:01 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:20:01 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:20:01 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:20:01 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:20:03 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:20:03 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 42904.94% | Free: $9280.11 | Equity: $9301.79 | Used: $21.68
2025-12-19 02:20:05 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:20:05 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:20:05 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-28] Got response: status=200
2025-12-19 02:20:05 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-28] No new updates (updates array empty)
2025-12-19 02:20:05 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 29 starting...
2025-12-19 02:20:05 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:20:05 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-29] Making request to Telegram...
2025-12-19 02:20:06 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:20:07 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:20:07 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:20:08 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:20:10 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:20:10 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:20:11 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:20:11 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:20:13 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:20:14 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:20:14 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:20:16 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:65034 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:20:18 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:20:19 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:20:21 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:20:21 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:20:22 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:20:24 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:20:24 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:20:26 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:20:26 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:20:27 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:20:29 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:20:29 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:20:31 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:20:33 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:20:34 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:20:35 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:20:35 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-29] Got response: status=200
2025-12-19 02:20:35 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-29] No new updates (updates array empty)
2025-12-19 02:20:35 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 30 starting...
2025-12-19 02:20:35 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:20:35 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-30] Making request to Telegram...
2025-12-19 02:20:35 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:20:35 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:20:37 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:20:38 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:20:38 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:20:40 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:20:40 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:20:40 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:20:40 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:20:40 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:20:40 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:20:40 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:20:42 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:20:44 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:20:44 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 42899.86% | Free: $9279.01 | Equity: $9300.69 | Used: $21.68
2025-12-19 02:20:45 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:20:47 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:20:47 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:20:48 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:20:50 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:20:50 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:20:51 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:20:51 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:20:52 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:20:54 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:20:54 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:20:56 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:20:58 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:20:59 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:21:01 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:21:01 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:21:02 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:21:04 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:21:04 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:21:05 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:21:05 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:21:05 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-30] Got response: status=200
2025-12-19 02:21:05 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:21:05 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-30] No new updates (updates array empty)
2025-12-19 02:21:05 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 31 starting...
2025-12-19 02:21:05 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:21:05 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-31] Making request to Telegram...
2025-12-19 02:21:07 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:21:08 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:21:08 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:21:10 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:21:12 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:21:13 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:21:15 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:21:15 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:21:16 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:21:18 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:21:18 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:21:19 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:21:19 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:21:21 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:21:22 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:21:22 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:50751 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:21:24 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:21:26 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:21:27 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:21:29 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:21:29 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:21:31 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:21:32 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:21:32 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:21:34 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:21:34 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:21:35 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:21:35 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:21:35 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-31] Got response: status=200
2025-12-19 02:21:35 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-31] No new updates (updates array empty)
2025-12-19 02:21:35 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 32 starting...
2025-12-19 02:21:35 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:21:35 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-32] Making request to Telegram...
2025-12-19 02:21:37 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:21:37 - src.services.price_monitor_service - DEBUG - 💓 Monitor loop heartbeat - Cycle #400, Running: True, Pending: SL Hunt=0, TP=0, Exit=0
2025-12-19 02:21:37 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:21:37 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 42857.20% | Free: $9269.76 | Equity: $9291.44 | Used: $21.68
2025-12-19 02:21:39 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:21:41 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:21:42 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:21:43 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:21:43 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:21:45 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:21:46 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:21:46 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:21:48 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:21:48 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:21:49 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:21:51 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:21:51 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:21:53 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:21:55 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:21:56 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:21:57 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:21:57 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:21:59 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:22:01 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:22:01 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:22:03 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:22:03 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:22:04 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:22:06 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:22:06 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-32] Got response: status=200
2025-12-19 02:22:06 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-32] No new updates (updates array empty)
2025-12-19 02:22:06 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 33 starting...
2025-12-19 02:22:06 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:22:06 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-33] Making request to Telegram...
2025-12-19 02:22:06 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:22:06 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:22:08 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:22:10 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:22:11 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:22:12 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:22:12 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:22:14 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:22:16 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:22:16 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:22:17 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:22:17 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:22:19 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:22:20 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:22:20 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:50790 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:22:22 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:22:22 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 42844.74% | Free: $9267.06 | Equity: $9288.74 | Used: $21.68
2025-12-19 02:22:24 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:22:25 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:22:26 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:22:26 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:22:28 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:22:30 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:22:30 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:22:31 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:22:31 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:22:33 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:22:34 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:22:34 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:22:36 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:22:36 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-33] Got response: status=200
2025-12-19 02:22:36 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-33] No new updates (updates array empty)
2025-12-19 02:22:36 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 34 starting...
2025-12-19 02:22:36 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:22:36 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-34] Making request to Telegram...
2025-12-19 02:22:36 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:22:38 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:22:39 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:22:41 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:22:41 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:22:42 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:22:44 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:22:44 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:22:45 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:22:45 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:22:47 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:22:48 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:22:48 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:22:50 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:22:52 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:22:53 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:22:55 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:22:55 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:22:56 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:22:57 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:22:57 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:22:59 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:22:59 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:23:01 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:23:02 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:23:02 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:23:04 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:23:06 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:23:06 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 42846.36% | Free: $9267.41 | Equity: $9289.09 | Used: $21.68
2025-12-19 02:23:06 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:23:06 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-34] Got response: status=200
2025-12-19 02:23:06 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-34] No new updates (updates array empty)
2025-12-19 02:23:06 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 35 starting...
2025-12-19 02:23:06 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:23:06 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-35] Making request to Telegram...
2025-12-19 02:23:07 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:23:09 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:23:09 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:23:10 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:23:12 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:23:12 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:23:13 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:23:13 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:23:15 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:23:16 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:23:16 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:23:18 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:50822 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:23:20 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:23:21 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:23:23 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:23:23 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:23:25 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:23:26 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:23:26 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:23:28 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:23:28 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:23:29 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:23:31 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:23:31 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:23:33 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:23:35 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:23:36 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:23:36 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:23:36 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-35] Got response: status=200
2025-12-19 02:23:36 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-35] No new updates (updates array empty)
2025-12-19 02:23:36 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 36 starting...
2025-12-19 02:23:36 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:23:36 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-36] Making request to Telegram...
2025-12-19 02:23:38 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:23:38 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:23:39 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:23:41 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:23:41 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:23:42 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:23:42 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:23:44 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:23:45 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:23:45 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:23:47 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:23:49 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:23:50 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:23:52 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:23:52 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:23:53 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:23:55 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:23:55 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:23:57 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:23:57 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:23:58 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:23:59 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:23:59 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:23:59 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 42848.89% | Free: $9267.96 | Equity: $9289.64 | Used: $21.68
2025-12-19 02:24:01 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:24:03 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:24:04 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:24:06 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:24:06 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:24:07 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:24:07 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-36] Got response: status=200
2025-12-19 02:24:07 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-36] No new updates (updates array empty)
2025-12-19 02:24:07 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 37 starting...
2025-12-19 02:24:07 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:24:07 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-37] Making request to Telegram...
2025-12-19 02:24:08 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:24:09 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:24:09 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:24:11 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:24:11 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:24:12 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:24:14 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:24:14 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:24:16 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:24:18 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:24:19 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:24:20 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:24:20 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:24:22 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:24:23 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:24:23 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:24:25 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:24:25 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:24:26 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:24:28 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:24:28 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:62933 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:24:30 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:24:32 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:24:33 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:24:34 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:24:34 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:24:36 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:24:37 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:24:37 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-37] Got response: status=200
2025-12-19 02:24:37 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-37] No new updates (updates array empty)
2025-12-19 02:24:37 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 38 starting...
2025-12-19 02:24:37 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:24:37 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-38] Making request to Telegram...
2025-12-19 02:24:37 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:24:37 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:24:39 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:24:39 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:24:40 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:24:42 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:24:42 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:24:44 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:24:44 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 42833.90% | Free: $9264.71 | Equity: $9286.39 | Used: $21.68
2025-12-19 02:24:46 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:24:47 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:24:48 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:24:48 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:24:50 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:24:51 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:24:51 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:24:53 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:24:53 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:24:54 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:24:56 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:24:56 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:24:58 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:25:00 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:25:01 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:25:02 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:25:02 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:25:04 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:25:06 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:25:06 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:25:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:25:07 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:25:07 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:25:07 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-38] Got response: status=200
2025-12-19 02:25:07 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-38] No new updates (updates array empty)
2025-12-19 02:25:07 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 39 starting...
2025-12-19 02:25:07 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:25:07 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-39] Making request to Telegram...
2025-12-19 02:25:09 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:25:10 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:25:10 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:25:12 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:25:14 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:25:15 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:25:16 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:25:16 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:25:18 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:25:19 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:25:19 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:25:21 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:25:21 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:25:22 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:25:24 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:25:24 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     127.0.0.1:62968 - "←[1mPOST /logstores/logstore_ens_ip/shards/lb HTTP/1.1←[0m" ←[31m404 Not Found←[0m
2025-12-19 02:25:26 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:25:28 - src.services.price_monitor_service - DEBUG - 💓 Monitor loop heartbeat - Cycle #450, Running: True, Pending: SL Hunt=0, TP=0, Exit=0
2025-12-19 02:25:28 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:25:28 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] 📊 Level: 42843.13% | Free: $9266.71 | Equity: $9288.39 | Used: $21.68
2025-12-19 02:25:29 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:25:30 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:25:30 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:25:32 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:25:34 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:25:34 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:25:35 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:25:35 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:25:37 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:25:37 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:25:37 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-39] Got response: status=200
2025-12-19 02:25:37 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-39] No new updates (updates array empty)
2025-12-19 02:25:37 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 40 starting...
2025-12-19 02:25:37 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:25:37 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-40] Making request to Telegram...
2025-12-19 02:25:38 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:25:38 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:25:40 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:25:42 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:25:43 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:25:45 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:25:45 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:25:46 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:25:48 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:25:48 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:25:49 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:25:49 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:25:50 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:25:52 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:25:52 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:25:54 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:25:56 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:25:57 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:25:59 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:25:59 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:26:00 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:26:02 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:26:02 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:26:04 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:26:04 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:26:05 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:26:07 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
2025-12-19 02:26:07 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:26:08 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-19 02:26:08 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-40] Got response: status=200
2025-12-19 02:26:08 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-40] No new updates (updates array empty)
2025-12-19 02:26:08 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 41 starting...
2025-12-19 02:26:08 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-19 02:26:08 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-41] Making request to Telegram...
2025-12-19 02:26:09 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:26:11 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:26:12 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494006570: $-13.55
Auto-reconciliation: Position 494006570 closed by Stop Loss (PnL: $-13.55)
2025-12-19 02:26:13 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007108: $-11.25
Auto-reconciliation: Position 494007108 closed by Stop Loss (PnL: $-11.25)
2025-12-19 02:26:14 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:26:14 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:26:16 - src.clients.mt5_client - DEBUG - Fetched actual profit for ticket 494007110: $-11.30
Auto-reconciliation: Position 494007110 closed by Stop Loss (PnL: $-11.30)
2025-12-19 02:26:17 - src.managers.profit_booking_reentry_manager - INFO - 💎 Profit Order SL Hit registered: XAUUSD Level 1 @ 4335.0650000000005
2025-12-19 02:26:17 - src.managers.profit_booking_reentry_manager - INFO - 🛑 Profit Chain PROFIT_XAUUSD_1a7bfc2e Hard Stopped (Max Recovery Exceeded)
2025-12-19 02:26:18 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [LOGIC_DETECTION] Normalized 'ZepixPremium' → 'LOGIC1' for XAUUSD
2025-12-19 02:26:18 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BULLISH, 15M=BULLISH, Direction=BULLISH)
2025-12-19 02:26:20 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007108 has no chain_id
2025-12-19 02:26:21 - src.services.price_monitor_service - WARNING - ⚠️ Cannot register SL hunt - Trade 494007110 has no chain_id
←[32mINFO←[0m:     Shutting down
2025-12-19 02:26:21 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-19 02:26:21 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9288.99 | Equity: $9288.99 | Used: $0.00
←[32mINFO←[0m:     Waiting for application shutdown.
[LIFESPAN] Shutdown signal received - cleaning up...
[SHUTDOWN] Stopping Telegram polling...
2025-12-19 02:26:21 - src.clients.telegram_bot - INFO - [POLLING] Stopping polling thread...
2025-12-19 02:26:26 - src.clients.telegram_bot - INFO - [POLLING] Polling thread stopped
[SHUTDOWN] Cancelling background tasks...
[SHUTDOWN] Cancelling task: <Task pending name='Task-4' coro=<TradingEngine.manage_open_trades() running at C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main\src\core\trading_engine.py:1071> wait_for=<Future pending cb=[Task.task_wakeup()]>>
[2025-12-19 02:26:26] Trade monitor cancelled - graceful shutdown
[SHUTDOWN] Background tasks cancelled. Shutdown complete.
2025-12-19 02:26:26 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     Application shutdown complete.
←[32mINFO←[0m:     Finished server process [←[36m5376←[0m]
2025-12-19 02:26:26 - src.services.price_monitor_service - INFO - Monitor loop cancelled
2025-12-19 02:26:26 - src.services.price_monitor_service - DEBUG - Monitor loop stopped after 461 cycles
PS C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main>