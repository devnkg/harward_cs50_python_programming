"""
HARVARD CS50 PYTHON - Week 3: Exceptions
==========================================
Concepts: try, except, ValueError, else, pass, raise, exception handling patterns

Author: David J. Malan (CS50)
Learning Level: Intermediate | Best Practice: ✅
"""

# =============================================================================
# V1: No Error Handling — Crashes on invalid input
# =============================================================================
# x = int(input("What's x? "))
# print(f"x is {x}")
# 💡 If user types "cat", program crashes with ValueError!

# =============================================================================
# V2: Basic try/except — Catches error, shows message
# =============================================================================
# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not a valid integer")
# 💡 try: code that might fail
# 💡 except: code to run if error occurs

# =============================================================================
# V3: Loop Until Valid — Keep asking until correct
# =============================================================================
# while True:
#     try:
#         x = int(input("What's x? "))
#         break   # 💡 Only runs if no error
#     except ValueError:
#         print("Invalid!")
# print(f"x is {x}")
# 💡 break ONLY reached if int() succeeds (no exception thrown)

# =============================================================================
# V4: Using else — Separates success from error handling
# =============================================================================
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("Invalid!")
#     else:
#         break   # 💡 else runs ONLY if try succeeded
# print(f"x is {x}")

# =============================================================================
# BEST PRACTICE ✅: Function with clean try/except/return pattern
# =============================================================================

def get_int(prompt: str = "What's x? ") -> int:
    """Prompt user for an integer, retrying until valid input.

    Args:
        prompt: The prompt message to display (default: "What's x? ")

    Returns:
        A valid integer from user input

    💡 Pattern: while True + try/except + return
       - return exits BOTH the loop AND the function
       - pass means "do nothing" — just retry silently
    """
    while True:
        try:
            return int(input(prompt))   # Returns immediately (no need for break)
        except ValueError:
            pass    # 💡 pass = silently ignore and retry
            # 💡 Alternative: print("Invalid!") for user feedback


def main() -> None:
    """Get integer from user and display it."""
    x = get_int("What's x? ")
    print(f"x is {x}")


if __name__ == "__main__":
    main()


# 💡 KEY TAKEAWAYS:
#   ✅ Always handle ValueError when converting user input
#   ✅ try/except catches errors without crashing
#   ✅ return inside try = clean exit from function + loop
#   ✅ pass = "do nothing" (silent retry)
#   ✅ else block runs ONLY if try succeeded
#   ✅ Specific except (except ValueError) is better than bare except

