# ==========================================
# PHASE 6: FILE HANDLING DEMO
# Bank Transaction Manager
# ==========================================

import csv
import json

# 1. WRITE: creates a file or overwrites it
with open("transactions.txt", "w", encoding="utf-8") as f:
    f.write("Deposit: 1000\n")
    f.write("Withdrawal: 200\n")
    f.writelines(["Deposit: 500\n", "Withdrawal: 100\n"])


# 2. APPEND: adds content without erasing existing data
with open("transactions.txt", "a", encoding="utf-8") as f:
    f.write("Deposit: 300\n")


# 3. READ: entire file, lines, and iteration
with open("transactions.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print("Complete file:\n", data)

with open("transactions.txt", "r", encoding="utf-8") as f:
    print("First line:", f.readline().strip())
    print("Remaining lines:", f.readlines())

with open("transactions.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())


# 4. FILE POINTER: tell() and seek()
with open("transactions.txt", "r", encoding="utf-8") as f:
    print("Initial position:", f.tell())
    print("Read:", f.read(7))
    print("Current position:", f.tell())
    f.seek(0)
    print("After resetting:", f.read(7))


# 5. CSV: tabular transaction data
transactions = [
    ["Type", "Amount"],
    ["Deposit", 1000],
    ["Withdrawal", 200],
    ["Deposit", 500],
]

with open("transactions.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(transactions)

with open("transactions.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# 6. CSV WITH DICTIONARIES
records = [
    {"type": "Deposit", "amount": 1000},
    {"type": "Withdrawal", "amount": 200},
]

with open("records.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f, fieldnames=["type", "amount"]
    )
    writer.writeheader()
    writer.writerows(records)

with open("records.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for record in reader:
        print(record["type"], record["amount"])


# 7. JSON: save and load structured data
account = {
    "holder": "Yatindra",
    "balance": 1200,
    "active": True
}

with open("account.json", "w", encoding="utf-8") as f:
    json.dump(account, f, indent=4)

with open("account.json", "r", encoding="utf-8") as f:
    loaded_account = json.load(f)

print("Loaded account:", loaded_account)

# String conversion without files
json_string = json.dumps(account)
python_object = json.loads(json_string)
print(python_object)


# 8. BINARY MODE: read bytes
with open("transactions.txt", "rb") as f:
    content = f.read()
    print("Binary content:", content)


# 9. FLUSH: push buffered data to the underlying stream
with open("flush_demo.txt", "w", encoding="utf-8") as f:
    f.write("Transaction saved")
    f.flush()
    print("Data flushed")

