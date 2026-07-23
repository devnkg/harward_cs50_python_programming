"""
HARVARD CS50 PYTHON - Week 8: Object-Oriented Programming (OOP)
=================================================================
Concepts: class, __init__, __str__, @property, @*.setter, @classmethod, encapsulation

Author: David J. Malan (CS50)
Learning Level: Advanced | Best Practice: ✅
"""


class Student:
    """
    Represents a student with name and house.

    Demonstrates multiple OOP concepts across versions:
    - V1: Basic class with __init__ and __str__
    - V2: With @property decorators for validation
    - V3 (Best Practice): With @classmethod alternative constructor
    """

    # =========================================================================
    # V1: Basic Class — Just stores data
    # =========================================================================
    # def __init__(self, name, house):
    #     self.name = name      # Direct assignment — no validation
    #     self.house = house
    #
    # def __str__(self):
    #     return f"{self.name} from {self.house}"
    #
    # 💡 __init__ = constructor (initializes object when created)
    # 💡 __str__ = string representation (what print(object) shows)
    # 💡 self = the current object instance

    # =========================================================================
    # V2: With @property Decorators — Validation on assignment
    # =========================================================================
    # @property
    # def name(self):
    #     return self._name      # 💡 _name = "private" by convention
    #
    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError("Missing Name")
    #     self._name = name
    #
    # @property
    # def house(self):
    #     return self._house
    #
    # @house.setter
    # def house(self, house):
    #     if house not in ["Vrindavan", "Ayodhya", "Chitrakoot", "Mithila"]:
    #         raise ValueError("Invalid House")
    #     self._house = house
    #
    # 💡 @property = getter method (called when accessing student.name)
    # 💡 @name.setter = setter method (called when assigning student.name = "X")
    # 💡 _variable = convention for "internal/private" attribute
    # 💡 Raise ValueError to reject invalid data immediately

    # =========================================================================
    # BEST PRACTICE ✅: With @classmethod Factory Pattern
    # =========================================================================

    def __init__(self, name: str, house: str) -> None:
        """Initialize a Student with name and house.

        Args:
            name: Student's name
            house: Student's house/location
        """
        self.name = name
        self.house = house

    def __str__(self) -> str:
        """String representation of the student."""
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls) -> "Student":
        """Alternative constructor: Get student info from user input.

        💡 @classmethod = method that operates on the CLASS, not an instance
        💡 cls = the class itself (like self but for class-level)
        💡 cls(name, house) = Student(name, house) — creates new instance
        """
        name = input("Name: ").strip().title()
        house = input("House: ").strip().title()
        return cls(name, house)   # Creates and returns a new Student


def main() -> None:
    """Demonstrate OOP class usage."""
    student = Student.get()   # 💡 Calls class method (no instance needed)
    print(student)            # 💡 Calls __str__() automatically

    # 💡 Equivalent manual creation:
    # student = Student(name="Ram", house="Ayodhya")


if __name__ == "__main__":
    main()


# 💡 KEY TAKEAWAYS:
#   ✅ __init__ = constructor, __str__ = string representation
#   ✅ self = instance reference (like "this" in other languages)
#   ✅ @property = getter, @*.setter = setter (for validation/control)
#   ✅ @classmethod = alternative constructor (operates on class, not instance)
#   ✅ cls = class reference (like self but for class-level methods)
#   ✅ _variable = convention meaning "internal, don't touch directly"
#   ✅ Encapsulation = keeping data and methods that work on data together

