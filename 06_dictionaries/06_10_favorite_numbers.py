# This prints people's favorite numbers

favorite_Numbers = {'anthony': [13, 19], 
                    'john': [7, 42, 54], 
                    'carl': [17, 90, 32], 
                    'lucas': [22, 33],  
                    'jack': [11, 81]}
for person, numbers in favorite_Numbers.items():
    print(f"{person.title()}'s favorite numbers are {numbers}")