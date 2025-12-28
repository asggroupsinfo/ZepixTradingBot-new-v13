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
2025-12-12 23:22:10 - __main__ - INFO - Bot starting with logging level: INFO
[LOGGING CONFIG] Loaded saved log level: INFO
[LOGGING CONFIG] Loaded trading_debug: True
Config loaded - MT5 Login: 308646228, Server: XMGlobal-MT5 6
DEBUG: TimeframeTrendManager using config file: C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main\config\timeframe_trends.json
SUCCESS: Loaded trends from C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main\config\timeframe_trends.json
DEBUG: Loaded MANUAL trend for XAUUSD 1h: BEARISH
DEBUG: Loaded MANUAL trend for XAUUSD 15m: BULLISH
DEBUG: Loaded MANUAL trend for AUDUSD 1h: BULLISH
DEBUG: Total manual trends loaded: 3
2025-12-12 23:22:10 - src.managers.recovery_window_monitor - INFO - ✅ RecoveryWindowMonitor initialized
2025-12-12 23:22:10 - src.managers.profit_protection_manager - INFO -
Profit Protection Settings Loaded:
├─ Enabled: True
├─ Mode: ⚖️ BALANCED
├─ Multiplier: 6.0x
├─ Min Threshold: $20.0
├─ Order A: ON ✅
└─ Order B: ON ✅

2025-12-12 23:22:10 - src.managers.profit_protection_manager - INFO - ✅ ProfitProtectionManager initialized
2025-12-12 23:22:10 - src.managers.sl_reduction_optimizer - INFO -
SL Reduction Settings Loaded:
├─ Enabled: True
├─ Strategy: ⚖️ BALANCED
├─ Reduction: 30%
└─ Description: Recommended for most conditions

