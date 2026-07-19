from random import choice
from random import randint
from random import shuffle

coin = choice(["haids", "tails"])
print(coin)

number = randint(1, 10)
print(number)

cards = ["sita", "ram", "hari", "vishnu"]
shuffle(cards)
for card in cards:
    print(card)