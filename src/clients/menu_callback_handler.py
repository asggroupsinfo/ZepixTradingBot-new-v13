"""
Menu Callback Handler
Handles all menu navigation callbacks for Telegram bot
Separated for modularity and easier maintenance
"""

import logging

logger = logging.getLogger(__name__)

class MenuCallbackHandler:
    """Handles menu-related callback queries"""
    
    def __init__(self, telegram_bot):
        self.bot = telegram_bot
        self.menu_manager = telegram_bot.menu_manager
        self.fine_tune_handler = None
    
    def handle_menu_callback(self, callback_data, user_id, message_id):
        """
        Handle menu navigation callbacks
        
        Args:
            callback_data: The callback data from button click
            user_id: Telegram user ID
            message_id: Message ID to edit
            
        Returns:
            True if handled, False if not a menu callback
        """
        # Main menu
        if callback_data == "menu_main":
            self.menu_manager.show_main_menu(user_id, message_id)
            return True
        
        # Fine-Tune menu - Special handling (two variants)
        elif callback_data == "menu_fine_tune" or callback_data == "fine_tune_menu":
            return self._handle_fine_tune_menu(user_id, message_id)
        
        # Re-entry menu - New handler
        elif callback_data == "menu_reentry":
            return self._handle_reentry_menu(user_id, message_id)
        
        # Profit booking menu - New handler
        elif callback_data == "menu_profit":
            return self._handle_profit_booking_menu(user_id, message_id)
        
        # Profit booking toggles (FIX: these were incorrectly going to reentry handler)
        elif callback_data in ["toggle_profit_sl_hunt", "toggle_profit_protection"]:
            return self._handle_profit_booking_toggle(callback_data, user_id, message_id)
        
        # Re-entry toggles
        elif callback_data.startswith("toggle_"):
            return self._handle_reentry_toggle(callback_data, user_id, message_id)
        
        # Profit SL mode selector
        elif callback_data.startswith("profit_sl_mode_"):
            return self._handle_profit_sl_mode(callback_data, user_id, message_id)
        
        # Recovery windows editing
        elif callback_data.startswith("rw_") or callback_data == "ft_recovery_windows_edit":
            return self._handle_recovery_windows(callback_data, user_id, message_id)
        
        # Re-entry status view
        elif callback_data == "reentry_view_status":
            return self._handle_reentry_status(user_id, message_id)
        
        # Re-entry advanced settings
        elif callback_data == "reentry_advanced":
            return self._handle_reentry_advanced(user_id, message_id)
        
        # Advanced settings parameter editors
        elif callback_data.startswith("adv_"):
            return self._handle_advanced_settings_callback(callback_data, user_id, message_id)
        
        # Parameter value setters
        elif callback_data.startswith("set_"):
            return self._handle_parameter_setter(callback_data, user_id, message_id)
        
        # All other category menus
        elif callback_data.startswith("menu_"):
            category = callback_data.replace("menu_", "")
            self.menu_manager.show_category_menu(user_id, category, message_id)
            return True
        
        return False

    
    def _handle_fine_tune_menu(self, user_id, message_id=None):
        """Handle Fine-Tune menu specifically"""
        # Get or initialize fine_tune_handler
        if not self.fine_tune_handler and hasattr(self.bot, 'fine_tune_handler'):
            self.fine_tune_handler = self.bot.fine_tune_handler
        
        # Initialize if needed
        if not self.fine_tune_handler:
            if hasattr(self.bot, '_initialize_fine_tune_handler'):
                self.bot._initialize_fine_tune_handler()
                self.fine_tune_handler = getattr(self.bot, 'fine_tune_handler', None)
        
        # Show menu
        if self.fine_tune_handler:
            self.fine_tune_handler.show_fine_tune_menu(user_id, message_id)
            return True
        else:
            self.bot.send_message("❌ Fine-Tune system not initialized. Please restart bot.")
            return True
    
    def handle_action_callback(self, callback_data, user_id, message_id):
        """
        Handle quick action callbacks
        
        Args:
            callback_data: The callback data from button click
            user_id: Telegram user ID  
            message_id: Message ID to edit
            
        Returns:
            True if handled, False if not an action callback
        """
        if callback_data == "action_trades":
            if hasattr(self.bot, 'handle_trades'):
                self.bot.handle_trades({"message_id": message_id})
            return True
        
        elif callback_data == "action_performance":
            if hasattr(self.bot, 'handle_performance'):
                self.bot.handle_performance({"message_id": message_id})
            return True
        
        elif callback_data == "action_pause_resume":
            if hasattr(self.bot, 'trading_engine') and self.bot.trading_engine:
                self.bot.trading_engine.is_paused = not self.bot.trading_engine.is_paused
                status = "PAUSED ⏸️" if self.bot.trading_engine.is_paused else "RESUMED ▶️"
                self.bot.send_message(f"✅ Trading {status}")
            return True
        
        elif callback_data == "action_dashboard":
            if hasattr(self.bot, 'handle_dashboard'):
                self.bot.handle_dashboard({"message_id": message_id})
            return True
        
        elif callback_data == "action_help":
            if hasattr(self.bot, '_show_help_menu'):
                self.bot._show_help_menu(user_id, message_id)
            return True
        
        return False
    
    # ==================== NEW HANDLER METHODS ====================
    
    def _handle_reentry_menu(self, user_id, message_id=None):
        """Handle Re-entry System menu"""
        if not hasattr(self.bot, 'reentry_menu_handler') or not self.bot.reentry_menu_handler:
            self.bot.send_message("❌ Re-entry menu not initialized. Please restart bot.")
            return True
        
        self.bot.reentry_menu_handler.show_reentry_menu(user_id, message_id)
        return True
    
    def _handle_profit_booking_menu(self, user_id, message_id=None):
        """Handle Profit Booking menu"""
        if not hasattr(self.bot, 'profit_booking_menu_handler') or not self.bot.profit_booking_menu_handler:
            self.bot.send_message("❌ Profit Booking menu not initialized. Please restart bot.")
            return True
        
        self.bot.profit_booking_menu_handler.show_profit_booking_menu(user_id, message_id)
        return True
    
    def _handle_reentry_toggle(self, callback_data, user_id, message_id):
        """Handle re-entry toggle callbacks"""
        if not hasattr(self.bot, 'reentry_menu_handler') or not self.bot.reentry_menu_handler:
            self.bot.send_message("❌ Re-entry menu not initialized.")
            return True
        
        self.bot.reentry_menu_handler.handle_toggle_callback(callback_data, user_id, message_id)
        return True
    
    def _handle_profit_sl_mode(self, callback_data, user_id, message_id):
        """Handle profit SL mode change"""
        if not hasattr(self.bot, 'profit_booking_menu_handler') or not self.bot.profit_booking_menu_handler:
            self.bot.send_message("❌ Profit Booking menu not initialized.")
            return True
        
        # Extract mode from callback_data
        mode = "SL-1.1" if "11" in callback_data else "SL-2.1"
        self.bot.profit_booking_menu_handler.handle_sl_mode_change(mode, user_id, message_id)
        return True
    
    def _handle_profit_booking_toggle(self, callback_data, user_id, message_id):
        """Handle profit booking toggle callbacks"""
        if not hasattr(self.bot, 'profit_booking_menu_handler') or not self.bot.profit_booking_menu_handler:
            self.bot.send_message("❌ Profit Booking menu not initialized.")
            return True
        
        # Route to correct method based on callback
        if callback_data == "toggle_profit_sl_hunt":
            self.bot.profit_booking_menu_handler.toggle_profit_sl_hunt(user_id, message_id)
        elif callback_data == "toggle_profit_protection":
            self.bot.profit_booking_menu_handler.toggle_profit_protection(user_id, message_id)
        return True
    
    def _handle_recovery_windows(self, callback_data, user_id, message_id):
        """Handle recovery windows editing callbacks"""
        if not hasattr(self.bot, 'fine_tune_handler') or not self.bot.fine_tune_handler:
            self.bot.send_message("❌ Fine-tune handler not initialized.")
            return True
        
        # Create callback_query dict for handler
        callback_query = {
            "data": callback_data,
            "from": {"id": user_id},
            "message": {"message_id": message_id}
        }
        
        # Route to recovery window handler
        if callback_data == "ft_recovery_windows_edit":
            self.bot.fine_tune_handler.show_recovery_windows_edit(user_id, 0, message_id)
        else:
            self.bot.fine_tune_handler.handle_recovery_window_callback(callback_query)
        
        return True
    
    def _handle_reentry_status(self, user_id, message_id):
        """Handle re-entry status view"""
        if not hasattr(self.bot, 'reentry_menu_handler') or not self.bot.reentry_menu_handler:
            self.bot.send_message("❌ Re-entry menu not initialized.")
            return True
        
        self.bot.reentry_menu_handler.show_reentry_status(user_id, message_id)
        return True
    
    def _handle_reentry_advanced(self, user_id, message_id):
        """Handle re-entry advanced settings submenu"""
        if not hasattr(self.bot, 'reentry_menu_handler') or not self.bot.reentry_menu_handler:
            self.bot.send_message("❌ Re-entry menu not initialized.")
            return True
        
        # Show advanced settings submenu
        if hasattr(self.bot.reentry_menu_handler, 'show_advanced_settings'):
            self.bot.reentry_menu_handler.show_advanced_settings(user_id, message_id)
        else:
            # Fallback: just show main reentry menu
            self.bot.reentry_menu_handler.show_reentry_menu(user_id, message_id)
        return True
    
    def _handle_advanced_settings_callback(self, callback_data, user_id, message_id):
        """Handle advanced settings parameter editor callbacks"""
        if not hasattr(self.bot, 'reentry_menu_handler') or not self.bot.reentry_menu_handler:
            self.bot.send_message("❌ Re-entry menu not initialized.")
            return True
        
        handler = self.bot.reentry_menu_handler
        
        # Route to appropriate editor
        if callback_data == "adv_monitor_interval":
            handler.show_monitor_interval_editor(user_id, message_id)
        elif callback_data == "adv_sl_offset":
            handler.show_sl_offset_editor(user_id, message_id)
        elif callback_data == "adv_cooldown":
            handler.show_cooldown_editor(user_id, message_id)
        elif callback_data == "adv_recovery_window":
            handler.show_recovery_window_editor(user_id, message_id)
        elif callback_data == "adv_max_levels":
            handler.show_max_levels_editor(user_id, message_id)
        elif callback_data == "adv_sl_reduction":
            handler.show_sl_reduction_editor(user_id, message_id)
        elif callback_data == "adv_reset_config":
            handler.reset_to_defaults(user_id, message_id)
        
        return True
    
    def _handle_parameter_setter(self, callback_data, user_id, message_id):
        """Handle parameter value setter callbacks"""
        if not hasattr(self.bot, 'reentry_menu_handler') or not self.bot.reentry_menu_handler:
            self.bot.send_message("❌ Re-entry menu not initialized.")
            return True
        
        handler = self.bot.reentry_menu_handler
        
        # Parse callback data to extract parameter and value
        # Format: set_<param>_<value>
        parts = callback_data.split("_")
        
        if len(parts) < 3:
            return True
        
        param_type = parts[1]  # monitor, offset, cooldown, window, levels, reduction
        value_str = parts[2]
        
        # Convert value to appropriate type and set parameter
        try:
            if param_type == "monitor":
                # set_monitor_5 → monitor_interval = 5
                value = int(value_str)
                handler.set_parameter("monitor_interval", value, user_id, message_id)
                
            elif param_type == "offset":
                # set_offset_1.0 → sl_hunt_offset_pips = 1.0
                value = float(value_str)
                handler.set_parameter("sl_hunt_offset_pips", value, user_id, message_id)
                
            elif param_type == "cooldown":
                # set_cooldown_30 → cooldown_seconds = 30
                value = int(value_str)
                handler.set_parameter("cooldown_seconds", value, user_id, message_id)
                
            elif param_type == "window":
                # set_window_15 → recovery_window_minutes = 15
                value = int(value_str)
                handler.set_parameter("recovery_window_minutes", value, user_id, message_id)
                
            elif param_type == "levels":
                # set_levels_5 → max_chain_levels = 5
                value = int(value_str)
                handler.set_parameter("max_chain_levels", value, user_id, message_id)
                
            elif param_type == "reduction":
                # set_reduction_30 → sl_reduction_per_level = 0.30
                value = int(value_str) / 100.0  # Convert percentage to decimal
                handler.set_parameter("sl_reduction_per_level", value, user_id, message_id)
                
        except Exception as e:
            logger.error(f"Error setting parameter from callback {callback_data}: {str(e)}")
            self.bot.send_message(f"❌ Error: {str(e)}")
        
        return True
