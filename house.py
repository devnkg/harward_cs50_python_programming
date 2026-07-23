"""
HARVARD CS50 PYTHON - Week 1: Match/Case (Switch Statement)
=============================================================
Concepts: match, case, | (OR pattern), _ (wildcard/default)

Author: David J. Malan (CS50)
Learning Level: Beginner → Intermediate | Best Practice: ✅
"""

# =============================================================================
# V1: Using if/elif/else — The traditional approach
# =============================================================================
# name = input("What's your name? ")
#
# if name == "Radha" or name == "Krishna" or name == "Balram":
#     print("Vrindavan")
# elif name == "Ram" or name == "Sita":
#     print("Ayodhya")
# elif name == "Shiva" or name == "Parvati":
#     print("Kailash")
# else:
#     print("Unknown")
# 💡 Works but repetitive — we repeat name == multiple times

# =============================================================================
# BEST PRACTICE ✅: Using match/case with | (OR) pattern
# =============================================================================

def find_location(name: str) -> str:
    """Match a name to their mythological location using match/case.

    Args:
        name: Name of the deity/person

    Returns:
        Location name, or 'Unknown' if not found
    """
    match name:
        case "Radha" | "Krishna" | "Balram":
            return "Vrindavan"
        case "Ram" | "Sita":
            return "Ayodhya"
        case "Shiva" | "Parvati":
            return "Kailash"
        case "Hanuman":
            return "Kishkindha"
        case _:  # Default / Wildcard — matches anything
            return "Unknown"


def main() -> None:
    """Get name and display their location."""
    name = input("What's your name? ").strip().title()
    print(find_location(name))


if __name__ == "__main__":
    main()

# 💡 KEY TAKEAWAYS:
#   ✅ match/case = Python's version of switch statement (Python 3.10+)
#   ✅ | means OR in pattern matching: case "A" | "B":
#   ✅ _ is the wildcard/default — matches ANYTHING (like default in switch)
#   ✅ match/case is CLEANER than long if/elif chains for discrete values
#   ✅ Use for specific values, NOT for ranges (use if/elif for ranges)

