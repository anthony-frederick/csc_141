import os
import random
os.system('cls')

superheros = {'   Iron man': 10, 
              '  Black Widow': 7, 
              'Captain America': 9, 
              '     Thor': 15, 
              '     Hulk': 30, 
              '  Spiderman': 9, 
              ' Black Panther': 10, 
              '   Wolverine': 12, 
              '  Professor X': 14, 
              '   Deadpool': 12}
heros_max_damage = {'   Iron man': 9, 
              '  Black Widow': 7, 
              'Captain America': 8, 
              '     Thor': 15, 
              '     Hulk': 100, 
              '  Spiderman': 8, 
              ' Black Panther': 10, 
              '   Wolverine': 12, 
              '  Professor X': 15, 
              '   Deadpool': 12}
superhero_number = len(superheros)
superheros_names = list(superheros.keys())
print(superheros_names)
superhero_strength = list(superheros.values())
print(superhero_strength)
player_strength = 5
player_max_damage = 8
hero_damage = list(heros_max_damage.values())

print("The heros that have entered the arena today are:\n")
for hero in superheros:
    print(f"{hero}\n")
random_number = random.randint(0, superhero_number - 1)
superhero = superheros_names[random_number]
hero_power = superhero_strength[random_number]

print("---------------------------------------------------")
print("      The hero you will be battling today is!      ")
print(f"                  {superhero}                     ")
print("           They have a power level of              ")
print(f"                        {hero_power}              ")
print("---------------------------------------------------")

action_choice = ' '
while True:
    if action_choice == 'e':
        print("You escaped knowing you couldn't defeat this foe...")
        break
    action_choice = input('Enter "e" to escape or "f" to fight: ')
    if action_choice == 'f':
        # Player attacks hero
        damage_to_hero = random.randint(0,  player_max_damage)
        if damage_to_hero  == 0:
            print("You whiffed your attack completely!")
        else:
            print(f"You have dealt {damage_to_hero} damage to {superhero.lstrip()}!")
        hero_power = hero_power - damage_to_hero
        if hero_power <= 0:
            print(f'You have defeated{superhero.lstrip()}!')
            print("Hope you had fun.")
            break
    # Hero attacks player
        damage_to_player = random.randint(0, random.choice(list(heros_max_damage.values())))
        if damage_to_player == 0:
            print("You barely dodged their attack!")
        else:
            print(f"{superhero.lstrip()} attacks dealing {damage_to_player} damage! ")
        player_strength = player_strength - damage_to_player
        if player_strength <= 0:
            print(f"{superhero.lstrip()} obliterated you...")
            print("Better luck next time.")
            break
    else:
        print('Invalid option please choose "e" or "f"' )
    
