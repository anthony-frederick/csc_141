# Adds two inputed nubmers
# 2/10 because it wasn't very confusing


print("Type in two numbers and I'll add them together.")
print("Enter q to stop the program.")


first_number = input("\nFirst number: ")
second_number = input("\nSecond number: ")

try:
    answer = int(first_number) + int(second_number)  
except ValueError:
    print("\nYou have to input a number!")
else:
    print(f"\n {first_number} plus {second_number} is equal to {answer}!")