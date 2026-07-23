"""
HARVARD CS50 PYTHON - Week 4: Statistics Library
==================================================
Concepts: import, statistics module, mean() function, list operations

Author: David J. Malan (CS50)
Learning Level: Intermediate | Best Practice: ✅
"""

import statistics

# =============================================================================
# V1: Direct call with literal list
# =============================================================================
print(f"Mean of [100, 90]: {statistics.mean([100, 90])}")

# =============================================================================
# V2 (Best Practice): Using variables for clarity
# =============================================================================
scores = [100, 90, 85, 95, 88]
average = statistics.mean(scores)
print(f"Scores: {scores}")
print(f"Average: {average:.2f}")  # 💡 :.2f formats to 2 decimal places

# 💡 Other useful statistics functions:
#   statistics.median(scores)    — Middle value
#   statistics.mode(scores)      — Most frequent value
#   statistics.stdev(scores)     — Standard deviation
#   statistics.variance(scores)  — Variance


# 💡 KEY TAKEAWAYS:
#   ✅ import statistics = import the whole module
#   ✅ statistics.mean(list) = average of values
#   ✅ :.2f in f-string = format to 2 decimal places
#   ✅ Other stats functions: median, mode, stdev, variance

