# Reads a book and tells you how many instances of a word appear
# 7/10 hard to troubleshoot with no coherent error message

from pathlib import Path

book = Path("10_files_and_exceptions/books.txt")

book = book.read_text()
book.splitlines()
try:
    print('\nApproximation of the word the:')
    print(book.count('the'))
    print('\nNumber of the word the:')
    print(book.count('the '))
except FileNotFoundError:
    pass