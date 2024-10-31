# Shows some information about users and their login attempts

class User:
    """Describes some people"""
    def __init__(self, first_name, last_name, age, gender, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is a {self.gender} who is {self.age} years old and is at {self.location}")
        
    def greet_user(self):
        print(f"\nThank you for signing in {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
         self.login_attempts = 0
           

user = User('Anthony', 'Frederick', '18', 'male', 'Albright College')
user.greet_user()
user.describe_user()
print("Attempting to login:")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Number of attempts = {user.login_attempts})")
print("Resetting login attempt count...")
user.reset_login_attempts()
print(f"Number of attempts = {user.login_attempts}")
