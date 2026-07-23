"""
HARVARD CS50 PYTHON - Week 7: Regular Expressions (Name Formatting)
====================================================================
Concepts: re.search(), groups (), walrus operator :=, string manipulation

Author: David J. Malan (CS50)
Learning Level: Intermediate → Advanced | Best Practice: ✅
"""

import re


def format_name(name: str) -> str:
    """Convert 'Last, First' format to 'First Last' format.

    Args:
        name: Name in 'Last, First' format (e.g., "Malan, David")

    Returns:
        Formatted name as 'First Last' (e.g., "David Malan")

    Examples:
        >>> format_name("Malan, David")
        'David Malan'
        >>> format_name("Turing, Alan")
        'Alan Turing'
    """
    # =========================================================================
    # V1: Manual string split — Simple but limited
    # =========================================================================
    # if "," in name:
    #     last, first = name.split(", ")
    #     name = f"{first} {last}"
    # 💡 Works for EXACT format "Last, First" but breaks on "Last,First"

    # =========================================================================
    # BEST PRACTICE ✅: Regex with groups () and walrus operator :=
    # =========================================================================
    # 💡 Regex: ^(.+), *(.+)$
    #    ^ = start of string
    #    (.+) = capture group 1: one or more of any character
    #    , * = comma followed by zero or more spaces
    #    (.+) = capture group 2: one or more of any character
    #    $ = end of string
    #
    # 💡 := walrus operator = ASSIGN AND EVALUATE in one step
    #    if matches := re.search(...) → assigns result AND checks if truthy

    if matches := re.search(r"^(.+), *(.+)$", name):
        # matches.group(1) = "Malan", matches.group(2) = "David"
        name = matches.group(2) + " " + matches.group(1)

    return name


def main() -> None:
    """Get name from user and format it."""
    name = input("What's your name? ").strip()
    formatted = format_name(name)
    print(f"Hello, {formatted}")


if __name__ == "__main__":
    main()


# 💡 KEY TAKEAWAYS:
#   ✅ re.search() returns a Match object (or None if no match)
#   ✅ groups () capture parts of the match
#   ✅ .group(0) = entire match, .group(1) = first capture, etc.
#   ✅ := walrus operator: assigns and checks truthiness in one line
#   ✅ .+ means "one or more of any character" (greedy)
#   ✅ * means "zero or more of preceding" — ", *" = comma + optional spaces
#   ✅ ^ = start anchor, $ = end anchor

