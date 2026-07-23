# 📑 Quick Topic Index

> Use this index when you want to quickly find which file covers a specific concept.

---

## 🔤 Variables & Data Types

| Concept | File(s) | Key Lines |
|---------|---------|-----------|
| `str` (strings) | `hello.py`, `formate.py` | `input()`, `strip()`, `title()`, regex |
| `int` (integers) | `calculater.py` | `int(input())`, `+`, `pow()` |
| `float` | `calculater.py` | `float(input())`, `round()` |
| `bool` | `parity.py`, `compare.py` | `True`/`False`, comparison operators |
| `list` | `hogwarts.py`, `generate.py` | `[]`, `for`, `shuffle()` |
| `dict` | `hogwarts.py`, `students.py` | `{}`, key-value pairs |
| `set` | `introduction.txt` (notes) | Unordered unique values |

---

## 🔧 Functions

| Concept | File(s) | Key Lines |
|---------|---------|-----------|
| `def` keyword | `hello.py` | `def main():` |
| `return` | `hello.py`, `parity.py` | `return f"Hello, {to}"` |
| Default parameters | `hello.py` | `def hello(to="World"):` |
| `if __name__ == "__main__"` | `hello.py`, `calculater.py`, `saying.py` | Module guard |
| `pow()` | `calculater.py` | `pow(n, 2)` |

---

## 🔀 Conditionals

| Concept | File(s) | Key Lines |
|---------|---------|-----------|
| `if/elif/else` | `compare.py`, `grade.py` | Comparison chains |
| `and` / `or` | `compare.py`, `grade.py` | Logical operators |
| `match/case` | `house.py` | Switch statement |
| Chained comparison | `grade.py` | `90 <= score <= 100` |
| `%` modulo operator | `parity.py` | `n % 2 == 0` |

---

## 🔄 Loops

| Concept | File(s) | Key Lines |
|---------|---------|-----------|
| `while` loop | `cat.py`, `number.py` | Input validation pattern |
| `for` loop with `range()` | `cat.py`, `mario.py` | `for _ in range(n):` |
| List iteration | `hogwarts.py` | `for student in students:` |
| Dictionary iteration | `hogwarts.py` | `for key, value in dict.items():` |
| Nested loops | `mario.py` | Printing 2D patterns |
| String multiplication | `mario.py`, `cat.py` | `"#" * height` |

---

## ⚠️ Exceptions

| Concept | File(s) | Key Lines |
|---------|---------|-----------|
| `try/except` | `number.py` | Error handling |
| `ValueError` | `number.py` | Invalid int conversion |
| `pass` | `number.py` | Silent retry |
| `return` in `try` | `number.py` | Clean exit pattern |
| `raise` | `student.py` (commented) | `raise ValueError("...")` |

---

## 📚 Libraries & Modules

| Concept | File(s) | Key Lines |
|---------|---------|-----------|
| `import` | All files | Module import |
| `from ... import ...` | `generate.py` | Selective import |
| `random.choice()` | `generate.py`, `hat.py` | Random selection |
| `random.randint()` | `generate.py` | Random integer |
| `random.shuffle()` | `generate.py` | Shuffle list |
| `statistics.mean()` | `average.py` | Average calculation |
| `sys.argv` | `name.py`, `costumes.py` | Command-line args |
| `sys.exit()` | `name.py` | Exit with message |
| Creating modules | `saying.py` → `say.py` | Custom module pattern |
| `cowsay` | `say.py` | Fun text output |
| `requests` + API | `itunes.py` | HTTP requests |
| `json` | `itunes.py` | JSON parsing |
| `PIL` (Pillow) | `costumes.py` | Image processing |

---

## ✅ Unit Testing

| Concept | File(s) | Key Lines |
|---------|---------|-----------|
| `assert` | `tests/test_calculator.py` | Test assertions |
| `pytest` | `tests/test_calculator.py` | Test framework |
| `pytest.raises()` | `tests/test_calculator.py` | Exception testing |
| Test organization | `tests/__init__.py` | Package structure |
| Import for testing | `tests/test_hello.py` | `from hello import hello` |

---

## 📁 File I/O

| Concept | File(s) | Key Lines |
|---------|---------|-----------|
| `open()` | `names.py`, `students.py` | File operations |
| `with` statement | `names.py`, `students.py` | Auto-close pattern |
| `"w"` write mode | `names.py` | Overwrite file |
| `"a"` append mode | `names.py` | Add to file |
| `"r"` read mode | `names.py` | Default mode |
| `line.rstrip()` | `names.py` | Clean line endings |
| `sorted()` | `names.py` | Sort file contents |
| `csv.reader()` | `students.py` | Parse CSV |
| `csv.DictReader()` | `students.py` | CSV with headers |
| `csv.DictWriter()` | `students.py` | Write CSV with headers |

---

## 🧩 Regular Expressions

| Concept | File(s) | Key Lines |
|---------|---------|-----------|
| `re.search()` | `validate.py`, `formate.py`, `twitter.py` | Pattern matching |
| `re.IGNORECASE` | `validate.py`, `twitter.py` | Case-insensitive |
| `^` and `$` anchors | `validate.py` | Start/end matching |
| Groups `()` | `formate.py`, `twitter.py` | Extract parts |
| `(?:...)` non-capturing | `twitter.py` | Optional www. |
| Walrus `:=` | `formate.py`, `twitter.py` | Assign in expression |
| `\w+` word chars | `validate.py` | Alphanumeric match |
| `*` and `+` quantifiers | All regex files | Repetition patterns |

---

## 🏗️ OOP (Object-Oriented Programming)

| Concept | File(s) | Key Lines |
|---------|---------|-----------|
| `class` | `student.py`, `bank.py`, `hat.py` | Class definition |
| `__init__` | `student.py`, `bank.py` | Constructor |
| `self` | `student.py`, `bank.py` | Instance reference |
| `__str__` | `student.py` | String representation |
| `@property` | `bank.py`, `student.py` (commented) | Getter decorator |
| `@*.setter` | `student.py` (commented) | Setter decorator |
| `@classmethod` | `hat.py`, `student.py` | Class-level methods |
| Encapsulation | `bank.py` | `_balance` convention |
| `if __name__ == "__main__"` | `student.py`, `bank.py` | Script guard |

---

## 🎯 Et Cetera (Advanced)

| Concept | File(s) | Key Lines |
|---------|---------|-----------|
| `*args` / `**kwargs` | `introduction.txt` | Variable arguments |
| List comprehension | `introduction.txt` | `[x for x in list]` |
| `map()` / `filter()` | `introduction.txt` | Functional tools |
| `enumerate()` | `introduction.txt` | Indexed iteration |
| `yield` / generators | `introduction.txt` | Lazy evaluation |
| Type hints | `introduction.txt` | `def func(x: int) -> str:` |
| `argparse` | `introduction.txt` | Advanced CLI args |

---

## 📖 Full Notes

For comprehensive handwritten notes covering all topics, see:
- [`introduction.txt`](introduction.txt) — Original course notes

