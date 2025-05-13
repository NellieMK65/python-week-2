# Object Oriented Programming -> OOP

""" Four main principles of OOP
1. Inherintance
2. Abstraction
3. Encapsulation
4. Polymorphism

-> Involves the use of classes and objects
-> It has methods and properties (attributes)
"""

# class -> blueprint of how objects are created and how they behave

# This was an example of a student entity
# Attributes -> name, class, grade, gender, reg no
# Behaviors -> read, playing a game, partying, rebellious

# Food entity
# Attributes -> ingredients, hot/cold, origin, calories, prep time
# Behaviors ->

# Scenario -> A client wants a system that tracks their fleet of cars/mats
# plus the passengers, daily trips and all that

"""
Entity Car -> color, number plate, brand, capacity, driven, stop
Entity Driver -> name, dl, age, drivec
Entity Trip ->
"""

# syntax
class Student:
    # should always be present when creating classes in python
    # it always takes self as its first parameter
    # This method is always automatically called when a new instance
    # is created
    def __init__(self, name, age):
        # instance attributes
        self.name = name
        self.age = age

    # we use methods to define behaviors
    # it always takes self as the first param
    def read(self):
        return  f"{self.name} is reading about oop"


# creating an instance of the student class
student1 = Student("Trevor", 20)

print((student1.name))
print(student1.age)
message = student1.read()
print(message)

def greeting():
    print("Good evening")

# parsing
# 1 or 2
print(greeting())

# print(greeting())

student2 = Student("Edna", 23)

print(student2.name)
print(student2.age)
student2.read()

student3 = {
    "name": "Brian",
    "age": 25
}

student4 = {
    "name": "Arif",
    "age": 22
}

# Create a class Person with 3-4 attributes and 2 methods (behaviors)
