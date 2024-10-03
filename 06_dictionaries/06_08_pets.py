# This shows some pets with some information about them

pets = []
pet = {'animal': 'guinea pig', 'owner': 'tom', 'food': 'lettuce', 'name': 'picky'}
pets.append(pet)
pet = {'animal': 'fish', 'owner': 'nate', 'food': 'fish food', 'name': 'gup'}
pets.append(pet)
pet = {'animal': 'dog', 'owner': 'frank', 'food': 'meat', 'name': 'sparky'}
pets.append(pet)

for pet in pets:
    print(f"This is what I know about each pet, {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")