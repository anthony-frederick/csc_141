# Shows two cities in Spain and a city in Sweden

def describe_city(city, country= 'Spain'):
    """Gives a city in a country"""
    print(f"{city} is in {country}")
describe_city('Madrid')
describe_city('Barcelona')
describe_city('Gothenburg', country= 'Sweden')