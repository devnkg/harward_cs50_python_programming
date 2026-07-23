# 🐍 Harvard CS50's Python Programming - Complete Learning Repository

> **Course:** CS50's Introduction to Programming with Python  
> **Instructor:** David J. Malan (Harvard University)  
> **Personal Learning Notes & Examples** — organized for quick recap & effective learning

---

## 📚 Course Overview (10 Weeks)

| Week | Topic | Key Concepts | Files |
|------|-------|--------------|-------|
| 0 | **Functions & Variables** | `def`, `input()`, `print()`, `int`, `float`, `str`, `round()`, comments | [`hello.py`](#functions--variables), [`calculater.py`](#functions--variables) |
| 1 | **Conditionals** | `if/elif/else`, `match/case`, `or/and`, comparison operators | [`compare.py`](#conditionals), [`grade.py`](#conditionals), [`parity.py`](#conditionals), [`house.py`](#conditionals) |
| 2 | **Loops** | `while`, `for`, `range()`, `list`, `dict`, `len()`, `sorted()` | [`cat.py`](#loops), [`mario.py`](#loops), [`hogwarts.py`](#loops) |
| 3 | **Exceptions** | `try/except`, `ValueError`, `else`, `pass`, `raise` | [`number.py`](#exceptions) |
| 4 | **Libraries** | `random`, `statistics`, `sys`, `requests`, `json`, APIs, packages | [`generate.py`](#libraries), [`average.py`](#libraries), [`name.py`](#libraries-command-line-arguments), [`say.py`](#libraries--packages), [`itunes.py`](#libraries--apis) |
| 5 | **Unit Tests** | `pytest`, `assert`, test functions, `__init__.py` | [`tests/test_calculator.py`](#unit-tests), [`tests/test_hello.py`](#unit-tests) |
| 6 | **File I/O** | `open()`, `with`, `CSV`, `reader()`, `DictReader()`, `DictWriter()` | [`names.py`](#file-io), [`students.py`](#file-io) |
| 7 | **Regular Expressions** | `re.search()`, `re.match()`, groups, `:=` walrus operator | [`validate.py`](#regular-expressions), [`formate.py`](#regular-expressions), [`twitter.py`](#regular-expressions) |
| 8 | **Object-Oriented Programming** | `class`, `__init__`, `@property`, `@classmethod`, `__str__`, encapsulation | [`student.py`](#oop), [`bank.py`](#oop), [`hat.py`](#oop) |
| 9 | **Et Cetera** | `*args`, `**kwargs`, list comprehension, `map`, `filter`, `enumerate`, generators, `yield`, type hints, `argparse` | In `introduction.txt` & Examples |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+ installed ([Download Python](https://www.python.org/downloads/))
- Basic terminal/command line knowledge

### Setup
```bash
# 1. Clone the repository
git clone <repo-url>
cd cs50-python-learning

# 2. (Recommended) Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run any example
python3 hello.py
```

---

## 📖 Topic-Wise Learning Guide

### Functions & Variables
> **Files:** [`hello.py`](hello.py), [`calculater.py`](calculater.py)

#### [hello.py](hello.py) — Input, Output & String Methods
```python
# --- V1: Basic Approach (Concatenation) ---
name = input("What is your name? ")
print("Hello, " + name)

# --- V2: Using commas & clean input ---
name = input("What is your name? ").strip().title()
print("Hello,", name)

# --- V3 (Best Practice ✓): f-strings & functions ---
def main():
    name = input("what's your name? ")
    print(hello(name))

def hello(to="World"):
    return f"Hello, {to}"

if __name__ == "__main__":
    main()
```

#### [calculater.py](calculater.py) — Integers, Floats & Custom Functions
| Version | Approach | Key Learning |
|---------|----------|--------------|
| V1 | Multiple `int()` calls | Type conversion basics |
| V2 | Nested `int(input())` | Compact code |
| V3 | `round()` function | Float precision |
| V4 (Best Practice ✓) | Define `square()` with `pow()` | Code reusability, `pow()` function |

```python
# --- V1: Basic integer addition ---
x = input("What's x? ")
y = input("What's y? ")
z = int(x) + int(y)
print(z)

# --- V2 (Better): Chained conversion ---
x = int(input("what's x? "))
y = int(input("what's y? "))
print(x + y)

# --- V3 (Best Practice ✓): With custom function ---
def main():
    x = int(input("what's x? "))
    print("x square is", square(x))

def square(n):
    return pow(n, 2)  # or n ** 2
```

**🧠 Key Takeaways:**
- `f"Hello, {name}"` is the **best practice** for string formatting
- Always use `if __name__ == "__main__": main()` for reusable modules
- `pow(n, 2)` or `n ** 2` for squaring

---

### Conditionals
> **Files:** [`compare.py`](compare.py), [`grade.py`](grade.py), [`parity.py`](parity.py), [`house.py`](house.py)

#### [compare.py](compare.py) — Comparison Operators
```python
# --- V1: Basic if/elif/else ---
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# --- V2: Using logical operators ---
if x < y or x > y:
    print("x is not equal to y")

# --- V3 (Best Practice ✓): Direct comparison ---
if x != y:
    print("x is not equal to y")
```

#### [grade.py](grade.py) — Nested Conditions
| Version | Approach | Key Learning |
|---------|----------|--------------|
| V1 | `score >= 90 and score <= 100` | Explicit range checking |
| V2 | `90 <= score <= 100` | Python chained comparison |
| V3 (Best Practice ✓) | `score >= 90` (no upper bound needed) | Logical simplification |

#### [parity.py](parity.py) — Boolean Functions
```python
def main():
    x = int(input("what's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0  # Best Practice ✓: Return boolean directly
```

#### [house.py](house.py) — Match/Case (Switch)
```python
name = input("what's your name? ")

# Best Practice ✓: match/case with | (or) pattern
match name:
    case "Radha" | "Krishna" | "Balram":
        print("Vrindavan")
    case "Ram" | "Sita":
        print("Ayodhya")
    case "Shiva" | "Parvati":
        print("Kailash")
    case _:  # Default case
        print("Unknown")
```

**🧠 Key Takeaways:**
- Use `if/elif/else` for ranges, `match/case` for specific values
- Always return boolean expressions directly: `return n % 2 == 0` (not `if...return True else return False`)
- `_` in match/case is the **wildcard/default** pattern

---

### Loops
> **Files:** [`cat.py`](cat.py), [`mario.py`](mario.py), [`hogwarts.py`](hogwarts.py)

#### [cat.py](cat.py) — While & For Loops
```python
# V1: While loop with counter
i = 0
while i < 3:
    print("meow")
    i += 1

# V2: For loop with range
for i in range(3):
    print("meow")

# V3 (Best Practice ✓): Function with validation
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):  # _ when variable unused
        print("meow")
```

#### [mario.py](mario.py) — Nested Loops & Print Patterns
```python
def print_column(height):
    print("#\n" * height, end="")  # String multiplication

def print_row(width):
    print("?" * width)

def print_square(size):
    for i in range(size):
        print("*" * size)  # Nested implicitly
```

#### [hogwarts.py](hogwarts.py) — Lists & Dictionaries
```python
# V1: Basic list iteration
students = ["sita", "ram", "hari", "vishnu"]
for student in students:
    print(student)

# V2: Indexed iteration
for i in range(len(students)):
    print(i + 1, students[i])

# V3: Dictionary iteration (Best Practice ✓)
gods = [
    {"name": "ram", "house": "ayodhya", "weapon": "bow"},
    {"name": "sita", "house": "mithila", "weapon": "lotus"},
]
for god in gods:
    print(god["name"], god["house"], god["weapon"], sep=", ")
```

**🧠 Key Takeaways:**
- Use `for _ in range(n)` when you don't need the loop variable
- `#\n` * height → string multiplication creates repeated patterns
- Dictionaries with lists of dicts → best for structured data

---

### Exceptions
> **File:** [`number.py`](number.py)

```python
# V1: No error handling
x = int(input("What's x? "))  # Crash if user enters "cat"

# V2: Basic try/except
try:
    x = int(input("What's x? "))
except ValueError:
    print("That's not a valid number!")

# V3: Loop until valid input
while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("Invalid!")

# V4 (Best Practice ✓): Function with exception handling
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))  # Clean & concise
        except ValueError:
            pass  # Just retry silently
```

**🧠 Key Takeaways:**
- Always handle `ValueError` when converting user input
- `return` inside `try` exits the function (and the loop) immediately
- `pass` lets you retry without printing error messages

---

### Libraries
> **Files:** [`generate.py`](generate.py), [`average.py`](average.py), [`name.py`](name.py), [`say.py`](say.py), [`saying.py`](saying.py), [`costumes.py`](costumes.py), [`itunes.py`](itunes.py)

#### Random Module ([generate.py](generate.py))
```python
from random import choice, randint, shuffle

# V1: Random choice from list
coin = choice(["heads", "tails"])
print(coin)

# V2: Random integer
number = randint(1, 10)

# V3: Shuffle list
cards = ["sita", "ram", "hari", "vishnu"]
shuffle(cards)
for card in cards:
    print(card)
```

#### Statistics ([average.py](average.py))
```python
import statistics
print(statistics.mean([100, 90]))  # Output: 95.0
```

#### Command-Line Arguments ([name.py](name.py))
```python
import sys

# V1: Basic (risky - crashes if no argument)
print("Hello,", sys.argv[1])

# V2: Error handling
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# V3 (Best Practice ✓): Iterate over all arguments
for arg in sys.argv[1:]:  # [1:] skips the script name
    print("Hello,", arg)
```

#### Creating & Importing Modules ([say.py](say.py), [saying.py](saying.py))
```python
# saying.py - reusable module
def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":  # Only runs when executed directly
    hello("world")

# say.py - imports from saying.py
from saying import hello, goodbye
hello(sys.argv[1])
goodbye(sys.argv[1])
```

#### APIs ([itunes.py](itunes.py))
```python
import requests
import sys
import json

response = requests.get(
    "https://music.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
)
object = response.json()
for result in object["results"]:
    print(result["trackName"])
```

#### Image Processing ([costumes.py](costumes.py))
```python
from PIL import Image

images = []
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costume.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
```

**🧠 Key Takeaways:**
- `sys.argv[0]` = script name, `sys.argv[1:]` = actual arguments
- `if __name__ == "__main__"` prevents code from running on import
- Use `requests` for APIs, `json` for parsing responses

---

### Unit Tests
> **Files:** [`tests/test_calculator.py`](tests/test_calculator.py), [`tests/test_hello.py`](tests/test_hello.py)

#### [tests/test_calculator.py](tests/test_calculator.py)
```python
import pytest
from calculater import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negetive():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")
```

#### [tests/test_hello.py](tests/test_hello.py)
```python
from hello import hello

def test_default():
    assert hello() == "Hello, World"

def test_argument():
    assert hello("Nkg") == "Hello, Nkg"
```

#### Run Tests
```bash
pytest tests/
```

**🧠 Key Takeaways:**
- Test files start with `test_` and are in a `tests/` folder
- Use `with pytest.raises(ErrorType)` to test for expected errors
- Test edge cases: positives, negatives, zeros, invalid types

---

### File I/O
> **Files:** [`names.py`](names.py), [`students.py`](students.py), [`names.txt`](names.txt), [`students.csv`](students.csv), [`names.csv`](names.csv)

#### Writing & Reading Text Files ([names.py](names.py))
```python
# V1: Write to file (overwrites)
name = input("what's your name? ")
with open("names.txt", "w") as file:
    file.write(f"{name}\n")

# V2 (Best Practice ✓): Append to file
name = input("what's your name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# Reading & sorting from file
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
```

#### CSV Files ([students.py](students.py))
```python
import csv

# Reading CSV - V1: Manual parsing
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

# Reading CSV - V2 (Best Practice ✓): Using DictReader
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']} is from {row['home']}")

# Writing CSV (Best Practice ✓): Using DictWriter
name = input("What's your name? ")
home = input("What's your home? ")
with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name})
```

**🧠 Key Takeaways:**
- `"a"` for append, `"w"` for overwrite, `"r"` (default) for read
- Always use `csv.DictReader`/`csv.DictWriter` for CSV files
- `line.rstrip()` removes trailing newline characters

---

### Regular Expressions
> **Files:** [`validate.py`](validate.py), [`formate.py`](formate.py), [`twitter.py`](twitter.py)

#### Email Validation ([validate.py](validate.py))
```python
import re

email = input("what's your email? ").strip()

# V1: Basic string check
if "@" in email and "." in email:
    print("valid")

# V2: Simple regex
if re.search(r".+@.+\.edu", email):
    print("valid")

# V3 (Best Practice ✓): Robust regex with re.IGNORECASE
if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com)$", email, re.IGNORECASE):
    print("valid")
else:
    print("Invalid")
```

#### Name Formatting ([formate.py](formate.py))
```python
import re

name = input("what's your username? ").strip()

# V1: Manual split
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"

# V2 (Best Practice ✓): Regex with walrus operator
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
```

#### URL Parsing ([twitter.py](twitter.py))
```python
import re

url = input("URL: ").strip()

# Best Practice ✓: Extract username from Twitter URL
if matches := re.search(
    r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE
):
    print(f"Username:", matches.group(1))
else:
    print("Invalid")
```

**🧠 Key Takeaways:**
- `:=` (walrus operator) assigns and evaluates in one step
- `re.IGNORECASE` flag makes pattern case-insensitive
- `^` and `$` anchor the pattern to start/end of string

---

### Object-Oriented Programming
> **Files:** [`student.py`](student.py), [`bank.py`](bank.py), [`hat.py`](hat.py)

#### Classes & Objects ([student.py](student.py))
```python
class Student:
    # V1: Basic class
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # V2 (Best Practice ✓): With @classmethod
    @classmethod
    def get(cls):
        name = input("name: ")
        house = input("house: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)
```

#### Properties & Encapsulation ([bank.py](bank.py))
```python
class Account:
    def __init__(self):
        self._balance = 0  # _ prefix = "protected" by convention

    @property  # Getter - read-only access
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n
```

#### Class Methods ([hat.py](hat.py))
```python
import random

class Hat:
    houses = ["Ayodhya", "Vrindavan", "Mithila", "Barsana"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Ram")
```

**🧠 Key Takeaways:**
- `__init__` is the constructor, `self` refers to the current instance
- `@property` creates getter methods for controlled access
- `@classmethod` operates on the class itself (no instance needed)
- `_variable` naming convention indicates internal/protected attributes

---

## 🗂 Repository Structure

```
cs50-python-learning/
├── hello.py            # Week 0: Functions & Variables
├── calculater.py       # Week 0: Integers, Floats, Functions
├── compare.py          # Week 1: Conditionals (if/elif/else)
├── grade.py            # Week 1: Nested Conditions
├── parity.py           # Week 1: Boolean Functions
├── house.py            # Week 1: Match/Case
├── cat.py              # Week 2: Loops (while, for)
├── mario.py            # Week 2: Nested Loops
├── hogwarts.py         # Week 2: Lists & Dictionaries
├── number.py           # Week 3: Exceptions
├── generate.py         # Week 4: Random Library
├── average.py          # Week 4: Statistics Library
├── name.py             # Week 4: Command-Line Arguments
├── say.py              # Week 4: Importing Modules
├── saying.py           # Week 4: Creating Modules
├── itunes.py           # Week 4: APIs & Requests
├── costumes.py         # Week 4: Pillow (Image Processing)
├── tests/              # Week 5: Unit Tests
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_hello.py
├── names.txt           # Week 6: Text File I/O
├── names.csv           # Week 6: CSV File I/O
├── names.py            # Week 6: File Reading/Writing
├── students.csv        # Week 6: CSV Data
├── students.py         # Week 6: CSV Handling
├── validate.py         # Week 7: Regex - Email
├── formate.py          # Week 7: Regex - Name Formatting
├── twitter.py          # Week 7: Regex - URL Parsing
├── student.py          # Week 8: OOP - Classes
├── bank.py             # Week 8: OOP - Properties
├── hat.py              # Week 8: OOP - Class Methods
├── introduction.txt    # Original handwritten notes
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## 🎯 How to Use This Repo

### For Beginners (Learning Python)
1. **Start chronologically** by week (0 → 9)
2. **Read the code comments** - each file shows V1 → V2 → Best Practice
3. **Run each file** and experiment by modifying values
4. **Refer to `introduction.txt`** for quick topic summaries

### For Quick Recap (Your Future Self)
1. **Check this README** topic index for the concept you need
2. **Open the relevant file** - look for "Best Practice ✓" commented section
3. **Run the test suite** with `pytest tests/` to verify your environment works

---

## 📦 Dependencies

```
pytest>=7.0.0
Pillow>=9.0.0
requests>=2.28.0
cowsay>=5.0
```

Install: `pip install -r requirements.txt`

---

## 🐛 Known Fixes Applied

| File | Issue | Fix |
|------|-------|-----|
| `costumes.py` | `image[0]` → should be `images[0]` (list variable name) | Fixed variable name |
| `validate.py` | `("Invalid")` → should be `print("Invalid")` | Added missing `print()` |

---

## 📝 License

This repository contains personal learning notes from Harvard's CS50 course.  
All code is shared for educational purposes.

