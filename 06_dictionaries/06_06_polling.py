# Here are some peoples favorite coding languages

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
pollers = ['mark', 'edward', 'brian', 'thomas', 'phil']
for name in pollers:
    if name in favorite_languages:
        print(f"Thank you {name.title()} for taking our poll!")
    else:
        print(f"{name.title()}, please take our poll")