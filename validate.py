"""
HARVARD CS50 PYTHON - Week 7: Regular Expressions (Email Validation)
======================================================================
Concepts: re.search(), regex patterns, \w, character classes, re.IGNORECASE, anchors

Author: David J. Malan (CS50)
Learning Level: Advanced | Best Practice: ✅
"""

import re


def validate_email(email: str) -> bool:
    """Validate an email address using regex.

    Args:
        email: Email address to validate

    Returns:
        True if email is valid, False otherwise

    Examples:
        >>> validate_email("user@harvard.edu")
        True
        >>> validate_email("user@example.com")
        True
        >>> validate_email("user@example.org")
        False  # (only .edu and .com allowed)
    """
    # =========================================================================
    # V1: Basic string check (no regex)
    # =========================================================================
    # if "@" in email and "." in email:
    #     return True
    # 💡 Too simple — "invalid@email" would pass!

    # =========================================================================
    # V2: Simple regex — Still not robust enough
    # =========================================================================
    # if re.search(r".+@.+\.edu", email):
    #     return True
    # 💡 Better but doesn't check start/end, only .edu allowed

    # =========================================================================
    # BEST PRACTICE ✅: Robust regex with proper anchors
    # =========================================================================
    # 💡 Regex: ^\w+@(\w+\.)?\w+\.(edu|com)$
    #    ^ = start of string (no characters before email)
    #    \w+ = one or more word chars (letters, digits, underscore)
    #    @ = literal @ symbol
    #    (\w+\.)? = optional subdomain (e.g., "mail." in "user@mail.harvard.edu")
    #    \w+ = domain name
    #    \. = literal dot (escaped)
    #    (edu|com) = only allow .edu or .com TLDs
    #    $ = end of string (no characters after email)
    #    re.IGNORECASE = case doesn't matter

    if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com)$", email, re.IGNORECASE):
        return True

    return False


def main() -> None:
    """Get email from user and validate it."""
    email = input("What's your email? ").strip()

    if validate_email(email):
        print("✅ Valid email address")
    else:
        print("❌ Invalid email address")


if __name__ == "__main__":
    main()


# 💡 KEY TAKEAWAYS:
#   ✅ ^ and $ = anchors — match must cover ENTIRE string
#   ✅ \w = word character: [a-zA-Z0-9_]
#   ✅ \w+ = one or more word characters
#   ✅ (pattern)? = optional group (zero or one occurrence)
#   ✅ (?: ) = non-capturing group (if you don't need to extract)
#   ✅ re.IGNORECASE = case-insensitive matching
#   ✅ \. = escaped dot (literal period, not wildcard)
#   ✅ | inside () = OR: .edu OR .com

