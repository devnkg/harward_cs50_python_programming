"""
HARVARD CS50 PYTHON - Week 1: Boolean Functions
=================================================
Concepts: bool, return, % (modulo), function design, clean boolean returns

Author: David J. Malan (CS50)
Learning Level: Beginner | Best Practice: ✅
"""


def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise.

    Args:
        n: Integer to check

    Returns:
        True if n is divisible by 2, False otherwise

    Examples:
        >>> is_even(4)
        True
        >>> is_even(7)
        False
    """
    # V1: Verbose (Not Pythonic)
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False
    # 💡 This works but is TOO VERBOSE. Don't do if/else for booleans!

    # BEST PRACTICE ✅: Return the boolean expression directly
    return n % 2 == 0

    # 💡 n % 2 evaluates to 0 or 1 (0 = even, 1 = odd)
    # 💡 n % 2 == 0 evaluates to True or False directly
    # 💡 No need for if/else — just return the condition!


def main() -> None:
    """Get number from user and display if it's even or odd."""
    x = int(input("What's x? "))

    if is_even(x):
        print("Even")
    else:
        print("Odd")


if __name__ == "__main__":
    main()


# 💡 KEY TAKEAWAYS:
#   ✅ % (modulo) gives remainder — n % 2 == 0 means even
#   ✅ NEVER do: if condition: return True else: return False
#   ✅ ALWAYS: return condition (the boolean expression directly)
#   ✅ Boolean functions make code readable: "if is_even(x):"

