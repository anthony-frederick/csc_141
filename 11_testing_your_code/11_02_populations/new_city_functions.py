# Gives a country, a city in it, and it's population
# 10/10 it is all very confusing to figure out

def city_country(city, country, population=0):
    """Return a string representing a city-country pair."""

    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f" - population {population}"
    return output_string