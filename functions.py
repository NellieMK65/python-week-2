""" Functions
1. Blocks of reusable code
Reusablity
Modularity -> breaking down complex programs into smaller managable parts
"""

# function defination
def hello(name):
    print(f"Hello {name}, we are learning about functions")

# calling the function
hello("Jane")

# 1. Positional arguments
def greeting(first_name, age, last_name = 'Doe'):
    print(f"Good morning {first_name} {last_name}, your age is {age}")

# calling the function
# the order in which we pass arguments matters
greeting(18, "Jane")

greeting("Jane", 18)

# Keyword arguments where arguments are identified by the parameter name which
# bascially makes the order irrelevant
greeting(first_name="Vincent", age=23)

# We can start with positional args and then end with keyword args
greeting("Daud", 25, last_name="Elmoge")

# kwargs
greeting(last_name="Haji", first_name="Robert", age=24)

# positional args -> means param name is not provided, we use the order to assign the
# values to our parameters in the function
greeting("Godwin", 25, "Thuranira")

# When starting with positional args we have to stick to using them for the remaining args too
greeting(first_name="Irene", age=20)

# an unknown number of positional args
# the unknown values will automatically be passed to a tuple
def sum_all(*args):
    # sum is an inbuilt function -> a bit similar to the reduce method in js
    print(sum(args))

sum_all(1, 2, 3, 7, 10)

# unknown number of kwargs
# for keyword arguments, the values are stored inside a dict
def display_profile(**kwargs):
    print(kwargs)

display_profile(name="Jane", age=20)

# list and Sets
# 1. They are both mutable
# the values must be immutable

# declaring a variable
day = "Monday"

# we are reassigning a new value
day = "Tuesday"

# this gives an error
# day[1] = "w"
{}

days = ["Mon", 'Tue', "wed"]

# it`s mutating the original value and updating from Tue to Fri
days[1] = "Fri"


unique_values = {1, 2, 3, 3, "t", "t"}

unique_values.add(4)

print(unique_values)

# Decorators -> reusablity
