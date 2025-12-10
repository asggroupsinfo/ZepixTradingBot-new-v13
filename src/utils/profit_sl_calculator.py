from typing import Tuple, Optional
from src.config import Config

class ProfitBookingSLCalculator:
    """
    Independent SL calculator for profit booking orders only
    Supports two modes:
    - SL-1.1: Logic-Specific SL ($20 for LOGIC1, $40 for LOGIC2, $50 for LOGIC3)
    - SL-2.1: Universal Fixed SL ($10 for all logics)
    This is separate from TP Trail's SL system
    """
    
    def __init__(self, config: Config):
        self.config = config
        self._load_settings()
    
    def _load_settings(self):
        """Load settings from config"""
        profit_config = self.config.get("profit_booking_config", {})
        self.current_mode = profit_config.get("sl_system", "SL-1.1")
        self.enabled = profit_config.get("sl_enabled", True)
        self.sl_1_1_settings = profit_config.get("sl_1_1_settings", {
            "LOGIC1": 20.0,
            "LOGIC2": 40.0,
            "LOGIC3": 50.0
        })
        self.sl_2_1_settings = profit_config.get("sl_2_1_settings", {
            "fixed_sl": 10.0
        })
    
    def calculate_sl_price(self, entry_price: float, direction: str, 
                          symbol: str, lot_size: float, 
                          strategy: str = "LOGIC1") -> Tuple[Optional[float], Optional[float]]:
        """
        Calculate SL price based on current mode and strategy
        Returns: (sl_price, sl_distance_in_price) or (None, None) if disabled
        
        Args:
            entry_price: Entry price of the order
            direction: 'buy' or 'sell'
            symbol: Trading symbol (e.g., 'XAUUSD')
            lot_size: Lot size of the order
            strategy: Trading strategy ('LOGIC1', 'LOGIC2', or 'LOGIC3')
        """
        # Return None if SL is disabled
        if not self.enabled:
            return None, None
        
        try:
            # Determine SL amount based on current mode
            if self.current_mode == "SL-1.1":
                # Logic-specific SL
                sl_amount = self.sl_1_1_settings.get(strategy, 20.0)
            else:  # SL-2.1
                # Universal fixed SL
                sl_amount = self.sl_2_1_settings.get("fixed_sl", 10.0)
            
            # Get symbol configuration
            symbol_config = self.config["symbol_config"][symbol]
            pip_size = symbol_config["pip_size"]
            pip_value_per_std_lot = symbol_config["pip_value_per_std_lot"]
            
            # Calculate pip value for this specific lot size
            pip_value = pip_value_per_std_lot * lot_size
            
            # Calculate how many pips needed for the specified loss amount
            sl_pips = sl_amount / pip_value
            
            # Convert pips to price distance
            sl_distance = sl_pips * pip_size
            
            # Calculate actual SL price based on direction
            if direction == "buy":
                sl_price = entry_price - sl_distance
            else:  # sell
                sl_price = entry_price + sl_distance
            
            return sl_price, sl_distance
            
        except KeyError as e:
            # Fallback if symbol not found in config
            print(f"WARNING: Symbol {symbol} not found in config, using fallback SL calculation")
            # Use a conservative fallback
            pip_size = 0.01  # Default pip size
            pip_value_per_std_lot = 10.0  # Default pip value
            pip_value = pip_value_per_std_lot * lot_size
            
            # Determine SL amount for fallback
            if self.current_mode == "SL-1.1":
                sl_amount = self.sl_1_1_settings.get(strategy, 20.0)
            else:
                sl_amount = self.sl_2_1_settings.get("fixed_sl", 10.0)
            
            sl_pips = sl_amount / pip_value
            sl_distance = sl_pips * pip_size
            
            if direction == "buy":
                sl_price = entry_price - sl_distance
            else:
                sl_price = entry_price + sl_distance
            
            return sl_price, sl_distance
        except Exception as e:
            print(f"ERROR: Error calculating profit booking SL: {str(e)}")
            # Return a safe fallback
            if direction == "buy":
                return entry_price - (0.01 * 50), 0.01 * 50
            else:
                return entry_price + (0.01 * 50), 0.01 * 50
    
    def switch_mode(self, new_mode: str) -> bool:
        """
        Switch between SL-1.1 and SL-2.1 modes
        Returns: True if successful, False if invalid mode
        """
        print(f"[SWITCH_MODE] Called with new_mode: {new_mode}", flush=True)
        old_mode = self.current_mode
        print(f"[SWITCH_MODE] Current mode: {old_mode}", flush=True)
        
        if new_mode not in ["SL-1.1", "SL-2.1"]:
            print(f"[SWITCH_MODE] Invalid mode: {new_mode}", flush=True)
            return False
        
        print(f"[SWITCH_MODE] Setting current_mode to {new_mode}", flush=True)
        self.current_mode = new_mode
        
        # Verify mode was set
        if self.current_mode != new_mode:
            print(f"[SWITCH_MODE ERROR] Mode not set correctly! Expected {new_mode}, got {self.current_mode}", flush=True)
            return False
        print(f"[SWITCH_MODE] Verified current_mode is now: {self.current_mode}", flush=True)
        print(f"[SWITCH_MODE] About to update config in memory...", flush=True)
        print(f"[SWITCH_MODE] Config object type: {type(self.config)}", flush=True)
        
        try:
            # Update config in memory FIRST
            # CRITICAL FIX: Config class doesn't support 'in' operator, use get() instead
            print(f"[SWITCH_MODE] Step 1: Getting profit_booking_config...", flush=True)
            profit_config = self.config.get("profit_booking_config")
            if profit_config is None:
                print(f"[SWITCH_MODE] Step 2: Creating profit_booking_config dict...", flush=True)
                self.config.update("profit_booking_config", {})
                profit_config = self.config.get("profit_booking_config", {})
            
            print(f"[SWITCH_MODE] Step 3: Setting sl_system to {new_mode}...", flush=True)
            # Access the underlying config dictionary
            if not hasattr(self.config, 'config'):
                # Fallback: use update method
                profit_config["sl_system"] = new_mode
                self.config.update("profit_booking_config", profit_config)
            else:
                # Direct access to config dictionary
                if "profit_booking_config" not in self.config.config:
                    self.config.config["profit_booking_config"] = {}
                self.config.config["profit_booking_config"]["sl_system"] = new_mode
            print(f"[SWITCH_MODE] Config updated in memory with sl_system={new_mode}", flush=True)
            
            # CRITICAL: Save config in background thread - DON'T WAIT for it
            # This ensures we return immediately and don't block execution
            print(f"[SWITCH_MODE] Step 4: Importing threading...", flush=True)
            import threading
            print(f"[SWITCH_MODE] Step 5: Creating background save function...", flush=True)
            def save_config_background():
                try:
                    print(f"[SWITCH_MODE BACKGROUND] Starting config save...", flush=True)
                    self.config.save_config()
                    print(f"[SWITCH_MODE BACKGROUND] Config saved successfully", flush=True)
                except Exception as e:
                    print(f"[SWITCH_MODE BACKGROUND] Config save error (non-critical): {e}", flush=True)
                    import traceback
                    traceback.print_exc()
            
            print(f"[SWITCH_MODE] Step 6: Creating thread...", flush=True)
            save_thread = threading.Thread(target=save_config_background, daemon=True)
            print(f"[SWITCH_MODE] Step 7: Starting thread...", flush=True)
            save_thread.start()
            print(f"[SWITCH_MODE] Config save started in background thread (non-blocking)", flush=True)
        except Exception as config_error:
            print(f"[SWITCH_MODE ERROR] Error updating config: {config_error}", flush=True)
            import traceback
            traceback.print_exc()
            # Continue anyway - mode was already set
        
        # IMMEDIATELY return True - don't wait for config save
        print(f"[SWITCH_MODE] Step 8: Mode switch complete: {old_mode} -> {new_mode}", flush=True)
        print(f"[SWITCH_MODE] Step 9: Final verification - current_mode: {self.current_mode}, new_mode: {new_mode}", flush=True)
        print(f"✅ MODE VERIFIED: {self.current_mode}", flush=True)
        print(f"[SWITCH_MODE] Step 10: Returning True IMMEDIATELY (config save in background)", flush=True)
        return True
    
    def set_enabled(self, enabled: bool) -> bool:
        """
        Enable or disable the profit booking SL system
        Returns: True if successful
        """
        self.enabled = enabled
        
        # Update config
        if "profit_booking_config" not in self.config:
            self.config["profit_booking_config"] = {}
        self.config["profit_booking_config"]["sl_enabled"] = enabled
        
        # Save config
        try:
            self.config.save_config()
        except Exception as e:
            print(f"ERROR: Failed to save config after enable/disable: {str(e)}")
        
        return True
    
    def update_logic_sl(self, strategy: str, amount: float) -> bool:
        """
        Update SL amount for a specific logic (SL-1.1 only)
        Returns: True if successful, False if invalid strategy
        """
        if strategy not in ["LOGIC1", "LOGIC2", "LOGIC3"]:
            return False
        
        if amount <= 0:
            return False
        
        # Update setting
        self.sl_1_1_settings[strategy] = amount
        
        # Update config
        if "profit_booking_config" not in self.config:
            self.config["profit_booking_config"] = {}
        if "sl_1_1_settings" not in self.config["profit_booking_config"]:
            self.config["profit_booking_config"]["sl_1_1_settings"] = {}
        self.config["profit_booking_config"]["sl_1_1_settings"][strategy] = amount
        
        # Save config
        try:
            self.config.save_config()
        except Exception as e:
            print(f"ERROR: Failed to save config after SL update: {str(e)}")
        
        return True
    
    def reset_to_defaults(self) -> bool:
        """
        Reset all settings to defaults
        Returns: True if successful
        """
        # Reset to defaults
        self.current_mode = "SL-1.1"
        self.enabled = True
        self.sl_1_1_settings = {
            "LOGIC1": 20.0,
            "LOGIC2": 40.0,
            "LOGIC3": 50.0
        }
        self.sl_2_1_settings = {
            "fixed_sl": 10.0
        }
        
        # Update config
        if "profit_booking_config" not in self.config:
            self.config["profit_booking_config"] = {}
        self.config["profit_booking_config"]["sl_system"] = "SL-1.1"
        self.config["profit_booking_config"]["sl_enabled"] = True
        self.config["profit_booking_config"]["sl_1_1_settings"] = {
            "LOGIC1": 20.0,
            "LOGIC2": 40.0,
            "LOGIC3": 50.0
        }
        self.config["profit_booking_config"]["sl_2_1_settings"] = {
            "fixed_sl": 10.0
        }
        
        # Save config
        try:
            self.config.save_config()
        except Exception as e:
            print(f"ERROR: Failed to save config after reset: {str(e)}")
        
        return True
    
    def get_pip_value(self, symbol: str, lot_size: float) -> float:
        """
        Get pip value for a specific symbol and lot size
        Returns pip value in dollars
        """
        try:
            symbol_config = self.config["symbol_config"][symbol]
            pip_value_per_std_lot = symbol_config["pip_value_per_std_lot"]
            return pip_value_per_std_lot * lot_size
        except KeyError:
            # Fallback
            return 10.0 * lot_size
    
    def validate_sl_loss(self, entry_price: float, sl_price: float, 
                        direction: str, symbol: str, lot_size: float,
                        strategy: str = "LOGIC1") -> dict:
        """
        Validate that SL will result in expected loss (within tolerance)
        Returns: {"valid": bool, "actual_loss": float, "expected_loss": float, "difference": float}
        """
        try:
            # Determine expected loss based on current mode
            if self.current_mode == "SL-1.1":
                expected_loss = self.sl_1_1_settings.get(strategy, 20.0)
            else:
                expected_loss = self.sl_2_1_settings.get("fixed_sl", 10.0)
            
            # Calculate actual loss
            pip_size = self.config["symbol_config"][symbol]["pip_size"]
            pip_value_per_std_lot = self.config["symbol_config"][symbol]["pip_value_per_std_lot"]
            pip_value = pip_value_per_std_lot * lot_size
            
            # Calculate price difference in pips
            price_diff = abs(entry_price - sl_price)
            pips = price_diff / pip_size
            
            # Calculate actual loss
            actual_loss = pips * pip_value
            
            # Check if within 5% tolerance
            tolerance = expected_loss * 0.05  # 5% tolerance
            difference = abs(actual_loss - expected_loss)
            
            is_valid = difference <= tolerance
            
            return {
                "valid": is_valid,
                "actual_loss": actual_loss,
                "expected_loss": expected_loss,
                "difference": difference,
                "tolerance": tolerance
            }
        except Exception as e:
            # Fallback expected loss
            if self.current_mode == "SL-1.1":
                fallback_loss = self.sl_1_1_settings.get(strategy, 20.0)
            else:
                fallback_loss = self.sl_2_1_settings.get("fixed_sl", 10.0)
            
            return {
                "valid": False,
                "actual_loss": 0.0,
                "expected_loss": fallback_loss,
                "difference": fallback_loss,
                "error": str(e)
            }

