"""
HARVARD CS50 PYTHON - Week 0: Functions & Variables
====================================================
Concepts: input(), print(), f-strings, strip(), title(), def, return, __name__

Author: David J. Malan (CS50)
Learning Level: Beginner | Best Practice: ✅
"""

# =============================================================================
# V1: Basic Concatenation — Understand string joining with +
# =============================================================================
# name = input("What is your name? ")
# print("Hello, " + name)
# 💡 The + operator joins (concatenates) strings together

# =============================================================================
# V2: Clean Input & Comma Separation — Using string methods
# =============================================================================
# name = input("What is your name? ").strip().title()
# print("Hello,", name)
# 💡 strip() removes whitespace, title() capitalizes first letter of each word
# 💡 print() with comma adds a space automatically between arguments

# =============================================================================
# V3: f-strings (Formatted Strings) — Clean & readable
# =============================================================================
# name = input("What is your name? ").strip().title()
# print(f"Hello, {name}")
# 💡 f-strings let you embed variables directly in string with {variable}

# =============================================================================
# BEST PRACTICE ✅: Functions with Default Parameters & Module Guard
# =============================================================================

def hello(to: str = "World") -> str:
    """
    Returns a greeting string.

    Args:
        to: Name to greet (default: "World")

    Returns:
        Formatted greeting string e.g. "Hello, World"
    """
    return f"Hello, {to}"


def main() -> None:
    """Entry point: gets user input and prints greeting."""
    name = input("What's your name? ").strip().title()
    print(hello(name))


if __name__ == "__main__":
    main()

# 💡 KEY TAKEAWAYS:
#   ✅ f"Hello, {name}" is BEST PRACTICE for string formatting
#   ✅ Always use if __name__ == "__main__": main() for reusable modules
#   ✅ Default parameters: def hello(to="World") — used when no argument given
#   ✅ Type hints (-> str, -> None) improve code readability

# 🔬 Try this:
#   python3 -c "from hello import hello; print(hello('CS50'))"

