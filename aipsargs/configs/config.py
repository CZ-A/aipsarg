import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
env_path = './.env'
load_dotenv(env_path)

# --- API Configuration ---
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
PASSWORD = os.getenv("PASSWORD")

# --- Trading Configuration ---
PAIRS = os.getenv("PAIRS","CORE/USDT")
TRADING_CONFIG = {
    "MARGIN": int(os.getenv("MARGIN", 10)),
    "TIMEFRAME": os.getenv("TIMEFRAME", '1m'),
    "LIMIT": int(os.getenv("LIMIT", 100)),
    "MINIMUM_ORDER_AMOUNT": float(os.getenv("MINIMUM_ORDER_AMOUNT", 2)),
    "BUY_PERCENTAGE": float(os.getenv("BUY_PERCENTAGE", 0.2)),
    "SELL_PERCENTAGE": float(os.getenv("SELL_PERCENTAGE", 0.8)),
    "TRADING_STYLE": os.getenv("TRADING_STYLE", 'swing_trading'),
    "TAKE_PROFIT_PERCENTAGE": float(os.getenv("TAKE_PROFIT_PERCENTAGE", 0.05)),
    "STOP_LOSS_PERCENTAGE": float(os.getenv("STOP_LOSS_PERCENTAGE", 0.03)),
    "MONITOR_SLEEP_INTERVAL": int(os.getenv("MONITOR_SLEEP_INTERVAL", 0)),
    "BOT_STATE_FILE": "./bot_state.json"  # Tambahkan BOT_STATE_FILE di sini
}

# --- Model Configuration ---
MODEL_CONFIG = {
    "TRAINING_LIMIT": int(os.getenv("TRAINING_LIMIT", 500)),
    "LSTM_UNITS": int(os.getenv("LSTM_UNITS", 50)),
    "EPOCHS": int(os.getenv("EPOCHS", 32)),
    "BATCH_SIZE": int(os.getenv("BATCH_SIZE", 64)),
    "SEQUENCE_LENGTH": int(os.getenv("SEQUENCE_LENGTH", 20)),
}

