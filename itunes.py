"""
HARVARD CS50 PYTHON - Week 4: APIs & JSON (Requests Module)
=============================================================
Concepts: requests module, JSON parsing, API calls, error handling, sys.argv

Author: David J. Malan (CS50)
Learning Level: Advanced | Best Practice: ✅
"""

import requests
import sys
import json


def search_music(term: str) -> list[dict]:
    """Search Apple iTunes for songs matching the search term.

    Args:
        term: Search term (artist or song name)

    Returns:
        List of result dictionaries from the iTunes API

    💡 API Endpoint: https://music.apple.com/search
    💡 Parameters: entity=song (search songs), limit=50 (max results), term=query
    """
    # Build the API URL
    url = f"https://music.apple.com/search?entity=song&limit=50&term={term}"

    # Make the API request
    response = requests.get(url)

    # Check for HTTP errors
    response.raise_for_status()  # 💡 Raises exception for 4xx/5xx errors

    # Parse JSON response into Python dictionary
    data = response.json()

    return data.get("results", [])  # 💡 .get() with default = safe access


def main() -> None:
    """Search iTunes for songs and display results."""
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 itunes.py <search-term>")

    search_term = sys.argv[1]

    try:
        results = search_music(search_term)

        if not results:
            print(f"No results found for '{search_term}'")
            return

        print(f"\n🎵 Songs matching '{search_term}':")
        print("-" * 40)

        for i, result in enumerate(results, 1):
            # 💡 Access nested JSON keys safely
            track = result.get("trackName", "Unknown Track")
            artist = result.get("artistName", "Unknown Artist")
            collection = result.get("collectionName", "Unknown Album")

            print(f"{i:2d}. {track}")
            print(f"    Artist: {artist}")
            print(f"    Album:  {collection}")
            print()

        print(f"Found {len(results)} results")

    except requests.exceptions.RequestException as e:
        print(f"❌ API Error: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ JSON Parse Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()


# 💡 KEY TAKEAWAYS:
#   ✅ requests.get(url) = make HTTP GET request
#   ✅ response.json() = parse response as JSON → Python dict
#   ✅ dict.get("key", "default") = safe access with fallback
#   ✅ response.raise_for_status() = check for HTTP errors
#   ✅ Always handle API errors with try/except
#   ✅ Use f-strings to build API URLs with parameters
#   ✅ API keys: iTunes API is free (no key needed!)

