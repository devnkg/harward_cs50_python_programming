"""
HARVARD CS50 PYTHON - Week 4: Libraries (Importing Modules & Packages)
=======================================================================
Concepts: from X import Y, sys.argv, packages (cowsay), module imports

Author: David J. Malan (CS50)
Learning Level: Intermediate | Best Practice: ✅
"""

import sys
import cowsay
from saying import hello, goodbye   # 💡 Import from OUR custom module!


def main() -> None:
    """Demonstrate importing from both custom modules and packages."""
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 say.py <name>")

    name = sys.argv[1]

    # V1: Using the cowsay package (fun text art)
    # 💡 cowsay is a THIRD-PARTY package from PyPI
    # 💡 Install: pip install cowsay
    print("\n🐄 Cowsay says:")
    cowsay.trex(f"Hello, {name}!")

    # V2: Using our custom module (saying.py)
    print("\n📢 Custom module says:")
    hello(name)
    goodbye(name)


if __name__ == "__main__":
    main()


# 💡 KEY TAKEAWAYS:
#   ✅ from saying import hello — import from YOUR OWN files
#   ✅ import cowsay — third-party packages from PyPI
#   ✅ Two types of imports:
#       1. from module import specific_function
#       2. import module (then use module.function())
#   ✅ sys.argv for command-line arguments
#   ✅ pip install cowsay → install packages from PyPI

