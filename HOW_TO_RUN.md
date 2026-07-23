# 🚀 How to Run This Repository

## Quick Start

```bash
# 1. Clone the repo
git clone <repo-url>
cd python_learning_cs50

# 2. Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run any Python file
python3 hello.py
python3 calculater.py
```

---

## 🧪 Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_hello.py

# Run with verbose output
pytest -v tests/

# See test coverage (if pytest-cov installed)
pytest --cov=. tests/
```

---

## 📂 Running Individual Examples

### Week 0 — Functions & Variables
```bash
python3 hello.py        # Input/output, functions
python3 calculater.py   # Integers, floats, square()
```

### Week 1 — Conditionals
```bash
python3 compare.py      # Comparison operators
python3 grade.py        # Grade calculation
python3 parity.py       # Even/odd detection
python3 house.py        # Match/case statements
```

### Week 2 — Loops
```bash
python3 cat.py          # While/for loops
python3 mario.py        # Nested loops, patterns
python3 hogwarts.py     # Lists & dictionaries
```

### Week 3 — Exceptions
```bash
python3 number.py       # Try/except error handling
```

### Week 4 — Libraries
```bash
python3 generate.py     # Random module
python3 average.py      # Statistics module
python3 name.py Ram     # CLI arguments
python3 say.py Ram      # Custom modules + cowsay
python3 itunes.py "A R Rahman"  # API requests
python3 costumes.py img1.jpg img2.jpg  # Pillow images
```

### Week 5 — Unit Tests
```bash
pytest tests/
```

### Week 6 — File I/O
```bash
python3 names.py        # Text file read/write
python3 students.py     # CSV file handling
```

### Week 7 — Regular Expressions
```bash
python3 validate.py     # Email validation
python3 formate.py      # Name formatting
python3 twitter.py      # URL parsing
```

### Week 8 — OOP
```bash
python3 student.py      # Classes & objects
python3 bank.py         # Properties & encapsulation
python3 hat.py          # Class methods
```

---

## 💡 Tips

1. **Read the code comments** — Each file shows multiple versions (V1 → Best Practice)
2. **Experiment** — Change values, add your own inputs, break things intentionally
3. **Use Python's interactive mode** — `python3` then `from hello import hello` then `hello("Test")`
4. **Check the README** for detailed explanations of each concept
5. **Use TOPIC_INDEX.md** to quickly find which file covers a specific concept

