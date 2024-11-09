# Prints the previously given favorite number from 10_ll_favorit_number
# 2/10 not too complicated

from pathlib import Path
import json

path = Path('number.json')
contents = path.read_text()
number = json.loads(contents)
print(f"I remember your favorite number its {number}!")