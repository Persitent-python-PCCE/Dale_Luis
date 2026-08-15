import csv
from datetime import datetime
from pathlib import Path

from Project0.config.connection import get_connection


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LOG_FILE = PROJECT_ROOT / "logs" / "application.log"
BACKUP_DIR = PROJECT_ROOT / "backups"
TABLES = (
    "Customer", "Categories", "Products", "orders", "order_details", "reviews"
)


def log_event(message):
    LOG_FILE.parent.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with LOG_FILE.open("a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")


def backup_database():
    BACKUP_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    con = get_connection()
    cursor = con.cursor()

    try:
        for table in TABLES:
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            backup_file = BACKUP_DIR / f"{table.lower()}_{timestamp}.csv"
            with backup_file.open("w", newline="", encoding="utf-8") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(columns)
                writer.writerows(rows)
    finally:
        cursor.close()
        con.close()

    log_event("Database backup created.")
