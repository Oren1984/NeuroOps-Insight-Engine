from pathlib import Path

BASE_DIR = Path(file).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = BASE_DIR / "business_intelligence.db"

USERS_CSV = DATA_DIR / "users.csv"
USAGE_CSV = DATA_DIR / "usage_events.csv"
SYSTEM_CSV = DATA_DIR / "system_events.csv"
TICKETS_CSV = DATA_DIR / "tickets.csv"
