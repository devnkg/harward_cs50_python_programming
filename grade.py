"""
HARVARD CS50 PYTHON - Week 1: Conditionals (Advanced)
======================================================
Concepts: Chained comparisons, and/or operators, if/elif/else optimization

Author: David J. Malan (CS50)
Learning Level: Beginner → Intermediate | Best Practice: ✅
"""

score = int(input("Score: "))

# =============================================================================
# V1: Explicit Range Checking — Using AND operator
# =============================================================================
# if score >= 90 and score <= 100:
#     print("Grade: A")
# elif score >= 80 and score <= 89:
#     print("Grade: B")
# elif score >= 70 and score <= 79:
#     print("Grade: C")
# elif score >= 60 and score <= 69:
#     print("Grade: D")
# else:
#     print("Grade: F")
# 💡 Explicit upper AND lower bounds — very clear but verbose

# =============================================================================
# V2: Python Chained Comparison — More Pythonic
# =============================================================================
# if 90 <= score <= 100:
#     print("Grade: A")
# elif 80 <= score <= 89:
#     print("Grade: B")
# elif 70 <= score <= 79:
#     print("Grade: C")
# elif 60 <= score <= 69:
#     print("Grade: D")
# else:
#     print("Grade: F")
# 💡 Python allows chained comparisons: 90 <= score <= 100
# 💡 Reads like math: "90 is less than or equal to score is less than or equal to 100"

# =============================================================================
# BEST PRACTICE ✅: Eliminate Upper Bounds (since elif stops at first match)
# =============================================================================
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# 💡 LOGIC:
#   - If score >= 90, it prints A and SKIPS all remaining elifs
#   - If score >= 80 (but < 90), it prints B
#   - So we don't need to check upper bounds!
# 💡 This is the CLEANEST and most MAINTAINABLE approach

# 🔬 Edge Cases:
#   Input: 95   → Grade: A
#   Input: 82   → Grade: B
#   Input: 70   → Grade: C
#   Input: 100  → Grade: A
#   Input: -5   → Grade: F (unexpected — consider validation!)


# 💡 KEY TAKEAWAYS:
#   ✅ elif chains STOP at the first True condition
#   ✅ You can simplify by dropping redundant upper bounds
#   ✅ Python supports chained comparisons: 90 <= score <= 100
#   ✅ Always consider edge cases (negative numbers, >100)
#   ✅ For validation, add: if score < 0 or score > 100: print("Invalid")

