# Gives information about how many people Dennys has served

class Restaurant:
    """Tells me some information about a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Prints restaurant name and what they serve"""
        print(f"\nThe restaurant is called {self.restaurant_name} and serves {self.cuisine_type}")
    
    def open_restaurant(self):
        """Prints the restaurant being open"""
        print(f"\n{self.restaurant_name} is now open")

    def set_number_served(self, number_served):
        """Tells how many people the restaurant has served"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Adds more people to the amount of people served at the restaurant"""
        self.number_served += additional_served

    
restaurant = Restaurant('Dennys', 'food')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"\nThey have served {restaurant.number_served} people")
restaurant.set_number_served(228)
print(f"\nThey have now served {restaurant.number_served} people")
restaurant.increment_number_served(923)
print(f"\nThey have now served {restaurant.number_served} people")

class icecreamstand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type= 'icecream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavor(self):
        print("\nThe following flavors are being sold:")
        for flavor in self.flavors:
            print(f"{flavor.title()}")

daves = icecreamstand("Dave's Icecream")
daves.flavors = ['vanilla', 'chocolate', 'peanut butter']

daves.describe_restaurant()
daves.display_flavor()

