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
