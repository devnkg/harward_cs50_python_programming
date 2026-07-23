"""
HARVARD CS50 PYTHON - Week 1: Conditionals
============================================
Concepts: if, elif, else, comparison operators (==, !=, <, >), or

Author: David J. Malan (CS50)
Learning Level: Beginner | Best Practice: ✅
"""

# =============================================================================
# V1: Multiple Comparisons — Explicit if/elif/else
# =============================================================================
# x = int(input("What's x? "))
# y = int(input("What's y? "))
#
# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")
# 💡 elif = "else if" — Python's way of chaining conditions

# =============================================================================
# V2: Logical OR — Combining conditions
# =============================================================================
# if x < y or x > y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")
# 💡 or = at least one condition must be True

# =============================================================================
# V3: Not Equal (!=) — Direct inequality check
# =============================================================================
# if x != y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")
# 💡 != means "not equal" — simpler than combining < and >

# =============================================================================
# V4: Equal (==) — Direct equality check
# =============================================================================
# if x == y:
#     print("x is equal to y")
# else:
#     print("x is not equal to y")
# 💡 == checks equality (don't confuse with = which assigns!)

# =============================================================================
# BEST PRACTICE ✅: Choose the simplest condition
# =============================================================================

def main() -> None:
    """Compare two numbers and display the result."""
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    # Best Practice: Use the most direct comparison
    if x == y:
        print("x is equal to y")
    else:
        print("x is not equal to y")

    # 🔍 For specific comparisons (less/greater), use if/elif/else


if __name__ == "__main__":
    main()


# 💡 KEY TAKEAWAYS:
#   ✅ == checks equality, = assigns values
#   ✅ != checks inequality (best for "not equal" logic)
#   ✅ Choose the SIMPLEST condition that works
#   ✅ elif is more efficient than multiple if statements
#   ✅ or returns True if ANY condition is True

