# Comments in city_functions

from city_functions import city_country

def test_city_country():
    description = city_country('santiago', 'chile')
    print(f'Location formated: {description}.')
