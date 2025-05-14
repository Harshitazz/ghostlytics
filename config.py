"""
Configuration settings for the ModeSwitch application.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

APP_NAME = "ModeSwitch"
APP_VERSION = "1.0.0"

DEFAULT_MODES = ["gaming", "work", "study"]
DEFAULT_MOODS = ["happy", "stressed", "tired", "energetic"]
DEFAULT_TIMES = ["morning", "afternoon", "evening"]

APP_DIR = Path(__file__).parent
DATA_DIR = APP_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
HISTORY_FILE = DATA_DIR / "session_history.json"

def get_groq_api_key():
    """Get the Groq API key from environment variable."""
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError(
            "GROQ_API_KEY environment variable not set. "
            "Please check your .env file or set it before running the application."
        )
    return api_key

# LLM model settings
LLM_MODEL = os.environ.get("LLM_MODEL", "llama-3.3-70b-versatile")
LLM_TEMPERATURE = float(os.environ.get("LLM_TEMPERATURE", "0.9"))
LLM_MAX_TOKENS = int(os.environ.get("LLM_MAX_TOKENS", "1024"))