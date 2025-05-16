
# Polymorphism, abstraction, encapsulation - (hiding implementation detials)

# Inheritance -> It allows a class called a child or subclass to inherit
# attributes and methods from another class called the parent or superclass

# basic syntax
class Parent: # parent class
    def __init__(self):
        pass

    def check(self):
        print("Hello from parent class")

parent1 = Parent()
parent1.check()

# child automatically inherits everything from parent
class Child(Parent): # child class that gets all the attributes and methods from parent
    def __init__(self):
        pass

    def grow_up(self):
        print("Child is growing")

child = Child()
child.check()
child.grow_up()

#
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"

    def walk(self):
        return "This person is walking"

person1 = Person("Haji")
print("Person", person1.introduce())
print("Person", person1.walk())

class Student(Person):
    def __init__(self, name):
        # This allows us to access parent methods
        # in this case, we want the student name to be used
        # as the Person name
        super().__init__(name)
        self.name = name

student1 = Student("Robert")
print("Student", student1.walk())
print("<Student>", student1.introduce())

# Example 3
class Animal:
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age

    def eat(self):
        return f"{self.name} is eating"

    def __repr__(self):
        return f"<Animal = Name: {self.name}, Age: {self.age}>"

crabs = Animal("Crabs")
print(crabs)
print("<Animal> ->", crabs.eat())

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    # by redifinig the methods in the parent class,
    # we can be able to override them (polymorphism)
    def eat(self):
        return f"{self.name} is chewing sugar cane"

    # returns a printable version of the instance
    def __repr__(self):
        return f"<Dog = Name: {self.name}, Age: {self.age}>"

dog1 = Dog("Bosco", 3, "Mutina")
#
print("<Dog>", dog1.eat())
print("<Dog>", dog1.name)
print( dog1)


class Car:
    def __init__(self, model):
        self.model = model

    #
    def drive(self, driver = ""):
        return f"Car of model {self.model} is being driven by {driver}"

    def __repr__(self):
        return f"<Car Model: {self.model}>"

car1 = Car("Mercedes")
print(car1)
print("<Car>", car1.drive())

class Toyota(Car):
    def __init__(self, model = "Toyota"):
        super().__init__(model)

    # polymorphism
    def drive(self, driver):
        return f"Toyota is being moved around by {driver}"

toyota1 = Toyota()
print("<Toyota>", toyota1.drive("Jane"))

toyota2 = Toyota("Carina")
print("<Toyota>", toyota2.drive("Wantam"))
