# Asks for your favorite number to be remembered
# 2/10 not too complicated

from pathlib import Path
import json

number = input('Please enter your favorite number: ')
path = Path('number.json')
contents = json.dumps(number)
path.write_text(contents)

print("I'll remember your favorite number!")