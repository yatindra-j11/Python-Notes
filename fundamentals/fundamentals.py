# ==========================================
# PYTHON FUNDAMENTALS — DEMO
# ==========================================

# 1. Variables, data types, operators
name = "Yatindra"
balance = 1000.0
active = True

balance += 500

print(f"{name}: ₹{balance}")
print(type(balance), active)


# 2. Input, type conversion, conditional statements
amount = int(input("Enter withdrawal amount: "))

if 0 < amount <= balance:
    balance -= amount
    print(f"Remaining balance: ₹{balance}")
else:
    print("Invalid amount or insufficient balance")


# 3. Loops
transactions = [200, -100, 500]

for transaction in transactions:
    print(transaction)


# 4. Data structures and comprehensions
customer = {
    "name": name,
    "balance": balance,
    "active": active
}

positive_transactions = [
    t for t in transactions if t > 0
]

print(customer)
print(positive_transactions)


# 5. Functions, *args, **kwargs, lambda
def total(*amounts):
    return sum(amounts)

def customer_details(**details):
    return details

square = lambda x: x * x

print(total(100, 200, 300))
print(customer_details(name="Rahul", age=21))
print(square(5))


# 6. Higher-order functions
def apply_operation(func, value):
    return func(value)

print(apply_operation(square, 4))  # 16


# 7. Recursion
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120


# 8. Namespace and scope (LEGB)
x = 10  # Global

def show_scope():
    x = 20  # Local
    print("Local x:", x)

show_scope()
print("Global x:", x)

print(globals().get("x"))
