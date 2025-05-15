class Toyota:

    def __init__(self, model, trim, year):
        self.model = model
        self.trim = trim
        self.year = year

    # magic/dunder
    # returns a printable version of the class instance
    def __repr__(self):
        return f"<Toyota -> Model: {self.model}, Trim: {self.trim}, Year: {self.year}>"


car1 = Toyota("Demio", "Salon", 2022)
car2 = Toyota("New Car", "SUV", 2025)
print(car1, car2)
