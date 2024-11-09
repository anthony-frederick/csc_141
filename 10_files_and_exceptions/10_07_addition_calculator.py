# Asks for two numbers and adds them
# 3/10 It is kinda like the last one but slightly longer

print("Type in two numbers and I'll add them together.")
print("Enter q to stop the program.")

while True:
    try:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        second_number = input("\nSecond number: ")
        if second_number == 'q':
            break
        answer = int(first_number) + int(second_number)
        print(f"\n {first_number} plus {second_number} is equal to {answer}!")
    except ValueError:
        print("Input an actual number please.")