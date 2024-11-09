# Asks for your favorite number and if it already knows it tells you
# 6/10 very buggy and confusing

from pathlib import Path
import json

path = Path('favorite_number.json')
if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"\nI remember your favorite number its {favorite_number}!")

else:
    favorite_number = input('Please enter your favorite number: ')
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    print("I'll remember your favorite number!")