"""
HARVARD CS50 PYTHON - Week 2: Lists & Dictionaries
====================================================
Concepts: list, dict, for loops with lists, enumerate, dict iteration, list of dicts

Author: David J. Malan (CS50)
Learning Level: Beginner → Intermediate | Best Practice: ✅
"""

# =============================================================================
# V1: Basic List Iteration — Simple loop over list
# =============================================================================
# students = ["sita", "ram", "hari", "vishnu"]
# for student in students:
#     print(student)
# 💡 Lists are ordered, indexed [0], can be iterated with for

# =============================================================================
# V2: Indexed Iteration — Using range(len(list))
# =============================================================================
# students = ["sita", "ram", "hari", "vishnu"]
# for i in range(len(students)):
#     print(i + 1, students[i])
# 💡 len(list) = number of elements, range(len) = indices 0, 1, 2...
# 💡 Add 1 to i for human-readable numbering (1-indexed)

# =============================================================================
# V3: Dictionary Iteration — Key-value pairs
# =============================================================================
# names = {
#     "ram": "ayodhya",
#     "sita": "mithila",
#     "hari": "bhaktapur",
#     "vishnu": "vaikunth"
# }
# for name in names:
#     print(name, names[name], sep=", ")
# 💡 dict[key] = value — access value using its key
# 💡 for key in dict: iterates over KEYS (not values)

# =============================================================================
# BEST PRACTICE ✅: List of Dictionaries — Structured data
# =============================================================================

from typing import Optional


def main() -> None:
    """Display information about mythological figures."""
    # List of dictionaries — each dict = one data record
    gods: list[dict[str, Optional[str]]] = [
        {"name": "ram", "house": "ayodhya", "weapon": "bow"},
        {"name": "sita", "house": "mithila", "weapon": "lotus"},
        {"name": "krishna", "house": "vrindavan", "weapon": "flute"},
        {"name": "radha", "house": "barsana", "weapon": None},  # None = no value
    ]

    for god in gods:
        # 💡 dict access: god["keyname"]
        # 💡 sep=", " controls what goes between printed items
        print(god["name"], god["house"], god["weapon"], sep=", ")


if __name__ == "__main__":
    main()


# 💡 KEY TAKEAWAYS:
#   ✅ List = ordered collection: ["a", "b", "c"]
#   ✅ Dict = key-value pairs: {"key": "value"}
#   ✅ List of dicts = structured data (like a mini-database)
#   ✅ None = Python's way of saying "no value" (null)
#   ✅ enumerate(list) gives (index, value) pairs — cleaner than range(len())
#   ✅ Use sep="," in print() to control separator between values

