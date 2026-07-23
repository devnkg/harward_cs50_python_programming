"""
HARVARD CS50 PYTHON - Week 4: Creating Your Own Module
========================================================
Concepts: module creation, __name__ == "__main__", import, reusability

Author: David J. Malan (CS50)
Learning Level: Intermediate | Best Practice: ✅

💡 This file IS a module that can be IMPORTED by other files (like say.py)
💡 python3 saying.py → runs the main() function (test/demo code)
💡 from saying import hello → only imports the function, NOT main()
"""


def hello(name: str) -> None:
    """Print a hello greeting.

    Args:
        name: Name to greet
    """
    print(f"hello, {name}")


def goodbye(name: str) -> None:
    """Print a goodbye farewell.

    Args:
        name: Name to bid farewell
    """
    print(f"goodbye, {name}")


def main() -> None:
    """Demo function — runs only when this file is executed DIRECTLY."""
    hello("world")
    goodbye("world")


# 💡 THE MAGIC: if __name__ == "__main__"
#   - __name__ is a special variable
#   - When you run python3 saying.py → __name__ = "__main__"
#   - When you import saying → __name__ = "saying" (NOT "__main__")
#   - So main() only runs when EXECUTED directly, not when IMPORTED!
if __name__ == "__main__":
    main()


# 💡 KEY TAKEAWAYS:
#   ✅ The if __name__ == "__main__" guard is ESSENTIAL for reusable modules
#   ✅ Without it: importing runs the test/demo code automatically
#   ✅ With it: imported modules just define functions, don't run them
#   ✅ Always add this guard to every Python file with a main()
#   ✅ Test: python3 -c "from saying import hello; hello('CS50')"

