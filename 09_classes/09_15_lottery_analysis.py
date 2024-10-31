# Checks to see how many rolls it would take me to win the lottery

from random import choice

random_choice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

print("This will be the winning ticket:")

def lottery_roll():
    ticket = []
    while len(ticket) < 4:
        chosen_character = choice(random_choice)

        if chosen_character not in ticket:
            print(f"Pulled a: {chosen_character}")
            ticket.append(chosen_character)
    return ticket
        
def check_my_ticket(played_ticket, winning_ticket):
    for thing in played_ticket:
        if thing not in winning_ticket:
            return False
    return True

def my_pulls():
    my_ticket = []
    while len(my_ticket) < 4:
        my_chosen_character = choice(random_choice)
        if my_chosen_character not in my_ticket:
            my_ticket.append(my_chosen_character)
    return my_ticket

ticket = lottery_roll()
print("This will be the winning ticket:", ticket)

plays = 0
won = False

while not won:
    my_ticket = my_pulls()
    won = check_my_ticket(my_ticket, ticket)
    plays += 1
    
if won:
    print("There has been a winner!")
    print(f"My ticket: {my_ticket}")
    print(f"Winning ticket: {ticket}")
    print(f"It took {plays} tries to win!")