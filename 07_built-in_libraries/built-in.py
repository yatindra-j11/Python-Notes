# ==========================================
# PHASE 10: BUILT-IN LIBRARIES DEMO
# Bank Transaction Report
# ==========================================

import os
import shutil
import json
import csv
import re
import math
import random
import logging

from pathlib import Path
from datetime import datetime, timedelta
from statistics import mean, median
from collections import Counter, defaultdict, deque
from itertools import islice, accumulate
from functools import reduce, lru_cache, partial


# 1. PATHLIB + OS: CREATE A WORKING DIRECTORY
folder = Path("bank_report")
folder.mkdir(exist_ok=True)

print("Working directory:", os.getcwd())
print("Folder exists:", folder.exists())


# 2. DATETIME: TRANSACTION TIMESTAMPS
now = datetime.now()
tomorrow = now + timedelta(days=1)

print("Current time:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Tomorrow:", tomorrow.date())


# 3. MATH + RANDOM: SAMPLE TRANSACTIONS
random.seed(42)

transactions = [
    {"type": "deposit", "amount": 2000},
    {"type": "withdrawal", "amount": 500},
    {"type": "deposit", "amount": 1500},
    {"type": "withdrawal", "amount": 300},
]

print("Square root:", math.sqrt(144))
print("Random transaction:", random.choice(transactions))


# 4. COLLECTIONS: COUNT AND GROUP TRANSACTIONS
counts = Counter(t["type"] for t in transactions)

grouped = defaultdict(list)
for transaction in transactions:
    grouped[transaction["type"]].append(transaction["amount"])

recent_transactions = deque(transactions, maxlen=3)

print("Transaction counts:", counts)
print("Grouped transactions:", dict(grouped))
print("Recent transactions:", list(recent_transactions))


# 5. STATISTICS + ITERTOOLS
amounts = [t["amount"] for t in transactions]

print("Average:", mean(amounts))
print("Median:", median(amounts))
print("Running totals:", list(accumulate(amounts)))
print("First two amounts:", list(islice(amounts, 2)))


# 6. FUNCTOOLS: REDUCE, PARTIAL, CACHING
total_amount = reduce(lambda a, b: a + b, amounts, 0)
print("Total transaction volume:", total_amount)

def calculate_fee(amount, rate):
    return amount * rate

bank_fee = partial(calculate_fee, rate=0.02)
print("Fee on ₹1000:", bank_fee(1000))

@lru_cache(maxsize=None)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

print("Factorial:", factorial(5))


# 7. REGEX: VALIDATE A TRANSACTION REFERENCE
reference = "TXN12345"

if re.fullmatch(r"TXN\d{5}", reference):
    print("Valid transaction reference")
else:
    print("Invalid transaction reference")


# 8. JSON: SAVE AND LOAD DATA
json_file = folder / "transactions.json"

json_file.write_text(json.dumps(transactions, indent=4))

loaded_data = json.loads(json_file.read_text())

print("Loaded JSON records:", len(loaded_data))


# 9. CSV: EXPORT A REPORT
csv_file = folder / "transactions.csv"

with csv_file.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["type", "amount"]
    )
    writer.writeheader()
    writer.writerows(transactions)

with csv_file.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("CSV records:", list(reader))


# 10. LOGGING: RECORD PROGRAM EVENTS
log_file = folder / "app.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler()
    ],
    force=True
)

logging.info("Bank report generated successfully")
logging.warning("Sample warning message")


# 11. SHUTIL: CREATE A ZIP BACKUP
archive = shutil.make_archive(
    "bank_report_backup",
    "zip",
    root_dir=folder
)

print("Backup created:", archive)

