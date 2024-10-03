# This shows where some people live and what their ages are

people = []
person = {'first_name': 'anthony', 'last_name': 'frederick', 'age': 18, 'city': 'King of Prussia'}
people.append(person)
person = {'first_name': 'carl', 'last_name': 'rudigaer', 'age': 17, 'city': 'King of Prussia'}
people.append(person)
person = {'first_name': 'jack', 'last_name': 'benedict', 'age': 18, 'city': 'N/A'}
people.append(person)

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
    print(f"{name} lives in {city} and is {age} years old")