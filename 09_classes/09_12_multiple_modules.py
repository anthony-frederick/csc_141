# Shows privileges for an admin

from privileges_admin_import import *
from privileges_user_import import User

anthony = Admin('Anthony', 'Frederick', '18', 'male', 'Albright College')
anthony.privileges.show_privileges()
