"""
HARVARD CS50 PYTHON - Week 4: Libraries (random module)
=========================================================
Concepts: import, from X import Y, random.choice(), random.randint(), random.shuffle()

Author: David J. Malan (CS50)
Learning Level: Intermediate | Best Practice: ✅
"""

# =============================================================================
# V1: Random Choice — Pick random element from a list
# =============================================================================
from random import choice
coin = choice(["heads", "tails"])
print(f"Coin flip: {coin}")

# 💡 choice(list) returns ONE random element from the list

# =============================================================================
# V2: Random Integer — Get random number in range
# =============================================================================
from random import randint
number = randint(1, 10)
print(f"Random number (1-10): {number}")

# 💡 randint(a, b) returns random integer INCLUDING both a and b
# 💡 randint(1, 6) = dice roll

# =============================================================================
# V3: Shuffle — Randomly reorder a list IN PLACE
# =============================================================================
from random import shuffle

cards = ["sita", "ram", "hari", "vishnu"]
shuffle(cards)   # 💡 Modifies the original list! (in-place)

print("Shuffled list:")
for card in cards:
    print(f"  - {card}")

# 💡 shuffle() does NOT return a new list — it shuffles IN PLACE
# 💡 The original list order is permanently changed


# 💡 KEY TAKEAWAYS:
#   ✅ from random import choice — import only what you need
#   ✅ choice(list) = pick one random element
#   ✅ randint(a, b) = random integer between a and b (inclusive)
#   ✅ shuffle(list) = randomly reorder list (modifies original)
#   ✅ For dice: randint(1, 6)
#   ✅ For lottery: choice(range(1, 100))

