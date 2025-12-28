from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
from src.config import Config
from src.models import Alert

class AlertProcessor:
    def __init__(self, config: Config, trend_manager=None, telegram_bot=None):
        self.config = config
        self.trend_manager = trend_manager  # For checking if trend actually changed
        self.telegram_bot = telegram_bot  # For sending notifications
        self.recent_alerts: List[Alert] = []
        self.alert_window = timedelta(minutes=5)
    
    def validate_alert(self, alert_data: Dict[str, Any]) -> bool:
        """Validate incoming alert"""
        try:
            print(f"ALERT: Received alert: {alert_data}")
            
            # Add timestamp if not present
            if 'timestamp' not in alert_data:
                alert_data['timestamp'] = datetime.now().isoformat()
            
            # NO DEFAULT TF FIELD - tf field is REQUIRED
            # If tf missing, Alert() will raise ValidationError
            
            # Store raw_data properly
            alert = Alert(**alert_data, raw_data=alert_data)
            
            # Clean old alerts BEFORE checking for duplicates
            self.clean_old_alerts()
            
            # Check if alert is duplicate
            if self.is_duplicate_alert(alert):
                print("ERROR: Duplicate alert detected")
                
                # IMPORTANT: Send Telegram notification for duplicate TREND alerts
                if alert.type in ['trend', 'bias'] and self.telegram_bot:
                    try:
                        dup_msg = f"ℹ️ Duplicate trend alert ignored - {alert.symbol} {alert.tf.upper()} is already {alert.signal.upper()}"
                        self.telegram_bot.send_message(dup_msg)
                        print(f"INFO: Sent duplicate notification to Telegram")
                    except Exception as e:
                        print(f"WARNING: Could not send duplicate notification: {e}")
                
                return False
                
            # Check if symbol is valid
            if not self.is_valid_symbol(alert.symbol):
                print(f"ERROR: Invalid symbol: {alert.symbol}")
                return False
                
            # Check if timeframe is valid
            if alert.tf not in ['1h', '15m', '5m', '1d']:
                print(f"ERROR: Invalid timeframe: {alert.tf}")
                return False
                
            # Check if signal type is valid
            if alert.type == 'bias' or alert.type == 'trend':
                if alert.signal not in ['bull', 'bear']:
                    print(f"ERROR: Invalid signal for {alert.type}: {alert.signal}")
                    return False
            elif alert.type == 'entry':
                if alert.signal not in ['buy', 'sell']:
                    print(f"ERROR: Invalid signal for {alert.type}: {alert.signal}")
                    return False
            elif alert.type == 'reversal':
                if alert.signal not in ['reversal_bull', 'reversal_bear', 'bull', 'bear']:
                    print(f"ERROR: Invalid signal for {alert.type}: {alert.signal}")
                    return False
            elif alert.type == 'exit':
                if alert.signal not in ['bull', 'bear']:
                    print(f"ERROR: Invalid signal for {alert.type}: {alert.signal}")
                    return False
                    
            # CRITICAL FIX: Only store non-entry alerts immediately
            # Entry alerts should ONLY be stored after successful execution
            # Otherwise, failed entries will block future legitimate alerts as "duplicates"
            if alert.type != 'entry':
                self.recent_alerts.append(alert)
                print(f"INFO: Stored {alert.type} alert for duplicate detection")
            else:
                print(f"INFO: Entry alert validated but NOT stored (will store after execution)")
            
            print("SUCCESS: Alert validation successful")
            return True
            
        except Exception as e:
            print(f"ERROR: Alert validation error: {str(e)}")
            import traceback
            traceback.print_exc()
            return False
    
    def is_duplicate_alert(self, alert: Alert) -> bool:
        """Check if this is a duplicate alert"""
        # Special handling for trend/bias alerts - check if value actually changed
        if alert.type in ['trend', 'bias'] and self.trend_manager:
            try:
                # Get current trend from trend_manager
                current_trend = self.trend_manager.get_trend(alert.symbol, alert.tf)
                
                # Normalize alert signal to match stored format (BEARISH/BULLISH)
                signal_normalized = alert.signal.upper()
                if signal_normalized in ['BEAR', 'SELL', 'BEARISH']:
                    signal_normalized = 'BEARISH'
                elif signal_normalized in ['BULL', 'BUY', 'BULLISH']:
                    signal_normalized = 'BULLISH'
                
                # Check if trend matches
                if current_trend and current_trend == signal_normalized:
                    print(f"INFO: Duplicate trend detected - {alert.symbol} {alert.tf.upper()} is already {signal_normalized}")
                    return True  # Duplicate regardless of mode
            except Exception as e:
                # If trend check fails, fall through to normal duplicate detection
                print(f"WARNING: Trend check failed, using normal duplicate detection: {e}")
        
        # Get incoming alert's timestamp
        incoming_timestamp = datetime.now()
        if alert.raw_data and isinstance(alert.raw_data, dict):
            timestamp_str = alert.raw_data.get('timestamp')
            if timestamp_str:
                try:
                    incoming_timestamp = datetime.fromisoformat(timestamp_str)
                except (ValueError, TypeError):
                    pass
        
        for recent_alert in self.recent_alerts:
            # Skip alerts older than alert_window relative to incoming alert
            if recent_alert.raw_data and isinstance(recent_alert.raw_data, dict):
                recent_timestamp_str = recent_alert.raw_data.get('timestamp')
                if recent_timestamp_str:
                    try:
                        recent_alert_time = datetime.fromisoformat(recent_timestamp_str)
                        if incoming_timestamp - recent_alert_time >= self.alert_window:
                            continue  # Skip old alerts (>5 min apart)
                    except (ValueError, TypeError):
                        pass  # If timestamp invalid, still check for duplicate
            
            if (recent_alert.type == alert.type and
                recent_alert.symbol == alert.symbol and
                recent_alert.tf == alert.tf and
                recent_alert.signal == alert.signal):
                return True
                
        return False
    
    def is_valid_symbol(self, symbol: str) -> bool:
        """Check if symbol is valid for trading"""
        valid_symbols = ['XAUUSD', 'EURUSD', 'GBPUSD', 'USDJPY', 'USDCAD', 
                        'AUDUSD', 'NZDUSD', 'EURJPY', 'GBPJPY', 'AUDJPY']
        return symbol in valid_symbols
    
    def clean_old_alerts(self):
        """Remove alerts older than the alert window"""
        try:
            current_time = datetime.now()
            cleaned_alerts = []
            
            for alert in self.recent_alerts:
                timestamp_str = None
                
                if alert.raw_data and isinstance(alert.raw_data, dict):
                    timestamp_str = alert.raw_data.get('timestamp')
                
                if timestamp_str:
                    try:
                        alert_time = datetime.fromisoformat(timestamp_str)
                        if current_time - alert_time < self.alert_window:
                            cleaned_alerts.append(alert)
                    except (ValueError, TypeError):
                        cleaned_alerts.append(alert)
                else:
                    cleaned_alerts.append(alert)
            
            self.recent_alerts = cleaned_alerts
            
        except Exception as e:
            print(f"WARNING: Error cleaning alerts: {str(e)}")
    
    def get_recent_alerts(self, alert_type: Optional[str] = None, symbol: Optional[str] = None, tf: Optional[str] = None) -> List[Alert]:
        """Get recent alerts filtered by type, symbol, or timeframe"""
        filtered = self.recent_alerts
        
        if alert_type:
            filtered = [alert for alert in filtered if alert.type == alert_type]
            
        if symbol:
            filtered = [alert for alert in filtered if alert.symbol == symbol]
            
        if tf:
            filtered = [alert for alert in filtered if alert.tf == tf]
            
        return filtered
    
    def store_entry_alert(self, alert: Alert):
        """
        Store an entry alert AFTER successful order execution.
        This prevents failed orders from blocking future legitimate alerts.
        """
        try:
            # Only store if it's actually an entry alert
            if alert.type == 'entry':
                self.recent_alerts.append(alert)
                print(f"INFO: Entry alert stored after successful execution for duplicate detection")
        except Exception as e:
            print(f"WARNING: Failed to store entry alert: {str(e)}")