# Here are some users least favorite coding languages

least_favorite_languages = {
'jen': ['python', 'rust'],
'sarah': ['c'],
'edward': ['rust', 'go'],
'phil': ['python', 'haskell'],
'dave': ['c'],
'bella': ['java']
}
for name, languages in least_favorite_languages.items():
    print(f"\n{name.title()}'s least favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")