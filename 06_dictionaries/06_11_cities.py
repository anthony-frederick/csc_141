# Here are some cities with some information about them

cities = {'madrid': {'country':'spain', 
                     'population': 3223000, 
                     'fact': 'It is the highest capital in Europe elevation-wise'},
         'boston': {'country':'united states', 
                     'population': 680000, 
                     'fact': 'The first dunkin donuts was located near Boston'},
         'paris': {'country':'france', 
                     'population': 2161000, 
                     'fact': 'The first public movie screening was in Paring in 1895'}}
for city, information in cities.items():
    print(f"\nCity: {city}")
    country = information['country']
    population = information['population']
    fact = information['fact']
    print(f"\t Country: {country}.")
    print(f"\tPopulation: {population}.")
    print(f"\tFact: {fact}.")