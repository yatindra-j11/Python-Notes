# ==========================================
# PHASE 9: ADVANCED PYTHON DEMO
# Mini Banking System
# ==========================================

from dataclasses import dataclass,field
from functools import wraps
from contextlib import contextmanager

# 1. DATACLASS
@dataclass
class Transaction:
    transaction_type: str
    amount: float

# 2. DECORATOR
def log_transaction(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# 3. CONTEXT MANAGER
@contextmanager
def transaction_session():
    print("Transaction session started")
    try:
        yield
    finally:
        print("Transaction session closed")


class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance
        self.transactions = []

    # 4. DECORATOR IN USE
    @log_transaction
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.balance += amount
        self.transactions.append(
            Transaction("Deposit", amount)
        )

    # 5. GENERATOR
    def transaction_history(self):
        for transaction in self.transactions:
            yield transaction

    # 6. DUNDER METHODS
    def __str__(self):
        return f"{self.holder}: ₹{self.balance}"

    def __len__(self):
        return len(self.transactions)

    def __getitem__(self, index):
        return self.transactions[index]

    def __add__(self, other):
        return self.balance + other.balance


# 7. CLOSURE
def create_discount(rate):
    def apply_discount(amount):
        return amount * (1 - rate)
    return apply_discount


# 8. ITERATORS
account = BankAccount("Yatindra", 1000)

account.deposit(500)
account.deposit(200)

iterator = iter(account.transactions)
print(next(iterator))
print()


# 9. CONTEXT MANAGER IN USE
with transaction_session():
    account.deposit(300)

print()


# 10. GENERATOR IN USE
for transaction in account.transaction_history():
    print(transaction)

print()


# 11. DUNDER METHODS IN USE
print(account)           # __str__()
print(len(account))     # __len__()
print(account[0])       # __getitem__()

another_account = BankAccount("Rahul", 2000)
print(account + another_account)  # __add__()

print()


# 12. CLOSURE IN USE
discount = create_discount(0.10)
print(discount(1000))   # 900.0
