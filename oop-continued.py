# class -> blueprint of objects are created and how they behave

# Attributes -> instance and class attributes
# Methods -> instance and class methods
# properties -> attributes controlled by methods
# syntax
class Person:
    # class attribute
    # Available  via the class itself
    # avaible in the class instances via the self keyword too
    species = "Homo Habilis"

    # This method gets called automatically when instantiating
    # a class
    # methods with the two underscores are normally called magic
    def __init__(self, name):
        # instance attributes
        # these variables that store data unique to each object
        self.name = name

    # instance methods
    def walk(self, pace):
        return f"{self.name} of species {self.species} is walking with the pace {pace}"

    def capitalize(self):
        return self.name.capitalize()

    def upper(self):
        return self.name.upper()

    # # class methods
    # @classmethod
    # def getSpecies(cls):
    #     print(cls.species)

person1 = Person("John")
print(Person.species)
print(person1.species)
print(person1.name)
person1.name = "Jane"
print(person1.name)

del person1.name

person2 = Person("tony")
# person2.species
print(person2.walk("Fast"))
print(person2.upper())
# print(person2.capitalize())
# print(person2.upper())
# print()

simple_str = "stark"
print(simple_str.upper())

person3 = Person("Thanos")
print(person3.walk("slow"))


class Customer:
    # class attr
    payment_method = "mpesa"
    currency = "KES"

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    # instance method
    def pay(self, amount):
        print(f"Customer {self.name} paid {amount} {self.currency} via {Customer.payment_method}")

    # class methods
    # it is a must to provide the @classmethod decorator when
    # creating/dealing with class methods
    @classmethod
    def example(cls):
        print(f"The currency we use is {cls.currency}")

#
customer1 = Customer("Jane Doe", "0712345678")
customer1.pay(100)
customer1.example()
Customer.example()
Customer.pay(customer1, 1000)

# instance
customer2 = Customer("Trevor Nyigei", "0712345678")
customer2.pay(400)


# PROPERTIES -> attributes controlled by methods
# this means how we get the values and store the values
class Car:
    def __init__(self, name, year):
        # attributes using the underscore indicate that
        # they should only be used/accessed within the
        # class itself and not outside
        self._name = name
        self._year = year

    # getter method
    @property
    def name(self):
        print("Internal", self._name)
        return self._name.upper()

    @property
    def year(self):
        return self._year

    # setter method
    @name.setter
    def name(self, value):
        # check value is equal to audi
        if value == "Audi":
            self._name = value
        else:
            # the raise keyword behaves like the return keyword
            # where they both stop execution
            # it also stops execution of the entire program
            raise ValueError("Car name must be audi")

    @year.setter
    def year(self, value):
        # I prefer to check for falsiness
        if not isinstance(value, int):
            raise ValueError("Year must be an integer")

        self._year = value


car1 = Car("Audi", 2020)
print(car1.name)
# We should no longer access attributes that start with the underscore
# This pattern falls under encapsulation
# print(car1._name)

# is this valid? -> Yes
car1.year = 2030

# is this valid? -> No because we have control of what
# values can be stored
# car1.year = "Twenty twenty five"

car1.name = "Audi"

print(car1.year)

# scenario
class Voter:
    def __init__(self, name, age):
        # if age < 18:
        #     raise ValueError("Age must be above 18")
        self.age_validator(age)

        self._name = name
        self._age = age


    # getter method
    @property
    def age(self):
        return self._age

    # setter method
    @age.setter
    def age(self, value):
        # # validate the data type is an int
        # if not isinstance(value, int):
        #     raise ValueError("Age must be an integer")

        # # condition to check if age is valid
        # if value >= 18:
        #     self._age = value
        # else:
        #     raise ValueError("Age must be above or equal to 18")
        self.age_validator(value)
        self._age = value

    # This is just for reusablity
    def age_validator(self, age):
        if not isinstance(age, int):
            raise ValueError("Age must be an integer")
        if age < 18:
            raise ValueError("Age must be above or equal to 18")
    # create a validation method for age that checks for the datatype
    # and also if it is above or equal to 18

voter1 = Voter("Jane", 23)

# now this gives errors
voter1.age = 13
