"""Working with Python classes"""

## Social network first steps
import copy

def function_name():
    """My docstring"""
    pass

class Person(object):
    """Information about a person"""
    pass

def print_person(x):
    """Print out details about given person"""
    template = "{first} {last} is a {job}"
    print template.format(first=x.first_name, last=x.last_name, job=x.job)

paul = Person()
paul.first_name = "Paul"
paul.last_name = "Ruvolo"
paul.job = "Professor"

# Create a person "ben" and set his attributes
ben = Person()
print ben
ben.first_name = "Ben"
ben.last_name = "Hill"
ben.job = "Professor"
ben.friend = paul

print_person(ben)

# Create new person blinder as a copy of Ben
# and modify attributes as necessary
blinder = copy.copy(ben)
blinder.last_name = "Linder"

# Print out the bens' info
print_person(blinder)
print "Blinder friend", print_person(blinder.friend)
print_person(ben)






# Aside: string formatting
# https://docs.python.org/2/library/string.html#format-examples