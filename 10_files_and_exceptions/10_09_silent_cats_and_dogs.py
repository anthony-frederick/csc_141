# Gives the names of some dogs and cats
# 1/10 I changed two lines of code so it wasn't too hard


from pathlib import Path

cats = Path('10_files_and_exceptions/cats.txt')
dogs = Path('10_files_and_exceptions/dogs.txt')

try:
    print("\nCat names:")
    cats = cats.read_text()
    print(cats) 
except FileNotFoundError:
    pass

try:
    print("\n Dog names:")
    dogs = dogs.read_text()
    print(dogs)
except FileNotFoundError:
    pass
