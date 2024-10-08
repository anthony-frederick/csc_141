# This poll asks people where they would want to go and prints it

responses = {}
polling_active = True
while polling_active:
    name = input("What is your name? ")
    place = input("If you could go one place in the world, where would it be? ")
    responses[name] = place
    repeat = input("Would you like to take the poll again? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\nPoll Results:")
for name, place in responses.items():
    print(f"{name.title()} would like to go to {place.title()}.")
