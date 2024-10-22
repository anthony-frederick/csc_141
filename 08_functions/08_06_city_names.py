# Gives cities and which countries thy are located in

def city_country(city, country):
    """Return a string of a city and a country"""
    return f"{city.title()}, {country.title()}"
city = city_country('santiago', 'chile')
print(city)
city = city_country("tokyo", 'japan')
print(city)
city = city_country('buenos aires', 'argentina')
print(city)