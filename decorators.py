""" Decorators
-> Design pattern that allows us to modify the functionality
of a function without necessarilly modofying the function
code itself
-> It the special @ symbol on functions
"""

# how to create decorators
def logger(func):
    # define another inner function
    def inner():
        print("Decorator is running before function")
        # execute the original function
        func()

    return inner

# @logger
def check_mic():
    print("Is the mic working?")

# check_mic()

decorated_func = logger(check_mic)

# call execute the inner function
decorated_func()


def modifier(func):
    def inner(a, b):
        # modify argument a
        a = a + 5
        # call the original function
        return func(a, b)

    return inner

def validator(func):
    def inner(a, b):
        # check the args are of type int
        if isinstance(a, int) and isinstance(b, int):
            return func(a, b)
        else:
            return "Args must of type int"
    return inner

@validator
@modifier
def calculate(a, b):
    return a + b

# this is how the decorators are applied in the background
# decorated = validator(modifier(calculate))

@validator
def multiply(x, y):
    return x * y

print(calculate(3, "3"))

# print(calculate("Wed", "Thur"))

# print(multiply(2, 2))

# print(multiply("X", 4))
