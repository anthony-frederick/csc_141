current_users = ['gamer', 'civilian', 'admin', 'dweller', 'player']
new_users = ['master', 'gamer', 'king', 'serpent', 'player']
for user in new_users:
    if user in current_users:
        print(f'{user} is already taken, please choose a new one.')
    else:
        print(f'{user} is available, welcome.')