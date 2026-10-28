# Phase 11 — Database Programming Demo

## 1. SQLite — Bank Account Management

import sqlite3

conn = sqlite3.connect("bank.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# CREATE TABLE
cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        balance REAL NOT NULL DEFAULT 0
    )
""")

# CREATE — Insert an account
cursor.execute(
    "INSERT INTO accounts (name, balance) VALUES (?, ?)",
    ("Aman", 5000)
)

# READ — Display accounts
cursor.execute("SELECT * FROM accounts")
for account in cursor.fetchall():
    print(account["name"], account["balance"])

# UPDATE — Deposit money
cursor.execute(
    "UPDATE accounts SET balance = balance + ? WHERE name = ?",
    (1000, "Aman")
)

# TRANSACTION — Withdraw money
try:
    with conn:
        cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE name = ?",
            (500, "Aman")
        )
except sqlite3.Error as e:
    print("Database error:", e)

# READ — Display updated balance
cursor.execute("SELECT * FROM accounts")
for account in cursor.fetchall():
    print(account["name"], account["balance"])

# DELETE (optional)
# cursor.execute("DELETE FROM accounts WHERE name = ?", ("Aman",))

conn.close()