2025-12-12 23:22:10 - src.managers.sl_reduction_optimizer - INFO - ✅ SLReductionOptimizer initialized
✅ Fine-Tune managers initialized (Recovery Monitor, Profit Protection, SL Optimizer)
✅ Autonomous System Manager initialized
2025-12-12 23:22:10 - src.menu.fine_tune_menu_handler - INFO - ✅ FineTuneMenuHandler initialized (Compatible Mode)
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
←[32mINFO←[0m:     Started server process [←[36m26140←[0m]
←[32mINFO←[0m:     Waiting for application startup.
======================================================================
STARTING ZEPIX TRADING BOT v2.0
======================================================================
Initializing components...
2025-12-12 23:22:10 - src.menu.fine_tune_menu_handler - INFO - ✅ FineTuneMenuHandler initialized (Compatible Mode)
✅ TelegramBot: Fine-Tune Menu Handler initialized
✅ TelegramBot: Re-entry Menu Handler initialized
✅ TelegramBot: Profit Booking Menu Handler initialized
SUCCESS: MT5 connection established
Account Balance: $9238.59
Account: 308646228 | Server: XMGlobal-MT5 6
2025-12-12 23:22:12 - src.clients.telegram_bot - INFO - SUCCESS: Trend manager set in Telegram bot
2025-12-12 23:22:12 - src.core.trading_engine - INFO - 📋 [RE-ENTRY_CONFIG] Startup Configuration:
  SL Hunt Enabled: True
  TP Re-entry Enabled: True
  Exit Continuation Enabled: True
  Monitor Interval: 5s
  SL Hunt Offset: 1.0 pips
  TP Continuation Gap: 2.0 pips
  Max Chain Levels: 5
  SL Reduction Per Level: 0.3
2025-12-12 23:22:12 - src.services.price_monitor_service - INFO - ✅ Price Monitor Service started successfully - Task created: <Task pending name='Task-3' coro=<PriceMonitorService._monitor_loop() running at C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main\src\services\price_monitor_service.py:129>>, is_running: True
2025-12-12 23:22:12 - src.core.trading_engine - INFO - ✅ Price Monitor Service confirmed running after initialization
2025-12-12 23:22:12 - src.managers.profit_booking_manager - INFO - SUCCESS: Recovered 0 profit booking chains from database
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
2025-12-12 23:22:13 - src.clients.telegram_bot - INFO - [POLLING] Starting polling loop...
2025-12-12 23:22:13 - src.clients.telegram_bot - INFO - SUCCESS: Telegram bot polling started
←[32mINFO←[0m:     Uvicorn running on ←[1mhttp://0.0.0.0:80←[0m (Press CTRL+C to quit)
[POLLING-THREAD] Polling thread exited
[MENU EXECUTION] Empty params detected, attempting recovery...
2025-12-12 23:23:44 - src.menu.command_executor - INFO - EXECUTING: clear_daily_loss with params {} for user 2139792302
[VALIDATE] Validating command 'clear_daily_loss' with params: {}
[VALIDATE] Required params for clear_daily_loss: []
[VALIDATE] All parameters validated successfully for clear_daily_loss
2025-12-12 23:23:44 - src.menu.command_executor - INFO - CALLING HANDLER: clear_daily_loss with formatted params: {}
2025-12-12 23:23:44 - src.managers.risk_manager - INFO - [RESET_DAILY_LOSS] Clearing daily stats (Current: Loss=$0.00, Profit=$0.00)
2025-12-12 23:23:44 - src.managers.risk_manager - INFO - ✅ Stats saved successfully: Daily Loss=$0.00, Lifetime=$0.00
2025-12-12 23:23:44 - src.managers.risk_manager - INFO - [RESET_DAILY_LOSS] ✅ Daily loss cleared successfully and verified in data/stats.json
2025-12-12 23:23:47 - src.menu.command_executor - INFO - EXECUTION SUCCESS: clear_daily_loss executed successfully for user 2139792302
[MENU EXECUTION] Empty params detected, attempting recovery...
2025-12-12 23:24:02 - src.menu.command_executor - INFO - EXECUTING: clear_loss_data with params {} for user 2139792302
[VALIDATE] Validating command 'clear_loss_data' with params: {}
[VALIDATE] Required params for clear_loss_data: []
[VALIDATE] All parameters validated successfully for clear_loss_data
2025-12-12 23:24:02 - src.menu.command_executor - INFO - CALLING HANDLER: clear_loss_data with formatted params: {}
2025-12-12 23:24:02 - src.managers.risk_manager - INFO - ✅ Stats saved successfully: Daily Loss=$0.00, Lifetime=$0.00
2025-12-12 23:24:04 - src.menu.command_executor - INFO - EXECUTION SUCCESS: clear_loss_data executed successfully for user 2139792302
2025-12-12 23:24:13 - src.menu.reentry_menu_handler - INFO - Re-entry menu shown to user 2139792302
2025-12-12 23:24:17 - src.menu.reentry_menu_handler - INFO - Handling toggle callback: toggle_sl_hunt
2025-12-12 23:24:17 - src.menu.reentry_menu_handler - INFO - SL Hunt toggled: False → True
2025-12-12 23:24:20 - src.menu.reentry_menu_handler - INFO - Re-entry menu shown to user 2139792302
2025-12-12 23:24:23 - src.menu.reentry_menu_handler - INFO - Handling toggle callback: toggle_exit_continuation
2025-12-12 23:24:23 - src.menu.reentry_menu_handler - INFO - Exit Continuation toggled: False → True
2025-12-12 23:24:26 - src.menu.reentry_menu_handler - INFO - Re-entry menu shown to user 2139792302
2025-12-12 23:24:30 - src.menu.reentry_menu_handler - INFO - Handling toggle callback: toggle_exit_continuation
2025-12-12 23:24:30 - src.menu.reentry_menu_handler - INFO - Exit Continuation toggled: True → False
2025-12-12 23:24:33 - src.menu.reentry_menu_handler - INFO - Re-entry menu shown to user 2139792302
2025-12-12 23:24:36 - src.menu.reentry_menu_handler - INFO - Handling toggle callback: toggle_tp_continuation
2025-12-12 23:24:36 - src.menu.reentry_menu_handler - INFO - TP Continuation toggled: False → True
2025-12-12 23:24:41 - src.menu.reentry_menu_handler - INFO - Re-entry menu shown to user 2139792302
2025-12-12 23:24:45 - src.menu.reentry_menu_handler - INFO - Handling toggle callback: toggle_tp_continuation
2025-12-12 23:24:45 - src.menu.reentry_menu_handler - INFO - TP Continuation toggled: True → False
2025-12-12 23:24:48 - src.menu.reentry_menu_handler - INFO - Re-entry menu shown to user 2139792302
2025-12-12 23:24:51 - src.menu.reentry_menu_handler - INFO - Handling toggle callback: toggle_exit_continuation
2025-12-12 23:24:51 - src.menu.reentry_menu_handler - INFO - Exit Continuation toggled: False → True
2025-12-12 23:24:54 - src.menu.reentry_menu_handler - INFO - Re-entry menu shown to user 2139792302
2025-12-12 23:25:03 - src.menu.reentry_menu_handler - INFO - Handling toggle callback: toggle_tp_continuation
2025-12-12 23:25:03 - src.menu.reentry_menu_handler - INFO - TP Continuation toggled: False → True
2025-12-12 23:25:06 - src.menu.reentry_menu_handler - INFO - Re-entry menu shown to user 2139792302
[MENU EXECUTION] Empty params detected, attempting recovery...
2025-12-12 23:25:24 - src.menu.command_executor - INFO - EXECUTING: sl_status with params {} for user 2139792302
[VALIDATE] Validating command 'sl_status' with params: {}
[VALIDATE] Required params for sl_status: []
[VALIDATE] All parameters validated successfully for sl_status
2025-12-12 23:25:24 - src.menu.command_executor - INFO - CALLING HANDLER: sl_status with formatted params: {}
2025-12-12 23:25:25 - src.menu.command_executor - INFO - EXECUTION SUCCESS: sl_status executed successfully for user 2139792302
2025-12-12 23:25:35 - src.menu.profit_booking_menu_handler - INFO - Profit Booking menu shown to user 2139792302 (Mode: SL-2.1)
DEBUG: Parsed param - type: symbol, command: set_trend, value: XAUUSD
🛑 [PARAM SELECTION] START - param_type=symbol, value=XAUUSD, command=set_trend
[PARAM SELECTION] Cleaned value: 'XAUUSD' -> 'XAUUSD'
[PARAM SELECTION] Stored param: symbol=XAUUSD, All params: {'symbol': 'XAUUSD'}
[PARAM SELECTION] Final stored params after preservation: {'symbol': 'XAUUSD'}
🔄 [PARAM SELECTION] More parameters needed. Next param: timeframe
🔄 [PARAM SELECTION] Showing next parameter selection (NOT executing command)
✅ [PARAM SELECTION] Next parameter selection shown. Returning (NO EXECUTION)
DEBUG: Parsed param - type: timeframe, command: set_trend, value: 1d
🛑 [PARAM SELECTION] START - param_type=timeframe, value=1d, command=set_trend
[PARAM SELECTION] Cleaned value: '1d' -> '1d'
[PARAM SELECTION] Stored param: timeframe=1d, All params: {'symbol': 'XAUUSD', 'timeframe': '1d'}
[PARAM SELECTION] Final stored params after preservation: {'symbol': 'XAUUSD', 'timeframe': '1d'}
🔄 [PARAM SELECTION] More parameters needed. Next param: trend
🔄 [PARAM SELECTION] Showing next parameter selection (NOT executing command)
✅ [PARAM SELECTION] Next parameter selection shown. Returning (NO EXECUTION)
DEBUG: Parsed param - type: trend, command: set_trend, value: BEARISH
🛑 [PARAM SELECTION] START - param_type=trend, value=BEARISH, command=set_trend
[PARAM SELECTION] Cleaned value: 'BEARISH' -> 'BEARISH'
[PARAM SELECTION] Stored param: trend=BEARISH, All params: {'symbol': 'XAUUSD', 'timeframe': '1d', 'trend': 'BEARISH'}
[PARAM SELECTION] Final stored params after preservation: {'symbol': 'XAUUSD', 'timeframe': '1d', 'trend': 'BEARISH'}
[PARAM SELECTION] All params collected. Final params: {'symbol': 'XAUUSD', 'timeframe': '1d', 'trend': 'BEARISH'}, showing confirmation
✅ [PARAM SELECTION] All parameters collected - SHOWING CONFIRMATION SCREEN
🛑 [PARAM SELECTION] CRITICAL: About to show confirmation (NOT executing command)
🛑 [CONFIRMATION] START - Showing confirmation for command: set_trend
[CONFIRMATION] Showing confirmation for set_trend with params: {'symbol': 'XAUUSD', 'timeframe': '1d', 'trend': 'BEARISH'}
[CONFIRMATION] Confirm button callback: execute_set_trend
[CONFIRMATION] About to display confirmation screen (NOT executing command)
[CONFIRMATION] Confirmation screen displayed. Result: True
✅ [CONFIRMATION] Confirmation screen shown successfully
🛑 [CONFIRMATION] END - Waiting for user to click 'Confirm' button. NO EXECUTION YET.
✅ [PARAM SELECTION] Confirmation screen shown. Returning (NO EXECUTION)
🛑 [PARAM SELECTION] END - Command will ONLY execute when user clicks 'Confirm' button
2025-12-12 23:26:23 - src.menu.command_executor - INFO - EXECUTING: set_trend with params {'symbol': 'XAUUSD', 'timeframe': '1d', 'trend': 'BEARISH'} for user 2139792302
[VALIDATE] Validating command 'set_trend' with params: {'symbol': 'XAUUSD', 'timeframe': '1d', 'trend': 'BEARISH'}
[VALIDATE] Required params for set_trend: ['symbol', 'timeframe', 'trend']
[VALIDATE] Validating param 'symbol' with value: XAUUSD
[VALIDATE PARAM] Validating 'symbol' = 'XAUUSD'
[VALIDATE PARAM] Param definition: {'type': 'string', 'format': 'uppercase', 'valid_values': ['XAUUSD', 'EURUSD', 'GBPUSD', 'USDJPY', 'USDCAD', 'AUDUSD', 'NZDUSD', 'EURJPY', 'GBPJPY', 'AUDJPY'], 'validation': <function <lambda> at 0x000002CDCA88ECA0>}
[VALIDATE PARAM] Converted to uppercase: XAUUSD -> XAUUSD
[VALIDATE PARAM] Checking valid_values: ['XAUUSD', 'EURUSD', 'GBPUSD', 'USDJPY', 'USDCAD', 'AUDUSD', 'NZDUSD', 'EURJPY', 'GBPJPY', 'AUDJPY']
[VALIDATE PARAM] Value 'XAUUSD' is in valid_values
[VALIDATE PARAM] Validation function passed
[VALIDATE PARAM] Parameter 'symbol' validation PASSED
[VALIDATE] Parameter 'symbol' validation passed
[VALIDATE] Validating param 'timeframe' with value: 1d
[VALIDATE PARAM] Validating 'timeframe' = '1d'
[VALIDATE PARAM] Param definition: {'type': 'string', 'format': 'lowercase', 'valid_values': ['15m', '1h', '1d'], 'validation': <function <lambda> at 0x000002CDCA88EF20>}
[VALIDATE PARAM] Converted to lowercase: 1d -> 1d
[VALIDATE PARAM] Checking valid_values: ['15m', '1h', '1d']
[VALIDATE PARAM] Value '1d' is in valid_values
[VALIDATE PARAM] Validation function passed
[VALIDATE PARAM] Parameter 'timeframe' validation PASSED
[VALIDATE] Parameter 'timeframe' validation passed
[VALIDATE] Validating param 'trend' with value: BEARISH
[VALIDATE PARAM] Validating 'trend' = 'BEARISH'
[VALIDATE PARAM] Param definition: {'type': 'string', 'format': 'uppercase', 'valid_values': ['BULLISH', 'BEARISH', 'NEUTRAL', 'AUTO'], 'validation': <function <lambda> at 0x000002CDCA88F420>}
[VALIDATE PARAM] Converted to uppercase: BEARISH -> BEARISH
[VALIDATE PARAM] Checking valid_values: ['BULLISH', 'BEARISH', 'NEUTRAL', 'AUTO']
[VALIDATE PARAM] Value 'BEARISH' is in valid_values
[VALIDATE PARAM] Validation function passed
[VALIDATE PARAM] Parameter 'trend' validation PASSED
[VALIDATE] Parameter 'trend' validation passed
[VALIDATE] All parameters validated successfully for set_trend
2025-12-12 23:26:23 - src.menu.command_executor - INFO - CALLING HANDLER: set_trend with formatted params: {'symbol': 'XAUUSD', 'timeframe': '1d', 'trend': 'BEARISH'}
SUCCESS: Trend updated: XAUUSD 1d -> BEARISH (MANUAL)
2025-12-12 23:26:25 - src.menu.command_executor - INFO - EXECUTION SUCCESS: set_trend executed successfully for user 2139792302
DEBUG: Parsed param - type: symbol, command: set_trend, value: XAUUSD
🛑 [PARAM SELECTION] START - param_type=symbol, value=XAUUSD, command=set_trend
[PARAM SELECTION] Cleaned value: 'XAUUSD' -> 'XAUUSD'
[PARAM SELECTION] Stored param: symbol=XAUUSD, All params: {'symbol': 'XAUUSD'}
[PARAM SELECTION] Final stored params after preservation: {'symbol': 'XAUUSD'}
🔄 [PARAM SELECTION] More parameters needed. Next param: timeframe
🔄 [PARAM SELECTION] Showing next parameter selection (NOT executing command)
✅ [PARAM SELECTION] Next parameter selection shown. Returning (NO EXECUTION)
DEBUG: Parsed param - type: timeframe, command: set_trend, value: 1h
🛑 [PARAM SELECTION] START - param_type=timeframe, value=1h, command=set_trend
[PARAM SELECTION] Cleaned value: '1h' -> '1h'
[PARAM SELECTION] Stored param: timeframe=1h, All params: {'symbol': 'XAUUSD', 'timeframe': '1h'}
[PARAM SELECTION] Final stored params after preservation: {'symbol': 'XAUUSD', 'timeframe': '1h'}
🔄 [PARAM SELECTION] More parameters needed. Next param: trend
🔄 [PARAM SELECTION] Showing next parameter selection (NOT executing command)
✅ [PARAM SELECTION] Next parameter selection shown. Returning (NO EXECUTION)
DEBUG: Parsed param - type: trend, command: set_trend, value: BEARISH
🛑 [PARAM SELECTION] START - param_type=trend, value=BEARISH, command=set_trend
[PARAM SELECTION] Cleaned value: 'BEARISH' -> 'BEARISH'
[PARAM SELECTION] Stored param: trend=BEARISH, All params: {'symbol': 'XAUUSD', 'timeframe': '1h', 'trend': 'BEARISH'}
[PARAM SELECTION] Final stored params after preservation: {'symbol': 'XAUUSD', 'timeframe': '1h', 'trend': 'BEARISH'}
[PARAM SELECTION] All params collected. Final params: {'symbol': 'XAUUSD', 'timeframe': '1h', 'trend': 'BEARISH'}, showing confirmation
✅ [PARAM SELECTION] All parameters collected - SHOWING CONFIRMATION SCREEN
🛑 [PARAM SELECTION] CRITICAL: About to show confirmation (NOT executing command)
🛑 [CONFIRMATION] START - Showing confirmation for command: set_trend
[CONFIRMATION] Showing confirmation for set_trend with params: {'symbol': 'XAUUSD', 'timeframe': '1h', 'trend': 'BEARISH'}
[CONFIRMATION] Confirm button callback: execute_set_trend
[CONFIRMATION] About to display confirmation screen (NOT executing command)
[CONFIRMATION] Confirmation screen displayed. Result: True
✅ [CONFIRMATION] Confirmation screen shown successfully
🛑 [CONFIRMATION] END - Waiting for user to click 'Confirm' button. NO EXECUTION YET.
✅ [PARAM SELECTION] Confirmation screen shown. Returning (NO EXECUTION)
🛑 [PARAM SELECTION] END - Command will ONLY execute when user clicks 'Confirm' button
2025-12-12 23:27:06 - src.menu.command_executor - INFO - EXECUTING: set_trend with params {'symbol': 'XAUUSD', 'timeframe': '1h', 'trend': 'BEARISH'} for user 2139792302
[VALIDATE] Validating command 'set_trend' with params: {'symbol': 'XAUUSD', 'timeframe': '1h', 'trend': 'BEARISH'}
[VALIDATE] Required params for set_trend: ['symbol', 'timeframe', 'trend']
[VALIDATE] Validating param 'symbol' with value: XAUUSD
[VALIDATE PARAM] Validating 'symbol' = 'XAUUSD'
[VALIDATE PARAM] Param definition: {'type': 'string', 'format': 'uppercase', 'valid_values': ['XAUUSD', 'EURUSD', 'GBPUSD', 'USDJPY', 'USDCAD', 'AUDUSD', 'NZDUSD', 'EURJPY', 'GBPJPY', 'AUDJPY'], 'validation': <function <lambda> at 0x000002CDCA88ECA0>}
[VALIDATE PARAM] Converted to uppercase: XAUUSD -> XAUUSD
[VALIDATE PARAM] Checking valid_values: ['XAUUSD', 'EURUSD', 'GBPUSD', 'USDJPY', 'USDCAD', 'AUDUSD', 'NZDUSD', 'EURJPY', 'GBPJPY', 'AUDJPY']
[VALIDATE PARAM] Value 'XAUUSD' is in valid_values
[VALIDATE PARAM] Validation function passed
[VALIDATE PARAM] Parameter 'symbol' validation PASSED
[VALIDATE] Parameter 'symbol' validation passed
[VALIDATE] Validating param 'timeframe' with value: 1h
[VALIDATE PARAM] Validating 'timeframe' = '1h'
[VALIDATE PARAM] Param definition: {'type': 'string', 'format': 'lowercase', 'valid_values': ['15m', '1h', '1d'], 'validation': <function <lambda> at 0x000002CDCA88EF20>}
[VALIDATE PARAM] Converted to lowercase: 1h -> 1h
[VALIDATE PARAM] Checking valid_values: ['15m', '1h', '1d']
[VALIDATE PARAM] Value '1h' is in valid_values
[VALIDATE PARAM] Validation function passed
[VALIDATE PARAM] Parameter 'timeframe' validation PASSED
[VALIDATE] Parameter 'timeframe' validation passed
[VALIDATE] Validating param 'trend' with value: BEARISH
[VALIDATE PARAM] Validating 'trend' = 'BEARISH'
[VALIDATE PARAM] Param definition: {'type': 'string', 'format': 'uppercase', 'valid_values': ['BULLISH', 'BEARISH', 'NEUTRAL', 'AUTO'], 'validation': <function <lambda> at 0x000002CDCA88F420>}
[VALIDATE PARAM] Converted to uppercase: BEARISH -> BEARISH
[VALIDATE PARAM] Checking valid_values: ['BULLISH', 'BEARISH', 'NEUTRAL', 'AUTO']
[VALIDATE PARAM] Value 'BEARISH' is in valid_values
[VALIDATE PARAM] Validation function passed
[VALIDATE PARAM] Parameter 'trend' validation PASSED
[VALIDATE] Parameter 'trend' validation passed
[VALIDATE] All parameters validated successfully for set_trend
2025-12-12 23:27:07 - src.menu.command_executor - INFO - CALLING HANDLER: set_trend with formatted params: {'symbol': 'XAUUSD', 'timeframe': '1h', 'trend': 'BEARISH'}
INFO: Trend already BEARISH (MANUAL) for XAUUSD 1h, ignoring update
2025-12-12 23:27:08 - src.menu.command_executor - INFO - EXECUTION SUCCESS: set_trend executed successfully for user 2139792302
DEBUG: Parsed param - type: symbol, command: set_trend, value: XAUUSD
🛑 [PARAM SELECTION] START - param_type=symbol, value=XAUUSD, command=set_trend
[PARAM SELECTION] Cleaned value: 'XAUUSD' -> 'XAUUSD'
[PARAM SELECTION] Stored param: symbol=XAUUSD, All params: {'symbol': 'XAUUSD'}
[PARAM SELECTION] Final stored params after preservation: {'symbol': 'XAUUSD'}
🔄 [PARAM SELECTION] More parameters needed. Next param: timeframe
🔄 [PARAM SELECTION] Showing next parameter selection (NOT executing command)
✅ [PARAM SELECTION] Next parameter selection shown. Returning (NO EXECUTION)
DEBUG: Parsed param - type: timeframe, command: set_trend, value: 15m
🛑 [PARAM SELECTION] START - param_type=timeframe, value=15m, command=set_trend
[PARAM SELECTION] Cleaned value: '15m' -> '15m'
[PARAM SELECTION] Stored param: timeframe=15m, All params: {'symbol': 'XAUUSD', 'timeframe': '15m'}
[PARAM SELECTION] Final stored params after preservation: {'symbol': 'XAUUSD', 'timeframe': '15m'}
🔄 [PARAM SELECTION] More parameters needed. Next param: trend
🔄 [PARAM SELECTION] Showing next parameter selection (NOT executing command)
✅ [PARAM SELECTION] Next parameter selection shown. Returning (NO EXECUTION)
DEBUG: Parsed param - type: trend, command: set_trend, value: BEARISH
🛑 [PARAM SELECTION] START - param_type=trend, value=BEARISH, command=set_trend
[PARAM SELECTION] Cleaned value: 'BEARISH' -> 'BEARISH'
[PARAM SELECTION] Stored param: trend=BEARISH, All params: {'symbol': 'XAUUSD', 'timeframe': '15m', 'trend': 'BEARISH'}
[PARAM SELECTION] Final stored params after preservation: {'symbol': 'XAUUSD', 'timeframe': '15m', 'trend': 'BEARISH'}
[PARAM SELECTION] All params collected. Final params: {'symbol': 'XAUUSD', 'timeframe': '15m', 'trend': 'BEARISH'}, showing confirmation
✅ [PARAM SELECTION] All parameters collected - SHOWING CONFIRMATION SCREEN
🛑 [PARAM SELECTION] CRITICAL: About to show confirmation (NOT executing command)
🛑 [CONFIRMATION] START - Showing confirmation for command: set_trend
[CONFIRMATION] Showing confirmation for set_trend with params: {'symbol': 'XAUUSD', 'timeframe': '15m', 'trend': 'BEARISH'}
[CONFIRMATION] Confirm button callback: execute_set_trend
[CONFIRMATION] About to display confirmation screen (NOT executing command)
[CONFIRMATION] Confirmation screen displayed. Result: True
✅ [CONFIRMATION] Confirmation screen shown successfully
🛑 [CONFIRMATION] END - Waiting for user to click 'Confirm' button. NO EXECUTION YET.
✅ [PARAM SELECTION] Confirmation screen shown. Returning (NO EXECUTION)
🛑 [PARAM SELECTION] END - Command will ONLY execute when user clicks 'Confirm' button
2025-12-12 23:27:47 - src.menu.command_executor - INFO - EXECUTING: set_trend with params {'symbol': 'XAUUSD', 'timeframe': '15m', 'trend': 'BEARISH'} for user 2139792302
[VALIDATE] Validating command 'set_trend' with params: {'symbol': 'XAUUSD', 'timeframe': '15m', 'trend': 'BEARISH'}
[VALIDATE] Required params for set_trend: ['symbol', 'timeframe', 'trend']
[VALIDATE] Validating param 'symbol' with value: XAUUSD
[VALIDATE PARAM] Validating 'symbol' = 'XAUUSD'
[VALIDATE PARAM] Param definition: {'type': 'string', 'format': 'uppercase', 'valid_values': ['XAUUSD', 'EURUSD', 'GBPUSD', 'USDJPY', 'USDCAD', 'AUDUSD', 'NZDUSD', 'EURJPY', 'GBPJPY', 'AUDJPY'], 'validation': <function <lambda> at 0x000002CDCA88ECA0>}
[VALIDATE PARAM] Converted to uppercase: XAUUSD -> XAUUSD
[VALIDATE PARAM] Checking valid_values: ['XAUUSD', 'EURUSD', 'GBPUSD', 'USDJPY', 'USDCAD', 'AUDUSD', 'NZDUSD', 'EURJPY', 'GBPJPY', 'AUDJPY']
[VALIDATE PARAM] Value 'XAUUSD' is in valid_values
[VALIDATE PARAM] Validation function passed
[VALIDATE PARAM] Parameter 'symbol' validation PASSED
[VALIDATE] Parameter 'symbol' validation passed
[VALIDATE] Validating param 'timeframe' with value: 15m
[VALIDATE PARAM] Validating 'timeframe' = '15m'
[VALIDATE PARAM] Param definition: {'type': 'string', 'format': 'lowercase', 'valid_values': ['15m', '1h', '1d'], 'validation': <function <lambda> at 0x000002CDCA88EF20>}
[VALIDATE PARAM] Converted to lowercase: 15m -> 15m
[VALIDATE PARAM] Checking valid_values: ['15m', '1h', '1d']
[VALIDATE PARAM] Value '15m' is in valid_values
[VALIDATE PARAM] Validation function passed
[VALIDATE PARAM] Parameter 'timeframe' validation PASSED
[VALIDATE] Parameter 'timeframe' validation passed
[VALIDATE] Validating param 'trend' with value: BEARISH
[VALIDATE PARAM] Validating 'trend' = 'BEARISH'
[VALIDATE PARAM] Param definition: {'type': 'string', 'format': 'uppercase', 'valid_values': ['BULLISH', 'BEARISH', 'NEUTRAL', 'AUTO'], 'validation': <function <lambda> at 0x000002CDCA88F420>}
[VALIDATE PARAM] Converted to uppercase: BEARISH -> BEARISH
[VALIDATE PARAM] Checking valid_values: ['BULLISH', 'BEARISH', 'NEUTRAL', 'AUTO']
[VALIDATE PARAM] Value 'BEARISH' is in valid_values
[VALIDATE PARAM] Validation function passed
[VALIDATE PARAM] Parameter 'trend' validation PASSED
[VALIDATE] Parameter 'trend' validation passed
[VALIDATE] All parameters validated successfully for set_trend
2025-12-12 23:27:47 - src.menu.command_executor - INFO - CALLING HANDLER: set_trend with formatted params: {'symbol': 'XAUUSD', 'timeframe': '15m', 'trend': 'BEARISH'}
SUCCESS: Trend updated: XAUUSD 15m -> BEARISH (MANUAL)
2025-12-12 23:27:48 - src.menu.command_executor - INFO - EXECUTION SUCCESS: set_trend executed successfully for user 2139792302
DEBUG: Parsed param - type: symbol, command: set_auto, value: XAUUSD
🛑 [PARAM SELECTION] START - param_type=symbol, value=XAUUSD, command=set_auto
[PARAM SELECTION] Cleaned value: 'XAUUSD' -> 'XAUUSD'
[PARAM SELECTION] Stored param: symbol=XAUUSD, All params: {'symbol': 'XAUUSD'}
[PARAM SELECTION] Final stored params after preservation: {'symbol': 'XAUUSD'}
🔄 [PARAM SELECTION] More parameters needed. Next param: timeframe
🔄 [PARAM SELECTION] Showing next parameter selection (NOT executing command)
✅ [PARAM SELECTION] Next parameter selection shown. Returning (NO EXECUTION)
DEBUG: Parsed param - type: timeframe, command: set_auto, value: 1d
🛑 [PARAM SELECTION] START - param_type=timeframe, value=1d, command=set_auto
[PARAM SELECTION] Cleaned value: '1d' -> '1d'
[PARAM SELECTION] Stored param: timeframe=1d, All params: {'symbol': 'XAUUSD', 'timeframe': '1d'}
[PARAM SELECTION] Final stored params after preservation: {'symbol': 'XAUUSD', 'timeframe': '1d'}
[PARAM SELECTION] All params collected. Final params: {'symbol': 'XAUUSD', 'timeframe': '1d'}, showing confirmation
✅ [PARAM SELECTION] All parameters collected - SHOWING CONFIRMATION SCREEN
🛑 [PARAM SELECTION] CRITICAL: About to show confirmation (NOT executing command)
🛑 [CONFIRMATION] START - Showing confirmation for command: set_auto
[CONFIRMATION] Showing confirmation for set_auto with params: {'symbol': 'XAUUSD', 'timeframe': '1d'}
[CONFIRMATION] Confirm button callback: execute_set_auto
[CONFIRMATION] About to display confirmation screen (NOT executing command)
[CONFIRMATION] Confirmation screen displayed. Result: True
✅ [CONFIRMATION] Confirmation screen shown successfully
🛑 [CONFIRMATION] END - Waiting for user to click 'Confirm' button. NO EXECUTION YET.
✅ [PARAM SELECTION] Confirmation screen shown. Returning (NO EXECUTION)
🛑 [PARAM SELECTION] END - Command will ONLY execute when user clicks 'Confirm' button
2025-12-12 23:28:23 - src.menu.command_executor - INFO - EXECUTING: set_auto with params {'symbol': 'XAUUSD', 'timeframe': '1d'} for user 2139792302
[VALIDATE] Validating command 'set_auto' with params: {'symbol': 'XAUUSD', 'timeframe': '1d'}
[VALIDATE] Required params for set_auto: ['symbol', 'timeframe']
[VALIDATE] Validating param 'symbol' with value: XAUUSD
[VALIDATE PARAM] Validating 'symbol' = 'XAUUSD'
[VALIDATE PARAM] Param definition: {'type': 'string', 'format': 'uppercase', 'valid_values': ['XAUUSD', 'EURUSD', 'GBPUSD', 'USDJPY', 'USDCAD', 'AUDUSD', 'NZDUSD', 'EURJPY', 'GBPJPY', 'AUDJPY'], 'validation': <function <lambda> at 0x000002CDCA88ECA0>}
[VALIDATE PARAM] Converted to uppercase: XAUUSD -> XAUUSD
[VALIDATE PARAM] Checking valid_values: ['XAUUSD', 'EURUSD', 'GBPUSD', 'USDJPY', 'USDCAD', 'AUDUSD', 'NZDUSD', 'EURJPY', 'GBPJPY', 'AUDJPY']
[VALIDATE PARAM] Value 'XAUUSD' is in valid_values
[VALIDATE PARAM] Validation function passed
[VALIDATE PARAM] Parameter 'symbol' validation PASSED
[VALIDATE] Parameter 'symbol' validation passed
[VALIDATE] Validating param 'timeframe' with value: 1d
[VALIDATE PARAM] Validating 'timeframe' = '1d'
[VALIDATE PARAM] Param definition: {'type': 'string', 'format': 'lowercase', 'valid_values': ['15m', '1h', '1d'], 'validation': <function <lambda> at 0x000002CDCA88EF20>}
[VALIDATE PARAM] Converted to lowercase: 1d -> 1d
[VALIDATE PARAM] Checking valid_values: ['15m', '1h', '1d']
[VALIDATE PARAM] Value '1d' is in valid_values
[VALIDATE PARAM] Validation function passed
[VALIDATE PARAM] Parameter 'timeframe' validation PASSED
[VALIDATE] Parameter 'timeframe' validation passed
[VALIDATE] All parameters validated successfully for set_auto
2025-12-12 23:28:23 - src.menu.command_executor - INFO - CALLING HANDLER: set_auto with formatted params: {'symbol': 'XAUUSD', 'timeframe': '1d'}
SUCCESS: Mode set to AUTO for XAUUSD 1d
2025-12-12 23:28:25 - src.menu.command_executor - INFO - EXECUTION SUCCESS: set_auto executed successfully for user 2139792302
DEBUG: Parsed param - type: symbol, command: set_auto, value: XAUUSD
🛑 [PARAM SELECTION] START - param_type=symbol, value=XAUUSD, command=set_auto
[PARAM SELECTION] Cleaned value: 'XAUUSD' -> 'XAUUSD'
[PARAM SELECTION] Stored param: symbol=XAUUSD, All params: {'symbol': 'XAUUSD'}
[PARAM SELECTION] Final stored params after preservation: {'symbol': 'XAUUSD'}
🔄 [PARAM SELECTION] More parameters needed. Next param: timeframe
🔄 [PARAM SELECTION] Showing next parameter selection (NOT executing command)
✅ [PARAM SELECTION] Next parameter selection shown. Returning (NO EXECUTION)
DEBUG: Parsed param - type: timeframe, command: set_auto, value: 1h
🛑 [PARAM SELECTION] START - param_type=timeframe, value=1h, command=set_auto
[PARAM SELECTION] Cleaned value: '1h' -> '1h'
[PARAM SELECTION] Stored param: timeframe=1h, All params: {'symbol': 'XAUUSD', 'timeframe': '1h'}
[PARAM SELECTION] Final stored params after preservation: {'symbol': 'XAUUSD', 'timeframe': '1h'}
[PARAM SELECTION] All params collected. Final params: {'symbol': 'XAUUSD', 'timeframe': '1h'}, showing confirmation
✅ [PARAM SELECTION] All parameters collected - SHOWING CONFIRMATION SCREEN
🛑 [PARAM SELECTION] CRITICAL: About to show confirmation (NOT executing command)
🛑 [CONFIRMATION] START - Showing confirmation for command: set_auto
[CONFIRMATION] Showing confirmation for set_auto with params: {'symbol': 'XAUUSD', 'timeframe': '1h'}
[CONFIRMATION] Confirm button callback: execute_set_auto
[CONFIRMATION] About to display confirmation screen (NOT executing command)
[CONFIRMATION] Confirmation screen displayed. Result: True
✅ [CONFIRMATION] Confirmation screen shown successfully
🛑 [CONFIRMATION] END - Waiting for user to click 'Confirm' button. NO EXECUTION YET.
✅ [PARAM SELECTION] Confirmation screen shown. Returning (NO EXECUTION)
🛑 [PARAM SELECTION] END - Command will ONLY execute when user clicks 'Confirm' button
2025-12-12 23:28:58 - src.menu.command_executor - INFO - EXECUTING: set_auto with params {'symbol': 'XAUUSD', 'timeframe': '1h'} for user 2139792302
[VALIDATE] Validating command 'set_auto' with params: {'symbol': 'XAUUSD', 'timeframe': '1h'}
[VALIDATE] Required params for set_auto: ['symbol', 'timeframe']
[VALIDATE] Validating param 'symbol' with value: XAUUSD
[VALIDATE PARAM] Validating 'symbol' = 'XAUUSD'
[VALIDATE PARAM] Param definition: {'type': 'string', 'format': 'uppercase', 'valid_values': ['XAUUSD', 'EURUSD', 'GBPUSD', 'USDJPY', 'USDCAD', 'AUDUSD', 'NZDUSD', 'EURJPY', 'GBPJPY', 'AUDJPY'], 'validation': <function <lambda> at 0x000002CDCA88ECA0>}
[VALIDATE PARAM] Converted to uppercase: XAUUSD -> XAUUSD
[VALIDATE PARAM] Checking valid_values: ['XAUUSD', 'EURUSD', 'GBPUSD', 'USDJPY', 'USDCAD', 'AUDUSD', 'NZDUSD', 'EURJPY', 'GBPJPY', 'AUDJPY']
[VALIDATE PARAM] Value 'XAUUSD' is in valid_values
[VALIDATE PARAM] Validation function passed
[VALIDATE PARAM] Parameter 'symbol' validation PASSED
[VALIDATE] Parameter 'symbol' validation passed
[VALIDATE] Validating param 'timeframe' with value: 1h
[VALIDATE PARAM] Validating 'timeframe' = '1h'
[VALIDATE PARAM] Param definition: {'type': 'string', 'format': 'lowercase', 'valid_values': ['15m', '1h', '1d'], 'validation': <function <lambda> at 0x000002CDCA88EF20>}
[VALIDATE PARAM] Converted to lowercase: 1h -> 1h
[VALIDATE PARAM] Checking valid_values: ['15m', '1h', '1d']
[VALIDATE PARAM] Value '1h' is in valid_values
[VALIDATE PARAM] Validation function passed
[VALIDATE PARAM] Parameter 'timeframe' validation PASSED
[VALIDATE] Parameter 'timeframe' validation passed
[VALIDATE] All parameters validated successfully for set_auto
2025-12-12 23:28:58 - src.menu.command_executor - INFO - CALLING HANDLER: set_auto with formatted params: {'symbol': 'XAUUSD', 'timeframe': '1h'}
SUCCESS: Mode set to AUTO for XAUUSD 1h
2025-12-12 23:29:00 - src.menu.command_executor - INFO - EXECUTION SUCCESS: set_auto executed successfully for user 2139792302
DEBUG: Parsed param - type: symbol, command: set_auto, value: XAUUSD
🛑 [PARAM SELECTION] START - param_type=symbol, value=XAUUSD, command=set_auto
[PARAM SELECTION] Cleaned value: 'XAUUSD' -> 'XAUUSD'
[PARAM SELECTION] Stored param: symbol=XAUUSD, All params: {'symbol': 'XAUUSD'}
[PARAM SELECTION] Final stored params after preservation: {'symbol': 'XAUUSD'}
🔄 [PARAM SELECTION] More parameters needed. Next param: timeframe
🔄 [PARAM SELECTION] Showing next parameter selection (NOT executing command)
✅ [PARAM SELECTION] Next parameter selection shown. Returning (NO EXECUTION)
DEBUG: Parsed param - type: timeframe, command: set_auto, value: 15m
🛑 [PARAM SELECTION] START - param_type=timeframe, value=15m, command=set_auto
[PARAM SELECTION] Cleaned value: '15m' -> '15m'
[PARAM SELECTION] Stored param: timeframe=15m, All params: {'symbol': 'XAUUSD', 'timeframe': '15m'}
[PARAM SELECTION] Final stored params after preservation: {'symbol': 'XAUUSD', 'timeframe': '15m'}
[PARAM SELECTION] All params collected. Final params: {'symbol': 'XAUUSD', 'timeframe': '15m'}, showing confirmation
✅ [PARAM SELECTION] All parameters collected - SHOWING CONFIRMATION SCREEN
🛑 [PARAM SELECTION] CRITICAL: About to show confirmation (NOT executing command)
🛑 [CONFIRMATION] START - Showing confirmation for command: set_auto
[CONFIRMATION] Showing confirmation for set_auto with params: {'symbol': 'XAUUSD', 'timeframe': '15m'}
[CONFIRMATION] Confirm button callback: execute_set_auto
[CONFIRMATION] About to display confirmation screen (NOT executing command)
[CONFIRMATION] Confirmation screen displayed. Result: True
✅ [CONFIRMATION] Confirmation screen shown successfully
🛑 [CONFIRMATION] END - Waiting for user to click 'Confirm' button. NO EXECUTION YET.
✅ [PARAM SELECTION] Confirmation screen shown. Returning (NO EXECUTION)
🛑 [PARAM SELECTION] END - Command will ONLY execute when user clicks 'Confirm' button
2025-12-12 23:29:34 - src.menu.command_executor - INFO - EXECUTING: set_auto with params {'symbol': 'XAUUSD', 'timeframe': '15m'} for user 2139792302
[VALIDATE] Validating command 'set_auto' with params: {'symbol': 'XAUUSD', 'timeframe': '15m'}
[VALIDATE] Required params for set_auto: ['symbol', 'timeframe']
[VALIDATE] Validating param 'symbol' with value: XAUUSD
[VALIDATE PARAM] Validating 'symbol' = 'XAUUSD'
[VALIDATE PARAM] Param definition: {'type': 'string', 'format': 'uppercase', 'valid_values': ['XAUUSD', 'EURUSD', 'GBPUSD', 'USDJPY', 'USDCAD', 'AUDUSD', 'NZDUSD', 'EURJPY', 'GBPJPY', 'AUDJPY'], 'validation': <function <lambda> at 0x000002CDCA88ECA0>}
[VALIDATE PARAM] Converted to uppercase: XAUUSD -> XAUUSD
[VALIDATE PARAM] Checking valid_values: ['XAUUSD', 'EURUSD', 'GBPUSD', 'USDJPY', 'USDCAD', 'AUDUSD', 'NZDUSD', 'EURJPY', 'GBPJPY', 'AUDJPY']
[VALIDATE PARAM] Value 'XAUUSD' is in valid_values
[VALIDATE PARAM] Validation function passed
[VALIDATE PARAM] Parameter 'symbol' validation PASSED
[VALIDATE] Parameter 'symbol' validation passed
[VALIDATE] Validating param 'timeframe' with value: 15m
[VALIDATE PARAM] Validating 'timeframe' = '15m'
[VALIDATE PARAM] Param definition: {'type': 'string', 'format': 'lowercase', 'valid_values': ['15m', '1h', '1d'], 'validation': <function <lambda> at 0x000002CDCA88EF20>}
[VALIDATE PARAM] Converted to lowercase: 15m -> 15m
[VALIDATE PARAM] Checking valid_values: ['15m', '1h', '1d']
[VALIDATE PARAM] Value '15m' is in valid_values
[VALIDATE PARAM] Validation function passed
[VALIDATE PARAM] Parameter 'timeframe' validation PASSED
[VALIDATE] Parameter 'timeframe' validation passed
[VALIDATE] All parameters validated successfully for set_auto
2025-12-12 23:29:34 - src.menu.command_executor - INFO - CALLING HANDLER: set_auto with formatted params: {'symbol': 'XAUUSD', 'timeframe': '15m'}
SUCCESS: Mode set to AUTO for XAUUSD 15m
2025-12-12 23:29:35 - src.menu.command_executor - INFO - EXECUTION SUCCESS: set_auto executed successfully for user 2139792302
[MENU EXECUTION] Empty params detected, attempting recovery...
2025-12-12 23:29:49 - src.menu.command_executor - INFO - EXECUTING: status with params {} for user 2139792302
[VALIDATE] Validating command 'status' with params: {}
[VALIDATE] Required params for status: []
[VALIDATE] All parameters validated successfully for status
2025-12-12 23:29:49 - src.menu.command_executor - INFO - CALLING HANDLER: status with formatted params: {}
2025-12-12 23:29:51 - src.menu.command_executor - INFO - EXECUTION SUCCESS: status executed successfully for user 2139792302
←[32mINFO←[0m:     34.212.75.30:0 - "←[1mPOST / HTTP/1.1←[0m" ←[31m404 Not Found←[0m
←[32mINFO←[0m:     52.32.178.7:0 - "←[1mPOST / HTTP/1.1←[0m" ←[31m404 Not Found←[0m
←[32mINFO←[0m:     34.212.75.30:0 - "←[1mPOST / HTTP/1.1←[0m" ←[31m404 Not Found←[0m
←[32mINFO←[0m:     52.32.178.7:0 - "←[1mPOST / HTTP/1.1←[0m" ←[31m404 Not Found←[0m
Webhook received: {
  "type": "trend",
  "symbol": "XAUUSD",
  "signal": "bull",
  "tf": "15m",
  "price": 4303.905,
  "strategy": "ZepixPremium"
}
ALERT: Received alert: {'type': 'trend', 'symbol': 'XAUUSD', 'signal': 'bull', 'tf': '15m', 'price': 4303.905, 'strategy': 'ZepixPremium'}
SUCCESS: Alert validation successful
SUCCESS: Trend updated: XAUUSD 15m -> BULLISH (AUTO)
←[32mINFO←[0m:     34.212.75.30:0 - "←[1mPOST /webhook HTTP/1.1←[0m" ←[32m200 OK←[0m
[MENU EXECUTION] Empty params detected, attempting recovery...
2025-12-12 23:45:51 - src.menu.command_executor - INFO - EXECUTING: trend_matrix with params {} for user 2139792302
[VALIDATE] Validating command 'trend_matrix' with params: {}
[VALIDATE] Required params for trend_matrix: []
[VALIDATE] All parameters validated successfully for trend_matrix
2025-12-12 23:45:51 - src.menu.command_executor - INFO - CALLING HANDLER: trend_matrix with formatted params: {}
SUCCESS: Loaded trends from C:\Users\Ansh Shivaay Gupta\Downloads\ZepixTradingBot-old-v2-main\ZepixTradingBot-old-v2-main\config\timeframe_trends.json
DEBUG: Loaded MANUAL trend for AUDUSD 1h: BULLISH
DEBUG: Total manual trends loaded: 1
2025-12-12 23:45:53 - src.menu.command_executor - INFO - EXECUTION SUCCESS: trend_matrix executed successfully for user 2139792302
Webhook received: {
  "type": "trend",
  "symbol": "XAUUSD",
  "signal": "bull",
  "tf": "15m",
  "price": 4303.125,
  "strategy": "ZepixPremium"
}
ALERT: Received alert: {'type': 'trend', 'symbol': 'XAUUSD', 'signal': 'bull', 'tf': '15m', 'price': 4303.125, 'strategy': 'ZepixPremium'}
INFO: Duplicate trend detected - XAUUSD 15M is already BULLISH
ERROR: Duplicate alert detected
INFO: Sent duplicate notification to Telegram
←[32mINFO←[0m:     52.32.178.7:0 - "←[1mPOST /webhook HTTP/1.1←[0m" ←[32m200 OK←[0m
Webhook received: {
  "type": "trend",
  "symbol": "XAUUSD",
  "signal": "bear",
  "tf": "15m",
  "price": 4303.425,
  "strategy": "ZepixPremium"
}
ALERT: Received alert: {'type': 'trend', 'symbol': 'XAUUSD', 'signal': 'bear', 'tf': '15m', 'price': 4303.425, 'strategy': 'ZepixPremium'}
SUCCESS: Alert validation successful
SUCCESS: Trend updated: XAUUSD 15m -> BEARISH (AUTO)
←[32mINFO←[0m:     34.212.75.30:0 - "←[1mPOST /webhook HTTP/1.1←[0m" ←[32m200 OK←[0m
Webhook received: {
  "type": "trend",
  "symbol": "XAUUSD",
  "signal": "bear",
  "tf": "15m",
  "price": 4302.42,
  "strategy": "ZepixPremium"
}
ALERT: Received alert: {'type': 'trend', 'symbol': 'XAUUSD', 'signal': 'bear', 'tf': '15m', 'price': 4302.42, 'strategy': 'ZepixPremium'}
INFO: Duplicate trend detected - XAUUSD 15M is already BEARISH
ERROR: Duplicate alert detected
INFO: Sent duplicate notification to Telegram
←[32mINFO←[0m:     34.212.75.30:0 - "←[1mPOST /webhook HTTP/1.1←[0m" ←[32m200 OK←[0m
Webhook received: {
  "type": "entry",
  "symbol": "XAUUSD",
  "signal": "sell",
  "tf": "5m",
  "price": 4302.06,
  "strategy": "ZepixPremium"
}
ALERT: Received alert: {'type': 'entry', 'symbol': 'XAUUSD', 'signal': 'sell', 'tf': '5m', 'price': 4302.06, 'strategy': 'ZepixPremium'}
SUCCESS: Alert validation successful
[2025-12-12 23:48:23] 🔔 Processing entry alert | Symbol: XAUUSD, TF: 5m
[2025-12-12 23:48:23] 🔔 Trade execution starting | Symbol: XAUUSD, Direction: BEARISH
WARNING: Dual order error: Risk validation failed: Daily loss cap exceeded: $150.00 > $100.0
←[32mINFO←[0m:     34.212.75.30:0 - "←[1mPOST /webhook HTTP/1.1←[0m" ←[32m200 OK←[0m
