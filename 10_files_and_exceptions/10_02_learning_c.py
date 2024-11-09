# Replaces instences of the word python with the letter C in another file
# 3/10 because it has a little more tricky

from pathlib import Path

path = Path('10_files_and_exceptions/learning_python.txt')
contents = path.read_text()
for line in contents.splitlines():
    line = line.replace('python', 'C')
    print(line)