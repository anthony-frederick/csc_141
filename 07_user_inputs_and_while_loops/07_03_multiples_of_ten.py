# This tells you if the number you chose is a multiple of 10

number = ("Pick any number: ")
number = int(number)
if number % 10 == 0:
    print("This number is a multiple of ten.")
else:
    print("This number is not a multiple of ten.")