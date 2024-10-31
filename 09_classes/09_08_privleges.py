# Gives some infornmation about a few people and greets them

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


class Admin(User):
    def __init__(self, first_name, last_name, age, gender, location):
        super().__init__(first_name, last_name, age, gender, location)
        self.privileges = Privileges()
    
            
class Privileges():
    def __init__(self, privileges= []):
        self.privileges = privileges
    def show_privileges(self):
        print("\nPrivileges")
        for privilege in self.privileges:
            print(f"{privilege}")

dave = Admin('Dave', 'Jones', '34', 'male', 'Pennsylvania')
dave.greet_user()
dave.describe_user()

print(f"\nThe admin...")
dave_privileges = ['can delete posts', 
                   'can add posts', 
                   'can ban users']
dave.privileges.privileges = dave_privileges
dave.privileges.show_privileges()