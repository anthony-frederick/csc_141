from random import choice

random_choice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

ticket = []
print("This will be the winning ticket:")

def lottery_roll():
    while len(ticket) < 4:
        chosen_character = choice(random_choice)

        if chosen_character not in ticket:
            print(f"Pulled a: {chosen_character}")
            ticket.append(chosen_character)
lottery_roll()

print("Winning ticket:", ticket)