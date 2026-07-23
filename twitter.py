"""
HARVARD CS50 PYTHON - Week 7: Regular Expressions (URL Parsing)
=================================================================
Concepts: re.search(), groups, non-capturing groups (?:), optional groups, walrus :=

Author: David J. Malan (CS50)
Learning Level: Advanced | Best Practice: ✅
"""

import re


def extract_username(url: str) -> str | None:
    """Extract Twitter/X username from a URL.

    Args:
        url: Twitter URL (e.g., "https://twitter.com/username")

    Returns:
        Username string if found, None otherwise

    Examples:
        >>> extract_username("https://twitter.com/narendramodi")
        'narendramodi'
        >>> extract_username("http://www.twitter.com/nkg")
        'nkg'
        >>> extract_username("https://x.com/elonmusk")
        None  # (pattern only matches twitter.com)
    """
    # =========================================================================
    # V1: Basic string manipulation — Simple but fragile
    # =========================================================================
    # username = url.removeprefix("https://twitter.com/")
    # 💡 Breaks on: http://, www.twitter.com, trailing slashes

    # =========================================================================
    # BEST PRACTICE ✅: Robust regex with optional groups
    # =========================================================================
    # 💡 Regex: ^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)
    #    ^ = start of string
    #    https? = "http" OR "https" (s? = optional s)
    #    :// = literal
    #    (?:www\.)? = optional non-capturing group for "www."
    #    twitter\.com = literal (dot is escaped)
    #    / = literal slash
    #    ([a-z0-9_]+) = CAPTURE group: username (letters, digits, underscore)
    #    re.IGNORECASE = case-insensitive matching

    if matches := re.search(
        r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)",
        url,
        re.IGNORECASE,
    ):
        return matches.group(1)   # First (and only) capture group

    return None


def main() -> None:
    """Get URL from user and extract username."""
    url = input("URL: ").strip()

    username = extract_username(url)

    if username:
        print(f"Username: {username}")
    else:
        print("Invalid Twitter URL")


if __name__ == "__main__":
    main()


# 💡 KEY TAKEAWAYS:
#   ✅ (?:pattern) = NON-CAPTURING group (groups but doesn't save)
#   ✅ ?: inside () makes it non-capturing
#   ✅ s? = optional "s" (matches both http and https)
#   ✅ \. = escaped dot (literal period, not "any character")
#   ✅ [a-z0-9_]+ = character class for usernames
#   ✅ re.IGNORECASE = case doesn't matter
#   ✅ := walrus = assign and check in one step

