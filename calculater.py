"""
HARVARD CS50 PYTHON - Week 0: Functions & Variables (Advanced)
===============================================================
Concepts: int, float, input(), type conversion, round(), pow(), def, return

Author: David J. Malan (CS50)
Learning Level: Beginner → Intermediate | Best Practice: ✅
"""

# =============================================================================
# V1: Basic Integer Addition — Understanding int() conversion
# =============================================================================
# x = input("What's x? ")
# y = input("What's y? ")
# z = int(x) + int(y)
# print(z)
# 💡 input() always returns a STRING. int() converts string → integer.

# =============================================================================
# V2: Chained Type Conversion — More compact
# =============================================================================
# x = int(input("What's x? "))
# y = int(input("What's y? "))
# print(x + y)
# 💡 Nesting int(input()) is efficient but less readable at first.

# =============================================================================
# V3: One-liner (Not Recommended) — Too compact, hard to read
# =============================================================================
# print(int(input("what's x? ")) + int(input("what's y? ")))
# 💡 Avoid this! Code should be readable first.

# =============================================================================
# V4: Working with Floats — Decimal numbers & rounding
# =============================================================================
# x = float(input("What's x? "))
# y = float(input("What's y? "))
# print(x + y)                      # Full float output
# print(round(x + y))               # Round to nearest integer
# print(round(x + y, 2))            # Round to 2 decimal places
# print(f"{x + y:.2f}")             # Format to 2 decimal places with f-string

# 💡 round(number, ndigits) — ndigits = decimal places to round to
# 💡 f"{value:.2f}" — Always shows 2 decimal places (e.g., 5.00)

# =============================================================================
# V5: Division — How / works with floats
# =============================================================================
# x = float(input("What's x? "))
# y = float(input("What's y? "))
# z = x / y
# print(f"{z}")

# =============================================================================
# BEST PRACTICE ✅: Custom Function with pow() — Reusable & Testable
# =============================================================================

def square(n: float) -> float:
    """
    Calculate the square of a number.

    Args:
        n: Number to square

    Returns:
        n raised to the power of 2

    Examples:
        >>> square(5)
        25
        >>> square(2.5)
        6.25
    """
    return pow(n, 2)      # Also works: n ** 2, n * n

    # 💡 Alternative implementations:
    #   return n ** 2     # Using exponentiation operator
    #   return n * n      # Using multiplication (fastest for integers)


def main() -> None:
    """Entry point: gets number and prints its square."""
    x = int(input("What's x? "))
    print(f"x squared is {square(x)}")


if __name__ == "__main__":
    main()

# 💡 KEY TAKEAWAYS:
#   ✅ pow(n, 2) or n ** 2 for squaring (pow is more readable)
#   ✅ int() for whole numbers, float() for decimals
#   ✅ round(number, 2) controls decimal precision
#   ✅ f"{value:.2f}" formats to exactly 2 decimal places
#   ✅ Always put reusable logic in functions (testable!)

# 🔬 Try this:
#   python3 -c "from calculater import square; print(square(12))"

