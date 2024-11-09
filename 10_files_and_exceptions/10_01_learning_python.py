# Calls some infomration from another file
# 2/10 because i just learned how to do it and it wasn't complicated

from pathlib import Path

path = Path('10_files_and_exceptions/learning_python.txt')
contents = path.read_text()
print(contents)
print('\n')
for line in contents.splitlines():
    print(line)