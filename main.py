import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
PYRUS_LOGIN = os.getenv("PYRUS_LOGIN")
PYRUS_SECURITY_KEY = os.getenv("PYRUS_SECURITY_KEY")
PYRUS_FORM_ID = os.getenv("PYRUS_FORM_ID")

# Safety check to fail fast if any secrets are missing
REQUIRED_VARS = {
    "TELEGRAM_BOT_TOKEN": TELEGRAM_BOT_TOKEN,
    "PYRUS_LOGIN": PYRUS_LOGIN,
    "PYRUS_SECURITY_KEY": PYRUS_SECURITY_KEY,
    "PYRUS_FORM_ID": PYRUS_FORM_ID
}

missing = [key for key, value in REQUIRED_VARS.items() if not value]
if missing:
    raise RuntimeError(f"Missing required environment variables: {', '.join(missing)}")
