"""
Profit Booking Menu Handler - Visual SL Mode Selector
Provides zero-typing button-based control for Profit Booking settings.
"""

from typing import Optional
import logging

logger = logging.getLogger(__name__)


class ProfitBookingMenuHandler:
    """Telegram menu handler for Profit Booking with visual selectors"""
    
    def __init__(self, bot):
        """
        Initialize Profit Booking menu handler
        
        Args:
            bot: TelegramBot instance
        """
        self.bot = bot
        self.config = bot.config
    
    def _btn(self, text: str, callback_data: str):
        """Helper to create inline keyboard button dict"""
        return {"text": text, "callback_data": callback_data}
    
    def _create_keyboard(self, rows: list):
        """Helper to create inline keyboard dict"""
        return {"inline_keyboard": rows}
    
    def show_profit_booking_menu(self, user_id: int, message_id: Optional[int] = None):
        """
        Show Profit Booking menu with visual SL mode selector
        
        Args:
            user_id: Telegram user ID
            message_id: Message ID to edit (if updating existing message)
        """
        try:
            # Get current config
            profit_config = self.config.get("profit_booking_config", {})
            current_mode = profit_config.get("sl_system", "SL-1.1")
            profit_enabled = profit_config.get("enabled", False)
            sl_hunt_enabled = profit_config.get("sl_hunt_enabled", False)
            
            # Build keyboard with 2-column layout
            keyboard = [
]
            
            # Status and Quick Actions (toggles are full-width)
            keyboard.append([self._btn(
                f"🛡 Profit Protection [{'ON ✅' if profit_enabled else 'OFF ❌'}]",
                "toggle_profit_protection"
            )])
            
            # Quick actions in 2-column layout
            keyboard.append([
                self._btn("📊 Active Chains", "cmd_profit_profit_chains"),
                self._btn(f"💎 SL Hunt [{'ON ✅' if sl_hunt_enabled else 'OFF ❌'}]", "toggle_profit_sl_hunt")
            ])
            
            # SL MODE SELECTOR (Visual Toggle) - header
            keyboard.append([self._btn("⚙ SL MODE", "noop")])  # Header
            
            # Mode buttons with visual indicators (2-column)
            sl_11_indicator = " ✅" if current_mode == "SL-1.1" else ""
            sl_21_indicator = " ✅" if current_mode == "SL-2.1" else ""
            
            keyboard.append([
                self._btn(f"SL-1.1 (Logic){sl_11_indicator}", "profit_sl_mode_11"),
                self._btn(f"SL-2.1 (Fixed){sl_21_indicator}", "profit_sl_mode_21")
            ])
            
            # Additional Options (2-column layout)
            keyboard.append([
                self._btn("📈 View Config", "cmd_profit_profit_config"),
                self._btn("📉 Set Targets", "cmd_profit_set_profit_targets")
            ])
            keyboard.append([self._btn("🏠 Back to Main Menu", "menu_main")])
            
            # Build message
            # Get mode description
            if current_mode == "SL-1.1":
                mode_desc = "Logic-Specific (Per Strategy)"
                sl_settings = profit_config.get("sl_1_1_settings", {})
                sl_info = (
                    f"• LOGIC1: ${sl_settings.get('LOGIC1', 20.0)}\n"
                    f"• LOGIC2: ${sl_settings.get('LOGIC2', 40.0)}\n"
                    f"• LOGIC3: ${sl_settings.get('LOGIC3', 50.0)}"
                )
            else:
                mode_desc = "Fixed Universal"
                sl_settings = profit_config.get("sl_2_1_settings", {})
                fixed_sl = sl_settings.get("fixed_sl", 10.0)
                sl_info = f"• Fixed SL: ${fixed_sl} (All Logics)"
            
            message = (
                "📈 <b>PROFIT BOOKING</b>\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"<b>Current SL Mode:</b> {current_mode}\n"
                f"<b>Type:</b> {mode_desc}\n\n"
                f"<b>SL Settings:</b>\n"
                f"{sl_info}\n\n"
                f"<b>Status:</b> {'ACTIVE 🟢' if profit_enabled else 'INACTIVE 🔴'}\n\n"
                "<b>💡 Tip:</b> Click mode buttons to switch\n"
            )
            
            reply_markup = self._create_keyboard(keyboard)
            
            # Send or edit message
            if message_id:
                self.bot.edit_message(message, message_id, reply_markup, parse_mode="HTML")
            else:
                self.bot.send_message_with_keyboard(message, reply_markup, parse_mode="HTML")
                
            logger.info(f"Profit Booking menu shown to user {user_id} (Mode: {current_mode})")
            
        except Exception as e:
            logger.error(f"Error showing profit booking menu: {str(e)}")
            import traceback
            traceback.print_exc()
    
    def handle_sl_mode_change(self, mode: str, user_id: int, message_id: int):
        """
        Handle SL mode change
        
        Args:
            mode: New mode ("SL-1.1" or "SL-2.1")
            user_id: Telegram user ID
            message_id: Message ID to update
        """
        try:
            # Get current mode
            current_mode = self.config.get("profit_booking_config", {}).get("sl_system", "SL-1.1")
            
            if current_mode == mode:
                # Already in this mode
                self.bot.send_message(f"ℹ️ Already using {mode} mode")
                return
            
            # Update config
            self.config.update_nested("profit_booking_config.sl_system", mode)
            self.config.save()
            
            logger.info(f"Profit SL mode changed: {current_mode} → {mode}")
            
            # Show confirmation
            mode_name = "Logic-Specific" if mode == "SL-1.1" else "Fixed Universal"
            self.bot.send_message(
                f"✅ <b>SL Mode Changed</b>\n\n"
                f"New Mode: {mode} ({mode_name})\n"
                f"Previous: {current_mode}\n\n"
                f"Settings will apply to new orders.",
                parse_mode="HTML"
            )
            
            # Refresh menu to show updated mode
            self.show_profit_booking_menu(user_id, message_id)
            
        except Exception as e:
            logger.error(f"Error changing SL mode: {str(e)}")
            import traceback
            traceback.print_exc()
            self.bot.send_message(f"❌ Error changing mode: {str(e)}")
    
    def toggle_profit_protection(self, user_id: int, message_id: int):
        """
        Toggle profit booking protection on/off
        
        Args:
            user_id: Telegram user ID
            message_id: Message ID to update
        """
        try:
            current = self.config.get("profit_booking_config", {}).get("enabled", False)
            new_value = not current
            
            # Update config
            self.config.update_nested("profit_booking_config.enabled", new_value)
            self.config.save()
            
            status = "ENABLED ✅" if new_value else "DISABLED ❌"
            self.bot.send_message(f"🛡 Profit Protection: {status}")
            
            logger.info(f"Profit protection toggled: {current} → {new_value}")
            
            # Refresh menu
            self.show_profit_booking_menu(user_id, message_id)
            
        except Exception as e:
            logger.error(f"Error toggling profit protection: {str(e)}")
            self.bot.send_message(f"❌ Error: {str(e)}")
    
    def toggle_profit_sl_hunt(self, user_id: int, message_id: int):
        """
        Toggle profit booking SL hunt on/off
        
        Args:
            user_id: Telegram user ID
            message_id: Message ID to update
        """
        try:
            current = self.config.get("profit_booking_config", {}).get("sl_hunt_enabled", False)
            new_value = not current
            
            # Update config
            self.config.update_nested("profit_booking_config.sl_hunt_enabled", new_value)
            self.config.save()
            
            status = "ENABLED ✅" if new_value else "DISABLED ❌"
            self.bot.send_message(f"💎 Profit SL Hunt: {status}")
            
            logger.info(f"Profit SL hunt toggled: {current} → {new_value}")
            
            # Refresh menu
            self.show_profit_booking_menu(user_id, message_id)
            
        except Exception as e:
            logger.error(f"Error toggling profit SL hunt: {str(e)}")
            self.bot.send_message(f"❌ Error: {str(e)}")
