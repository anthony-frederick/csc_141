# This prints people's favorite places

favorite_places = {'anthony': ['united states', 'finland', 'canada'], 
                   'mark': ['germany, egypt', 'iran'], 
                   'fred': ['china', 'japan', 'united states']}
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are {places}")