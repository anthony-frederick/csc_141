# Adds a name to a seperate sheet
# 2/10 not to difficult to figure out

from pathlib import Path
path = Path('10_files_and_exceptions/guest.txt')
name = input('What is your name: ')
path.write_text(name) 