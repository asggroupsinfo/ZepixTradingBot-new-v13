Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\WINDOWS\system32> cd "c:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main"
PS C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main> python src/main.py --host 0.0.0.0 --port 80
[EVENT-LOOP] Set WindowsProactorEventLoopPolicy on Windows
[LOGGING CONFIG] Loaded saved log level: INFO
[LOGGING CONFIG] Loaded trading_debug: True
═══════════════════════════════════════
🚀 BOT STARTING - LOGGING LEVEL: INFO
═══════════════════════════════════════
2025-12-13 00:01:56 - __main__ - INFO - Bot starting with logging level: INFO
[LOGGING CONFIG] Loaded saved log level: INFO
[LOGGING CONFIG] Loaded trading_debug: True
Config loaded - MT5 Login: 308646228, Server: XMGlobal-MT5 6
DEBUG: TimeframeTrendManager using config file: C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main\config\timeframe_trends.json
SUCCESS: Loaded trends from C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main\config\timeframe_trends.json
DEBUG: Loaded MANUAL trend for AUDUSD 1h: BULLISH
DEBUG: Total manual trends loaded: 1
2025-12-13 00:01:57 - src.managers.recovery_window_monitor - INFO - ✅ RecoveryWindowMonitor initialized
2025-12-13 00:01:57 - src.managers.profit_protection_manager - INFO -
Profit Protection Settings Loaded:
├─ Enabled: True
├─ Mode: ⚖️ BALANCED
├─ Multiplier: 6.0x
├─ Min Threshold: $20.0
├─ Order A: ON ✅
└─ Order B: ON ✅

2025-12-13 00:01:57 - src.managers.profit_protection_manager - INFO - ✅ ProfitProtectionManager initialized
2025-12-13 00:01:57 - src.managers.sl_reduction_optimizer - INFO -
SL Reduction Settings Loaded:
├─ Enabled: True
├─ Strategy: ⚖️ BALANCED
├─ Reduction: 30%
└─ Description: Recommended for most conditions

