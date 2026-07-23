"""
HARVARD CS50 PYTHON - Week 8: OOP — Class Methods (Singleton-like Pattern)
============================================================================
Concepts: @classmethod, class variables, class-level operations, no instance needed

Author: David J. Malan (CS50)
Learning Level: Advanced | Best Practice: ✅
"""

import random


class Hat:
    """
    Sorting Hat — assigns people to houses.
    
    💡 @classmethod = method that works on the CLASS, not an instance
    💡 No __init__ needed! We NEVER create individual Hat objects
    💡 house is a CLASS VARIABLE (shared across all instances/uses)
    """

    # Class variable — shared by ALL uses of Hat
    # 💡 Defined OUTSIDE any method, belongs to the class itself
    houses = ["Ayodhya", "Vrindavan", "Mithila", "Barsana"]

    @classmethod
    def sort(cls, name: str) -> None:
        """Assign a person to a random house.

        Args:
            name: Name of the person to sort

        💡 cls = the class itself (Hat), not an instance
        💡 cls.houses accesses the class variable
        💡 Called as: Hat.sort("Ram") — no instance needed!
        """
        house = random.choice(cls.houses)
        print(f"{name} is in {house}")


# =============================================================================
# Usage — Note: NO object instantiation needed!
# =============================================================================
# 💡 We call Hat.sort() DIRECTLY on the class, not on an object
# 💡 Contrast with Student class where we create Student() objects

Hat.sort("Ram")
Hat.sort("Krishna")
Hat.sort("Sita")


# 💡 KEY TAKEAWAYS:
#   ✅ @classmethod = operates on class itself, not instances
#   ✅ cls = the class (like self but at class level)
#   ✅ Class variables = shared across all uses (defined outside methods)
#   ✅ No __init__ = we never create Hat objects (a design choice)
#   ✅ Useful for utility/helper classes that don't need state
#   ✅ Call with ClassName.method() directly
#   ✅ Contrast with instance methods: object.method()

