"""
HARVARD CS50 PYTHON - Week 2: Loops
=====================================
Concepts: while, for, range(), _, break, infinite loops, input validation

Author: David J. Malan (CS50)
Learning Level: Beginner → Intermediate | Best Practice: ✅
"""

# =============================================================================
# V1: While Loop with Counter — Manual increment
# =============================================================================
# i = 0
# while i < 3:
#     print("meow")
#     i += 1       # 💡 Don't forget this! Otherwise infinite loop!
# 💡 Must always increment (i += 1) or while loop runs forever

# =============================================================================
# V2: For Loop with range() — Cleaner iteration
# =============================================================================
# for i in range(3):
#     print("meow")
# 💡 for loops are SAFER — no risk of infinite loop!

# =============================================================================
# V3: For Loop with _ (underscore) — When variable is unused
# =============================================================================
# for _ in range(3):
#     print("meow")
# 💡 _ means "I don't need this variable" — convention for unused variables

# =============================================================================
# V4: Input Validation with while True / break
# =============================================================================
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break   # 💡 break exits the innermost loop
# for _ in range(n):
#     print("meow")

# =============================================================================
# BEST PRACTICE ✅: Function with validation + helper function
# =============================================================================

def get_number(prompt: str = "What's the number? ") -> int:
    """Get a positive integer from user.

    Args:
        prompt: Prompt message (default: "What's the number? ")

    Returns:
        A positive integer

    💡 Uses while True / break / return pattern:
       - Loop forever until valid input received
       - break/return exits both the loop AND the function
    """
    while True:
        n = int(input(prompt))
        if n > 0:
            return n    # 💡 return exits function AND loop immediately


def meow(n: int) -> None:
    """Print 'meow' n times.

    Args:
        n: Number of times to meow (must be positive)
    """
    for _ in range(n):
        print("meow")


def main() -> None:
    """Entry point: get number of meows and print them."""
    number = get_number()
    meow(number)


if __name__ == "__main__":
    main()


# 💡 KEY TAKEAWAYS:
#   ✅ for loops are SAFER than while (no infinite loop risk)
#   ✅ Use _ when you don't need the loop variable
#   ✅ while True + break = "validate until correct" pattern
#   ✅ return inside while True exits the function (and loop) immediately
#   ✅ Always validate user input before using it

