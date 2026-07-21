import re

email = input("what's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com)$", email, re.IGNORECASE):
    print("valid")
else:
    ("Invalid")