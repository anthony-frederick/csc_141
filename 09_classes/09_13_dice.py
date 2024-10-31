# Rolls some different types of dice being rolled 10 times

from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides=sides

    def roll_die(self):
        return randint(1, self.sides)

d6 = Die()
results = []
for number in range(10):
    result = d6.roll_die()
    results.append(result)
print("6-sided dice rolls:")
print(results)

d10 = Die(sides=10)
results = []
for number in range(10):
    result = d10.roll_die()
    results.append(result)
print("10-sided dice rolls:")
print(results)

d20 = Die(sides=20)
results = []
for number in range(10):
    result = d20.roll_die()
    results.append(result)
print("20-sided dice rolls:")
print(results)