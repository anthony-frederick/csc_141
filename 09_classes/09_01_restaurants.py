# This prints some inforamation about a restaurant

class Restaurant:
    """Tells me some information about a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name} and serves {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")
    
restaurant = Restaurant('Dennys', 'food')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()