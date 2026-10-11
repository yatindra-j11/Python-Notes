# ==========================================
# PHASE 7: EXCEPTION HANDLING DEMO
# Mini Banking System
# ==========================================

# 1. Custom exception
class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):
    try:
        # 2. Raise exceptions manually
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > balance:
            raise InsufficientBalanceError(
                "Insufficient balance"
            )

        balance -= amount

    except (ValueError, InsufficientBalanceError) as e:
        print(f"Transaction failed: {e}")

    else:
        # Runs only when try completes successfully
        print("Withdrawal successful")

    finally:
        # Runs whether an exception occurs or not
        print("Transaction processing completed")

    return balance


balance = 5000

balance = withdraw(balance, 1000)
print("Balance:", balance)

balance = withdraw(balance, 6000)
print("Balance:", balance)

balance = withdraw(balance, -100)
print("Balance:", balance)

