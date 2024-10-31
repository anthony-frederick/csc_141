# Used to import into 09_11_imported_admin

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
        print("\n Admin Privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"{privilege}")
        else:
            print("This user has no privileges.")