# Gives some information about some poeple I know

class User:
    """Describes some people"""
    def __init__(self, first_name, last_name, age, gender, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.location = location

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is a {self.gender} who is {self.age} years old and is at {self.location}")
        
    def greet_user(self):
        print(f"\nThank you for signing in {self.first_name} {self.last_name}")

user = User('Anthony', 'Frederick', '18', 'male', 'Albright College')
user.greet_user()
user.describe_user()

user = User('Jack', 'Benedict', '18', 'male', 'Albright College')
user.greet_user()
user.describe_user()

user = User('Nathan', 'Huffman', '19', 'male', 'Albright College')
user.greet_user()
user.describe_user()
