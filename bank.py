"""
HARVARD CS50 PYTHON - Week 8: OOP — Properties & Encapsulation
================================================================
Concepts: @property (getter), encapsulation, _private convention, bank account example

Author: David J. Malan (CS50)
Learning Level: Advanced | Best Practice: ✅
"""


class Account:
    """
    A simple bank account demonstrating encapsulation and properties.

    💡 Encapsulation = hiding internal data and providing controlled access
    💡 _balance = "protected" attribute (convention: don't access directly)
    💡 @property = read-only access to internal data
    """

    def __init__(self) -> None:
        """Initialize account with zero balance."""
        self._balance = 0   # 💡 _ prefix = "please don't touch this directly"

    @property
    def balance(self) -> int:
        """Get current balance (read-only property).

        💡 This is a GETTER — provides controlled READ access
        💡 Called as account.balance (without parentheses!)
        """
        return self._balance

    def deposit(self, n: int) -> None:
        """Deposit money into account.

        Args:
            n: Amount to deposit (must be positive)
        """
        if n <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += n
        print(f"✅ Deposited ${n}")

    def withdraw(self, n: int) -> None:
        """Withdraw money from account.

        Args:
            n: Amount to withdraw (must not exceed balance)
        """
        if n <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if n > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= n
        print(f"💰 Withdrew ${n}")


def main() -> None:
    """Demonstrate bank account operations."""
    account = Account()

    print(f"💳 Starting balance: ${account.balance}")

    account.deposit(100)
    print(f"💳 Current balance: ${account.balance}")

    account.withdraw(50)
    print(f"💳 Final balance: ${account.balance}")

    # 💡 This would fail because there's no setter for balance:
    # account.balance = 1000  # AttributeError!


if __name__ == "__main__":
    main()


# 💡 KEY TAKEAWAYS:
#   ✅ @property = makes a method look like an attribute (no parentheses needed)
#   ✅ _variable = "protected" — convention, not enforced by Python
#   ✅ Properties allow READ-ONLY access (no setter = can't assign)
#   ✅ Encapsulation = protect data integrity (can't set negative balance)
#   ✅ Getters (@property) = controlled read access
#   ✅ To allow writes: use @balance.setter

