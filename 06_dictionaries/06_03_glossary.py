# This program describes some different functions we used this year

glossary = {'variable': 'Stores information.', 
    'list': 'list of different things like strings or integers.',
    'if_statement': 'conditional for a certain thinsg to happen.',
    'error': 'thing that goes wrong and needs to be fixed.',
    'tuple': "list of items that can't be changed.",
    'else': 'function to be used with "if" as the other condition',
    'string': "word that can't really be used as a number",
    'integer': "number that can be used in equations",
    'float': "number that has any sort of decimal place even .0",
    'sort': "function that lets you sort lists alphabetically",
    'del': "function that lets you delete things out of lists or dictionaries"}
for term, description in glossary.items():
    print(f"{term.title()} is a {description}")