2025-12-13 00:01:57 - src.managers.sl_reduction_optimizer - INFO - ✅ SLReductionOptimizer initialized
✅ Fine-Tune managers initialized (Recovery Monitor, Profit Protection, SL Optimizer)
✅ Autonomous System Manager initialized
2025-12-13 00:01:57 - src.menu.fine_tune_menu_handler - INFO - ✅ FineTuneMenuHandler initialized (Compatible Mode)
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
←[32mINFO←[0m:     Started server process [←[36m9440←[0m]
←[32mINFO←[0m:     Waiting for application startup.
======================================================================
STARTING ZEPIX TRADING BOT v2.0
======================================================================
Initializing components...
2025-12-13 00:01:57 - src.menu.fine_tune_menu_handler - INFO - ✅ FineTuneMenuHandler initialized (Compatible Mode)
✅ TelegramBot: Fine-Tune Menu Handler initialized
✅ TelegramBot: Re-entry Menu Handler initialized
✅ TelegramBot: Profit Booking Menu Handler initialized
SUCCESS: MT5 connection established
Account Balance: $9238.59
Account: 308646228 | Server: XMGlobal-MT5 6
2025-12-13 00:01:58 - src.clients.telegram_bot - INFO - SUCCESS: Trend manager set in Telegram bot
2025-12-13 00:01:58 - src.core.trading_engine - INFO - 📋 [RE-ENTRY_CONFIG] Startup Configuration:
  SL Hunt Enabled: True
  TP Re-entry Enabled: True
  Exit Continuation Enabled: True
  Monitor Interval: 5s
  SL Hunt Offset: 1.0 pips
  TP Continuation Gap: 2.0 pips
  Max Chain Levels: 5
  SL Reduction Per Level: 0.3
2025-12-13 00:01:58 - src.services.price_monitor_service - INFO - ✅ Price Monitor Service started successfully - Task created: <Task pending name='Task-3' coro=<PriceMonitorService._monitor_loop() running at C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main\src\services\price_monitor_service.py:129>>, is_running: True
2025-12-13 00:01:58 - src.core.trading_engine - INFO - ✅ Price Monitor Service confirmed running after initialization
2025-12-13 00:01:58 - src.managers.profit_booking_manager - INFO - SUCCESS: Recovered 0 profit booking chains from database
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
←[32mINFO←[0m:     Application startup complete.
2025-12-13 00:01:59 - src.clients.telegram_bot - INFO - [POLLING] Starting polling loop...
2025-12-13 00:01:59 - src.clients.telegram_bot - INFO - SUCCESS: Telegram bot polling started
←[32mINFO←[0m:     Uvicorn running on ←[1mhttp://0.0.0.0:80←[0m (Press CTRL+C to quit)
[POLLING-THREAD] Polling thread exited
DEBUG: Parsed param - type: level, command: set_log_level, value: DEBUG
🛑 [PARAM SELECTION] START - param_type=level, value=DEBUG, command=set_log_level
[PARAM SELECTION] Cleaned value: 'DEBUG' -> 'DEBUG'
[PARAM SELECTION] Stored param: level=DEBUG, All params: {'level': 'DEBUG'}
[PARAM SELECTION] Final stored params after preservation: {'level': 'DEBUG'}
[PARAM SELECTION] All params collected. Final params: {'level': 'DEBUG'}, showing confirmation
✅ [PARAM SELECTION] All parameters collected - SHOWING CONFIRMATION SCREEN
🛑 [PARAM SELECTION] CRITICAL: About to show confirmation (NOT executing command)
🛑 [CONFIRMATION] START - Showing confirmation for command: set_log_level
[CONFIRMATION] Showing confirmation for set_log_level with params: {'level': 'DEBUG'}
[CONFIRMATION] Confirm button callback: execute_set_log_level
[CONFIRMATION] About to display confirmation screen (NOT executing command)
[CONFIRMATION] Confirmation screen displayed. Result: True
✅ [CONFIRMATION] Confirmation screen shown successfully
🛑 [CONFIRMATION] END - Waiting for user to click 'Confirm' button. NO EXECUTION YET.
✅ [PARAM SELECTION] Confirmation screen shown. Returning (NO EXECUTION)
🛑 [PARAM SELECTION] END - Command will ONLY execute when user clicks 'Confirm' button
2025-12-13 00:02:22 - src.menu.command_executor - INFO - EXECUTING: set_log_level with params {'level': 'DEBUG'} for user 2139792302
[VALIDATE] Validating command 'set_log_level' with params: {'level': 'DEBUG'}
[VALIDATE] Required params for set_log_level: ['level']
[VALIDATE] Validating param 'level' with value: DEBUG
[VALIDATE PARAM] Validating 'level' = 'DEBUG'
[VALIDATE PARAM] Param definition: {'type': 'string', 'format': 'uppercase', 'valid_values': ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], 'validation': <function <lambda> at 0x000002AC7FCB0220>}
[VALIDATE PARAM] Converted to uppercase: DEBUG -> DEBUG
[VALIDATE PARAM] Checking valid_values: ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
[VALIDATE PARAM] Value 'DEBUG' is in valid_values
[VALIDATE PARAM] Validation function passed
[VALIDATE PARAM] Parameter 'level' validation PASSED
[VALIDATE] Parameter 'level' validation passed
[VALIDATE] All parameters validated successfully for set_log_level
2025-12-13 00:02:22 - src.menu.command_executor - INFO - CALLING HANDLER: set_log_level with formatted params: {'level': 'DEBUG'}
2025-12-13 00:02:22 - src.menu.command_executor - DEBUG - Updated handler StreamHandler to DEBUG
2025-12-13 00:02:23 - src.menu.command_executor - INFO - Saved log level 'DEBUG' to config/logging_settings.json
═══════════════════════════════════════
📊 LOGGING LEVEL CHANGED: INFO → DEBUG
═══════════════════════════════════════
2025-12-13 00:02:24 - src.menu.command_executor - INFO - Log level changed: INFO → DEBUG (verified: True)
2025-12-13 00:02:24 - src.menu.command_executor - DEBUG - TEST: This is a DEBUG message (level=DEBUG)
2025-12-13 00:02:24 - src.menu.command_executor - INFO - TEST: This is an INFO message (level=DEBUG)
2025-12-13 00:02:24 - src.menu.command_executor - DEBUG - 🎯 HANDLER RESULT: True
2025-12-13 00:02:24 - src.menu.command_executor - DEBUG - [MENU EXECUTION] Handler set_log_level returned (no exception)
2025-12-13 00:02:24 - src.menu.command_executor - DEBUG - 🎯 HANDLER RETURNED: Command set_log_level completed
2025-12-13 00:02:24 - src.menu.command_executor - DEBUG - 📊 EXECUTION STEPS: {'validation': True, 'handler_call': True, 'handler_complete': True, 'success': False}
2025-12-13 00:02:24 - src.menu.command_executor - INFO - EXECUTION SUCCESS: set_log_level executed successfully for user 2139792302
2025-12-13 00:02:24 - src.menu.command_executor - DEBUG - [MENU EXECUTION] [OK] Command set_log_level executed successfully
2025-12-13 00:02:24 - src.menu.command_executor - DEBUG - ✅ EXECUTION SUCCESS: set_log_level
2025-12-13 00:02:24 - src.menu.command_executor - DEBUG - 📊 FINAL EXECUTION STEPS: {'validation': True, 'handler_call': True, 'handler_complete': True, 'success': True}
2025-12-13 00:02:24 - src.menu.command_executor - DEBUG - [MENU EXECUTION] Marking execution as SUCCESS for set_log_level
2025-12-13 00:02:24 - src.menu.command_executor - DEBUG - [MENU EXECUTION] Returning True for set_log_level
2025-12-13 00:02:24 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:02:26 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 6 starting...
2025-12-13 00:02:26 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-13 00:02:26 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-6] Making request to Telegram...
2025-12-13 00:02:29 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:02:34 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:02:39 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:02:44 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:02:44 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9238.59 | Equity: $9238.59 | Used: $0.00
2025-12-13 00:02:49 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:02:54 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:02:57 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-13 00:02:57 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-6] Got response: status=200
2025-12-13 00:02:57 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 7 starting...
2025-12-13 00:02:57 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-13 00:02:57 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-7] Making request to Telegram...
2025-12-13 00:02:59 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:03:04 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:03:09 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:03:14 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:03:19 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:03:24 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:03:28 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-13 00:03:28 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-7] Got response: status=200
2025-12-13 00:03:28 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 8 starting...
2025-12-13 00:03:28 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-13 00:03:28 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-8] Making request to Telegram...
2025-12-13 00:03:29 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:03:34 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:03:34 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9238.59 | Equity: $9238.59 | Used: $0.00
2025-12-13 00:03:39 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:03:44 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:03:49 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:03:54 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:03:59 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:04:00 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-13 00:04:00 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-8] Got response: status=200
2025-12-13 00:04:00 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 9 starting...
2025-12-13 00:04:00 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-13 00:04:00 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-9] Making request to Telegram...
2025-12-13 00:04:04 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:04:09 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:04:14 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:04:20 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:04:25 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:04:25 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9238.59 | Equity: $9238.59 | Used: $0.00
2025-12-13 00:04:30 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:04:31 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-13 00:04:31 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-9] Got response: status=200
2025-12-13 00:04:31 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 10 starting...
2025-12-13 00:04:31 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-13 00:04:31 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-10] Making request to Telegram...
2025-12-13 00:04:35 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:04:40 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:04:45 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:04:50 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:04:55 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:05:00 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:05:03 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-13 00:05:03 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-10] Got response: status=200
2025-12-13 00:05:03 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 11 starting...
2025-12-13 00:05:03 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-13 00:05:03 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-11] Making request to Telegram...
2025-12-13 00:05:05 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:05:10 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:05:15 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:05:15 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9238.59 | Equity: $9238.59 | Used: $0.00
2025-12-13 00:05:20 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:05:25 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:05:30 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:05:34 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-13 00:05:34 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-11] Got response: status=200
2025-12-13 00:05:34 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 12 starting...
2025-12-13 00:05:34 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-13 00:05:34 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-12] Making request to Telegram...
2025-12-13 00:05:35 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:05:40 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:05:45 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:05:50 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:05:55 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:06:00 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:06:05 - src.services.price_monitor_service - DEBUG - 💓 Monitor loop heartbeat - Cycle #50, Running: True, Pending: SL Hunt=0, TP=0, Exit=0
2025-12-13 00:06:05 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:06:05 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9238.59 | Equity: $9238.59 | Used: $0.00
2025-12-13 00:06:06 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-13 00:06:06 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-12] Got response: status=200
2025-12-13 00:06:06 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 13 starting...
2025-12-13 00:06:06 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-13 00:06:06 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-13] Making request to Telegram...
2025-12-13 00:06:10 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:06:15 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:06:20 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:06:25 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:06:30 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
Webhook received: {
  "type": "entry",
  "symbol": "XAUUSD",
  "signal": "sell",
  "tf": "5m",
  "price": 4299.255,
  "strategy": "ZepixPremium"
}
ALERT: Received alert: {'type': 'entry', 'symbol': 'XAUUSD', 'signal': 'sell', 'tf': '5m', 'price': 4299.255, 'strategy': 'ZepixPremium'}
SUCCESS: Alert validation successful
[2025-12-13 00:06:35] 🔔 Processing entry alert | Symbol: XAUUSD, TF: 5m
[2025-12-13 00:06:35] 🔍 TRADING_DEBUG: Alert=sell, TF=5m, Symbol=XAUUSD
[2025-12-13 00:06:35] 🔍 TRADING_DEBUG: Alignment={'aligned': False, 'direction': 'PENDING'}
[2025-12-13 00:06:35] 🔍 TRADING_DEBUG: SignalDir=PENDING, Logic=LOGIC1
2025-12-13 00:06:35 - src.managers.timeframe_trend_manager - DEBUG - 🔍 [ALIGNMENT_CHECK] XAUUSD LOGIC1: ✅ ALIGNED (1H=BEARISH, 15M=BEARISH, Direction=BEARISH)
[2025-12-13 00:06:35] 🔍 TRADING_DEBUG: Alert=sell, TF=5m, Symbol=XAUUSD
[2025-12-13 00:06:35] 🔍 TRADING_DEBUG: Alignment={'aligned': True, 'direction': 'BEARISH', 'details': {'1h': 'BEARISH', '15m': 'BEARISH'}, 'failure_reason': None}
[2025-12-13 00:06:35] 🔍 TRADING_DEBUG: SignalDir=PENDING, Logic=LOGIC1
[2025-12-13 00:06:35] 🔍 TRADING_DEBUG: Alert=sell, TF=5m, Symbol=XAUUSD
[2025-12-13 00:06:35] 🔍 TRADING_DEBUG: Alignment={'aligned': True, 'direction': 'BEARISH', 'details': {'1h': 'BEARISH', '15m': 'BEARISH'}, 'failure_reason': None}
[2025-12-13 00:06:35] 🔍 TRADING_DEBUG: SignalDir=BEARISH, Logic=LOGIC1
[2025-12-13 00:06:35] 🔔 Trade execution starting | Symbol: XAUUSD, Direction: BEARISH
2025-12-13 00:06:35 - src.managers.dual_order_manager - DEBUG - [DUAL_ORDER_LOT_SIZE] Symbol=XAUUSD Balance=$9238.59 Lot Size=0.05 (SAME for both orders)
2025-12-13 00:06:35 - src.managers.dual_order_manager - DEBUG - [DUAL_ORDER_RISK] Symbol=XAUUSD Valid=False Reason=Daily loss cap exceeded: $150.00 > $100.0
WARNING: Dual order error: Risk validation failed: Daily loss cap exceeded: $150.00 > $100.0
2025-12-13 00:06:36 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     34.212.75.30:0 - "←[1mPOST /webhook HTTP/1.1←[0m" ←[32m200 OK←[0m
2025-12-13 00:06:37 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Got response status=200
2025-12-13 00:06:37 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-13] Got response: status=200
2025-12-13 00:06:37 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Cycle 14 starting...
2025-12-13 00:06:37 - src.clients.telegram_bot - DEBUG - [POLLING-DEBUG] Making request to: https://api.telegram.org/bot8526101969:AAF9fqQlPbNUkb1fg3vylwG4uDNiz-Z9IY4/getUp...
2025-12-13 00:06:37 - src.clients.telegram_bot - DEBUG - [POLLING-CYCLE-14] Making request to Telegram...
2025-12-13 00:06:41 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:06:46 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:06:51 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:06:56 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
2025-12-13 00:06:56 - src.services.price_monitor_service - DEBUG - 💰 [MARGIN_CHECK] ✅ No positions | Free: $9238.59 | Equity: $9238.59 | Used: $0.00
2025-12-13 00:07:01 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     Shutting down
←[32mINFO←[0m:     Waiting for application shutdown.
[LIFESPAN] Shutdown signal received - cleaning up...
[SHUTDOWN] Stopping Telegram polling...
2025-12-13 00:07:02 - src.clients.telegram_bot - INFO - [POLLING] Stopping polling thread...
2025-12-13 00:07:07 - src.clients.telegram_bot - INFO - [POLLING] Polling thread stopped
[SHUTDOWN] Cancelling background tasks...
[SHUTDOWN] Cancelling task: <Task pending name='Task-4' coro=<TradingEngine.manage_open_trades() running at C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main\src\core\trading_engine.py:909> wait_for=<Future pending cb=[Task.task_wakeup()]>>
[2025-12-13 00:07:07] Trade monitor cancelled - graceful shutdown
[SHUTDOWN] Background tasks cancelled. Shutdown complete.
2025-12-13 00:07:07 - src.services.price_monitor_service - DEBUG - [MONITOR_CYCLE] Checking opportunities - SL Hunt: 0, TP Continuation: 0, Exit Continuation: 0
←[32mINFO←[0m:     Application shutdown complete.
←[32mINFO←[0m:     Finished server process [←[36m9440←[0m]
2025-12-13 00:07:07 - src.services.price_monitor_service - INFO - Monitor loop cancelled
2025-12-13 00:07:07 - src.services.price_monitor_service - DEBUG - Monitor loop stopped after 62 cycles
PS C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main>