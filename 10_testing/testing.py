# ==========================================
# PHASE 14: TESTING DEMO
# Banking System Testing
# ==========================================

# INSTALLATION:
# pip install pytest

# RUN PYTEST TESTS:
# pytest -v

import unittest
import pytest
from unittest.mock import Mock, patch


# ==========================================
# APPLICATION CODE
# ==========================================

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance


class NotificationService:
    def send_notification(self, message):
        print("Notification sent:", message)


def transfer_money(sender, receiver, amount, notification_service):
    sender.withdraw(amount)
    receiver.deposit(amount)
    notification_service.send_notification(
        f"{amount} transferred successfully"
    )


# ==========================================
# 1. UNITTEST — BASIC UNIT TESTING
# ==========================================

class TestBankAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nStarting unittest cases")

    def setUp(self):
        self.account = BankAccount("Aman", 5000)

    def tearDown(self):
        pass

    def test_deposit(self):
        self.account.deposit(1000)
        self.assertEqual(self.account.get_balance(), 6000)

    def test_withdrawal(self):
        self.account.withdraw(1000)
        self.assertEqual(self.account.get_balance(), 4000)

    def test_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(6000)

    def test_invalid_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    @classmethod
    def tearDownClass(cls):
        print("Unittest cases completed")


# ==========================================
# 2. PYTEST — BASIC TESTING WITH ASSERT
# ==========================================

def test_pytest_deposit():
    account = BankAccount("Rahul", 3000)
    account.deposit(1000)
    assert account.get_balance() == 4000


def test_pytest_withdrawal():
    account = BankAccount("Rahul", 3000)
    account.withdraw(500)
    assert account.get_balance() == 2500


# ==========================================
# 3. FIXTURES — REUSABLE TEST SETUP
# ==========================================

@pytest.fixture
def account():
    # Setup
    account = BankAccount("Aman", 5000)

    yield account

    # Teardown
    print("Test completed")


def test_fixture_deposit(account):
    account.deposit(1000)
    assert account.get_balance() == 6000


# ==========================================
# 4. PARAMETRIZATION — MULTIPLE TEST CASES
# ==========================================

@pytest.mark.parametrize("amount, expected", [
    (100, 5100),
    (500, 5500),
    (1000, 6000),
])
def test_multiple_deposits(amount, expected):
    account = BankAccount("Aman", 5000)
    account.deposit(amount)
    assert account.get_balance() == expected


# ==========================================
# 5. MOCKING — FAKE EXTERNAL SERVICES
# ==========================================

def test_transfer_with_mock(account):
    receiver = BankAccount("Rahul", 2000)

    mock_service = Mock()

    transfer_money(account, receiver, 1000, mock_service)

    assert account.get_balance() == 4000
    assert receiver.get_balance() == 3000

    mock_service.send_notification.assert_called_once_with(
        "1000 transferred successfully"
    )


# ==========================================
# 6. PATCHING — TEMPORARILY REPLACE OBJECTS
# ==========================================

def test_notification_patch(account):
    receiver = BankAccount("Rahul", 2000)

    with patch.object(
        NotificationService,
        "send_notification"
    ) as mock_notification:

        service = NotificationService()
        transfer_money(account, receiver, 500, service)

        mock_notification.assert_called_once_with(
            "500 transferred successfully"
        )


# ==========================================
# 7. EXCEPTION TESTING
# ==========================================

def test_invalid_withdrawal(account):
    with pytest.raises(ValueError, match="Insufficient balance"):
        account.withdraw(10000)


# ==========================================
# RUN UNITTEST TESTS
# ==========================================

if __name__ == "__main__":
    unittest.main()