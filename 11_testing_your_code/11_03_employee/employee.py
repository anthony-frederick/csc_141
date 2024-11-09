# Gives a bunch of information about an employee
# 10/10 Doesn't make much sense and all the troublshooting doesn't work

class Employee:

    def __init__(self, f_name, l_name, salary):
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount
