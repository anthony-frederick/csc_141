# This program also runs some conditional tests

drink = 'water'
print(drink == 'water')
print(drink == 'mouse')
print("\n")
planet = 'Earth'
print(planet.lower() == 'earth')
print(planet.lower() == 'Earth')
print("\n")
number = 15
print(number < 20)
print(number > 20)
print(number <= 15)
print(number >= 16)
print("\n")
limit = 30
print(limit > 23 or limit < 21)
print(limit > 10 and limit <= 29)
print("\n")
places = ['america', 'africa', 'asia']
print('africa' in places)
print('toilet' in places)
print('glass' not in places)
print('asia' not in places)