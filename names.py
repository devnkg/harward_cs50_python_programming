"""
HARVARD CS50 PYTHON - Week 6: File I/O
========================================
Concepts: open(), with statement, file modes (w, a, r), read/write, sorted()

Author: David J. Malan (CS50)
Learning Level: Intermediate | Best Practice: ✅
"""

# =============================================================================
# V1: Write to File (Overwrite) — "w" mode ERASES existing content
# =============================================================================
# name = input("What's your name? ")
# file = open("names.txt", "w")
# file.write(f"{name}\n")
# file.close()
# 💡 "w" = write mode — CREATES file or OVERWRITES existing file
# 💡 Must call file.close() — easy to forget!

# =============================================================================
# V2: Write to File (Append) — "a" mode ADDS to existing content
# =============================================================================
# name = input("What's your name? ")
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()
# 💡 "a" = append mode — ADDS to end of file, doesn't erase

# =============================================================================
# V3: Using with Statement — Auto-closes file (BEST PRACTICE)
# =============================================================================
# name = input("What's your name? ")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")
# 💡 with statement AUTO-CLOSES the file — even if error occurs!
# 💡 No need for file.close()

# =============================================================================
# V4: Read from File and Sort — Read all lines into list
# =============================================================================
names = []

with open("names.txt") as file:     # 💡 Default mode = "r" (read)
    for line in file:                # 💡 Iterate over lines directly
        names.append(line.rstrip())  # 💡 rstrip() removes \n at end

# 💡 sorted() returns a NEW sorted list (original list unchanged)
for name in sorted(names):
    print(f"Hello, {name}")

# 💡 Alternative: names.sort() sorts IN PLACE (modifies original list)


# 💡 KEY TAKEAWAYS:
#   ✅ Always use with open() — auto-closes the file
#   ✅ "w" = write (overwrites), "a" = append (adds to end), "r" = read (default)
#   ✅ \n = newline character — without it, everything is on one line
#   ✅ line.rstrip() removes trailing whitespace/newlines
#   ✅ sorted(list) = returns new sorted list, list.sort() = sorts in place
#   ✅ for line in file: reads file line-by-line (memory efficient)

