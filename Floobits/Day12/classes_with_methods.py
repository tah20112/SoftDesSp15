"""Working with Python classes"""

## Social network first steps
import copy

def function_name():
    """My docstring"""
    pass

class Person:
    """Information about a person"""
    def __init__(self, first_name, last_name, job):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.friends = []

    def __str__(self):
        """Print out details about given person"""
        template = "{first} {last} is a {job}"
        return template.format(first=self.first_name, last=self.last_name, job=self.job)

    def add_friend(self, friend):
        self.friends.append(friend)

paul = Person("Paul", "Ruvolo", "Professor")

# Create a person "ben" and set his attributes
ben = Person("Ben", "Hill", "Professor")
print ben

ben.add_friend(paul)

#ben.print_person()

# # Create new person blinder as a copy of Ben
# # and modify attributes as necessary
# blinder = copy.copy(ben)
# blinder.last_name = "Linder"

# # Print out the bens' info
# print_person(blinder)
# print "Blinder friend", print_person(blinder.friend)
# print_person(ben)






# Aside: string formatting
# https://docs.python.org/2/library/string.html#format-examples