# --- Indicator Configuration ---
INDICATOR_CONFIG = {
    "SCALPING_MA_WINDOW": int(os.getenv("SCALPING_MA_WINDOW", 10)),
    "SCALPING_EMA_WINDOW": int(os.getenv("SCALPING_EMA_WINDOW", 10)),
    "SCALPING_MACD_SHORT_WINDOW": int(os.getenv("SCALPING_MACD_SHORT_WINDOW", 6)),
    "SCALPING_MACD_LONG_WINDOW": int(os.getenv("SCALPING_MACD_LONG_WINDOW", 13)),
    "SCALPING_RSI_WINDOW": int(os.getenv("SCALPING_RSI_WINDOW", 7)),
    "SCALPING_STOCHASTIC_WINDOW": int(os.getenv("SCALPING_STOCHASTIC_WINDOW", 7)),
    "SCALPING_BOLLINGER_WINDOW": int(os.getenv("SCALPING_BOLLINGER_WINDOW", 10)),
    "SCALPING_ATR_WINDOW": int(os.getenv("SCALPING_ATR_WINDOW", 7)),
    "SCALPING_ADX_WINDOW": int(os.getenv("SCALPING_ADX_WINDOW", 7)),
    "SCALPING_SENTIMENT_WINDOW": int(os.getenv("SCALPING_SENTIMENT_WINDOW", 10)),
    "DAY_TRADING_MA_WINDOW": int(os.getenv("DAY_TRADING_MA_WINDOW", 20)),
    "DAY_TRADING_EMA_WINDOW": int(os.getenv("DAY_TRADING_EMA_WINDOW", 20)),
    "DAY_TRADING_MACD_SHORT_WINDOW": int(os.getenv("DAY_TRADING_MACD_SHORT_WINDOW", 12)),
    "DAY_TRADING_MACD_LONG_WINDOW": int(os.getenv("DAY_TRADING_MACD_LONG_WINDOW", 26)),
    "DAY_TRADING_RSI_WINDOW": int(os.getenv("DAY_TRADING_RSI_WINDOW", 14)),
    "DAY_TRADING_STOCHASTIC_WINDOW": int(os.getenv("DAY_TRADING_STOCHASTIC_WINDOW", 14)),
    "DAY_TRADING_BOLLINGER_WINDOW": int(os.getenv("DAY_TRADING_BOLLINGER_WINDOW", 20)),
    "DAY_TRADING_ATR_WINDOW": int(os.getenv("DAY_TRADING_ATR_WINDOW", 14)),
    "DAY_TRADING_ADX_WINDOW": int(os.getenv("DAY_TRADING_ADX_WINDOW", 14)),
    "DAY_TRADING_SENTIMENT_WINDOW": int(os.getenv("DAY_TRADING_SENTIMENT_WINDOW", 20)),
    "SWING_TRADING_MA_WINDOW": int(os.getenv("SWING_TRADING_MA_WINDOW", 50)),
    "SWING_TRADING_EMA_WINDOW": int(os.getenv("SWING_TRADING_EMA_WINDOW", 50)),
    "SWING_TRADING_MACD_SHORT_WINDOW": int(os.getenv("SWING_TRADING_MACD_SHORT_WINDOW", 26)),
    "SWING_TRADING_MACD_LONG_WINDOW": int(os.getenv("SWING_TRADING_MACD_LONG_WINDOW", 52)),
    "SWING_TRADING_RSI_WINDOW": int(os.getenv("SWING_TRADING_RSI_WINDOW", 20)),
    "SWING_TRADING_STOCHASTIC_WINDOW": int(os.getenv("SWING_TRADING_STOCHASTIC_WINDOW", 20)),
    "SWING_TRADING_BOLLINGER_WINDOW": int(os.getenv("SWING_TRADING_BOLLINGER_WINDOW", 50)),
    "SWING_TRADING_ATR_WINDOW": int(os.getenv("SWING_TRADING_ATR_WINDOW", 20)),
    "SWING_TRADING_ADX_WINDOW": int(os.getenv("SWING_TRADING_ADX_WINDOW", 20)),
    "SWING_TRADING_SENTIMENT_WINDOW": int(os.getenv("SWING_TRADING_SENTIMENT_WINDOW", 50)),
    "LONG_TERM_MA_WINDOW": int(os.getenv("LONG_TERM_MA_WINDOW", 100)),
    "LONG_TERM_EMA_WINDOW": int(os.getenv("LONG_TERM_EMA_WINDOW", 100)),
    "LONG_TERM_MACD_SHORT_WINDOW": int(os.getenv("LONG_TERM_MACD_SHORT_WINDOW", 52)),
    "LONG_TERM_MACD_LONG_WINDOW": int(os.getenv("LONG_TERM_MACD_LONG_WINDOW", 104)),
    "LONG_TERM_RSI_WINDOW": int(os.getenv("LONG_TERM_RSI_WINDOW", 30)),
    "LONG_TERM_STOCHASTIC_WINDOW": int(os.getenv("LONG_TERM_STOCHASTIC_WINDOW", 30)),
    "LONG_TERM_BOLLINGER_WINDOW": int(os.getenv("LONG_TERM_BOLLINGER_WINDOW", 100)),
    "LONG_TERM_ATR_WINDOW": int(os.getenv("LONG_TERM_ATR_WINDOW", 30)),
    "LONG_TERM_ADX_WINDOW": int(os.getenv("LONG_TERM_ADX_WINDOW", 30)),
    "LONG_TERM_SENTIMENT_WINDOW": int(os.getenv("LONG_TERM_SENTIMENT_WINDOW", 100)),
}

# --- File Paths ---
MODEL_FILE = "./model.h5"
SCALER_FILE = "./scaler.json"
OUTPUT_DIR = "./lab.alice"

def validate_config():
    """Validates if essential configuration variables are set."""
    if not all([API_KEY, API_SECRET, PASSWORD, PAIRS]):
        logging.error("Essential API or trading configuration variables are missing.")
        return False
    if not all(TRADING_CONFIG.values()):
      logging.error("Essential trading configuration variables are missing.")
      return False

    # Validate trading style
    valid_trading_styles = ['scalping', 'day_trading', 'swing_trading', 'long_term']
    if TRADING_CONFIG["TRADING_STYLE"] not in valid_trading_styles:
        logging.error(f"Invalid TRADING_STYLE: {TRADING_CONFIG['TRADING_STYLE']}. Must be one of {valid_trading_styles}")
        return False
    
    return True

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(levelname)s] - %(message)s')
    if validate_config():
        logging.info("Configuration is valid.")
    else:
        logging.error("Configuration is invalid.")