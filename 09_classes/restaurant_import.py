# Used to import to 09_10_imported_restaurant

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