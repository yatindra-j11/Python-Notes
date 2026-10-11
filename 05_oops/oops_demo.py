# ============================================================
# PYTHON OOP DEMO — MINI BANKING SYSTEM
# ============================================================

# ------------------------------------------------------------
# 1. CLASS + OBJECT + CONSTRUCTOR + ATTRIBUTES
# ------------------------------------------------------------

class BankAccount:
    # Class variable
    bank_name = "ABC Bank"

    # Constructor
    def __init__(self, account_holder, balance):
        # Instance variables
        self.account_holder = account_holder
        self.balance = balance

    # Instance method
    def show_details(self):
        print(f"Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


# Creating objects
account1 = BankAccount("Yatindra", 10000)
account2 = BankAccount("Rahul", 5000)

account1.show_details()
account2.show_details()

print()


# ------------------------------------------------------------
# 2. INSTANCE VARIABLES vs CLASS VARIABLES
# ------------------------------------------------------------

print(account1.account_holder)   # Unique to account1
print(account2.account_holder)   # Unique to account2

# Both objects access the same class variable
print(account1.bank_name)
print(account2.bank_name)

print()


# ------------------------------------------------------------
# 3. INSTANCE METHODS
# ------------------------------------------------------------

class Account:
    bank_name = "ABC Bank"

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"{self.holder}'s balance: {self.balance}")


account = Account("Yatindra", 10000)

account.deposit(2000)
account.withdraw(3000)
account.show_balance()

print()


# ------------------------------------------------------------
# 4. CLASS METHOD
# ------------------------------------------------------------

class Bank:
    bank_name = "ABC Bank"
    total_accounts = 0

    def __init__(self, name):
        self.name = name
        Bank.total_accounts += 1

    @classmethod
    def show_total_accounts(cls):
        print(f"Total accounts: {cls.total_accounts}")


a1 = Bank("Yatindra")
a2 = Bank("Rahul")
a3 = Bank("Aman")

Bank.show_total_accounts()

print()


# ------------------------------------------------------------
# 5. STATIC METHOD
# ------------------------------------------------------------

class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    @staticmethod
    def is_valid_account_number(account_number):
        return len(account_number) == 10 and account_number.isdigit()


print(BankAccount.is_valid_account_number("1234567890"))  # True
print(BankAccount.is_valid_account_number("12345"))       # False

print()


# ------------------------------------------------------------
# 6. INHERITANCE + METHOD OVERRIDING
# ------------------------------------------------------------

class SavingsAccount:
    def withdraw(self, amount):
        print("Withdrawal from savings account")


class CurrentAccount:
    def withdraw(self, amount):
        print("Withdrawal from current account")


class PremiumSavingsAccount(SavingsAccount):
    # Method overriding
    def withdraw(self, amount):
        print("Premium savings withdrawal")


savings = SavingsAccount()
current = CurrentAccount()
premium = PremiumSavingsAccount()

savings.withdraw(1000)
current.withdraw(1000)
premium.withdraw(1000)

print()


# ------------------------------------------------------------
# 7. POLYMORPHISM
# ------------------------------------------------------------

# Different objects respond to the same method name
accounts = [
    SavingsAccount(),
    CurrentAccount(),
    PremiumSavingsAccount()
]

for account in accounts:
    account.withdraw(1000)

print()


# ------------------------------------------------------------
# 8. ENCAPSULATION
# ------------------------------------------------------------

class SecureAccount:

    def __init__(self, holder, balance):
        self.holder = holder

        # "Protected" by convention
        self._account_type = "Savings"

        # Name-mangled "private" attribute
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal")

    def get_balance(self):
        return self.__balance


account = SecureAccount("Yatindra", 10000)

account.deposit(2000)
account.withdraw(3000)

print(account.get_balance())

# Direct access is discouraged / prevented by name mangling:
# print(account.__balance)   # AttributeError

print()


# ------------------------------------------------------------
# 9. ABSTRACTION
# ------------------------------------------------------------

from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Card(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")


# PaymentMethod cannot be instantiated directly
# payment = PaymentMethod()  # TypeError

upi = UPI()
card = Card()

upi.pay(500)
card.pay(1000)

print()


# ------------------------------------------------------------
# 10. MULTIPLE INHERITANCE
# ------------------------------------------------------------

class AccountHolder:
    def show_holder(self):
        print("Account holder information")


class TransactionService:
    def make_transaction(self):
        print("Transaction completed")


class CustomerAccount(AccountHolder, TransactionService):
    pass


customer = CustomerAccount()

customer.show_holder()
customer.make_transaction()

print()


# ------------------------------------------------------------
# 11. METHOD RESOLUTION ORDER (MRO)
# ------------------------------------------------------------

print(CustomerAccount.__mro__)

# Or:
print(CustomerAccount.mro())

print()


# ------------------------------------------------------------
# 12. COMBINING EVERYTHING
# ------------------------------------------------------------

from abc import ABC, abstractmethod


class BankAccount(ABC):

    bank_name = "ABC Bank"

    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    # Encapsulated access to balance
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ₹{amount}")

    @abstractmethod
    def withdraw(self, amount):
        pass

    @staticmethod
    def validate_amount(amount):
        return amount > 0


class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        if not self.validate_amount(amount):
            print("Invalid amount")
        elif amount <= self.get_balance():
            # We cannot directly modify __balance here because
            # it is private to BankAccount.
            print(f"Withdrawing ₹{amount} from savings account")
        else:
            print("Insufficient balance")


class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        if amount <= self.get_balance():
            print(f"Withdrawing ₹{amount} from current account")
        else:
            print("Insufficient balance")


# Objects of child classes
savings = SavingsAccount("Yatindra", 10000)
current = CurrentAccount("Rahul", 20000)

savings.deposit(2000)
savings.withdraw(5000)

current.withdraw(10000)

print()


# ------------------------------------------------------------
# 13. POLYMORPHISM WITH ABSTRACT CLASS
# ------------------------------------------------------------

accounts = [
    SavingsAccount("Yatindra", 10000),
    CurrentAccount("Rahul", 20000)
]

for account in accounts:
    account.withdraw(5000)

print()


# ------------------------------------------------------------
# OOP CONCEPT SUMMARY
# ------------------------------------------------------------

"""
CLASS
    BankAccount is a blueprint for creating bank accounts.

OBJECT
    savings and current are objects/instances of their classes.

CONSTRUCTOR
    __init__() initializes an object's data.

ATTRIBUTES
    holder, balance, bank_name etc.

INSTANCE VARIABLE
    self.holder
    Each object has its own value.

CLASS VARIABLE
    bank_name
    Shared through the class.

INSTANCE METHOD
    deposit(), withdraw(), get_balance()
    Works with object/instance data.

CLASS METHOD
    @classmethod
    Works with class-level data using cls.

STATIC METHOD
    @staticmethod
    Does not need self or cls.

INHERITANCE
    SavingsAccount and CurrentAccount inherit from BankAccount.

METHOD OVERRIDING
    Both child classes provide their own withdraw() implementation.

POLYMORPHISM
    Different account objects can respond to withdraw()
    through the same interface.

ENCAPSULATION
    __balance is hidden inside BankAccount and accessed
    through methods.

ABSTRACTION
    BankAccount defines the required withdraw() interface
    using @abstractmethod.

MULTIPLE INHERITANCE
    CustomerAccount inherits from AccountHolder and
    TransactionService.

MRO
    Python uses MRO to determine the order in which classes
    are searched for methods and attributes.
"""
