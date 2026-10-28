from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["bank"]
accounts = db["accounts"]

# CREATE — Insert an account
accounts.insert_one({"name": "Aman", "balance": 5000})

# READ — Find accounts
for account in accounts.find({"name": "Aman"}):
    print(account["name"], account["balance"])

# UPDATE — Deposit money
accounts.update_one(
    {"name": "Aman"},
    {"$inc": {"balance": 1000}}
)

# QUERY — Find accounts with balance >= 5000
for account in accounts.find({"balance": {"$gte": 5000}}):
    print(account)

# AGGREGATION — Calculate total balance
result = accounts.aggregate([
    {"$group": {"_id": None, "total_balance": {"$sum": "$balance"}}}
])

for document in result:
    print("Total balance:", document["total_balance"])

# DELETE (optional)
# accounts.delete_one({"name": "Aman"})

client.close()