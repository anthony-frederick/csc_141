
from privileges_import import User
from privileges_import import Admin
from privileges_import import Privileges

anthony = Admin('Anthony', 'Frederick', '18', 'male', 'Alrbight College')
anthony.greet_user()
anthony.describe_user()
anthony.privileges.show_privileges()