"""
HARVARD CS50 PYTHON - Week 4: Command-Line Arguments (sys.argv)
=================================================================
Concepts: sys, argv, sys.exit(), command-line arguments, slicing, iteration

Author: David J. Malan (CS50)
Learning Level: Intermediate | Best Practice: ✅
"""

import sys
from typing import List

# =============================================================================
# V1: Basic (Risky) — Crashes if no argument provided
# =============================================================================
# print("Hello, my name is", sys.argv[1])
# 💡 sys.argv[0] = script name (e.g., "name.py")
# 💡 sys.argv[1] = first argument
# 💡 If no argument given → IndexError! (list index out of range)

# =============================================================================
# V2: Error Handling with try/except
# =============================================================================
# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")
# 💡 try/except catches the error instead of crashing

# =============================================================================
# V3: Explicit Length Check with sys.exit()
# =============================================================================
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
# print("Hello, my name is", sys.argv[1])
# 💡 sys.exit(message) prints message AND exits the program

# =============================================================================
# BEST PRACTICE ✅: Handle multiple arguments with slicing
# =============================================================================

def greet(names: List[str]) -> None:
    """Greet all provided names.

    Args:
        names: List of names to greet
    """
    for name in names:
        print(f"Hello, my name is {name}")


def main() -> None:
    """Process command-line arguments and greet users."""
    # sys.argv[1:] = all arguments EXCEPT script name
    # 💡 [1:] = slice from index 1 to end

    if len(sys.argv) < 2:
        sys.exit("Usage: python3 name.py [name1] [name2] ...")

    # Process each argument
    greet(sys.argv[1:])   # Pass slice of all names


if __name__ == "__main__":
    main()


# 💡 KEY TAKEAWAYS:
#   ✅ sys.argv[0] = script name, sys.argv[1:] = actual arguments
#   ✅ [1:] = slice: start at index 1, go to end
#   ✅ sys.exit() exits the program (optionally with a message)
#   ✅ Always validate argument count before accessing argv
#   ✅ Use: python3 name.py Ram Sita Krishna

