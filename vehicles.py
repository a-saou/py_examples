# Superclass
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describe(self):
        print("This is a vehicle.")

# Train (Subclass of Vehicle)
class Train(Vehicle):
    def __init__(self, brand, model, cnt):
        self.brand = brand
        self.cnt = cnt

    def describe(self):
        print(f"This is train NO.{self.cnt} ({self.brand})!")

# Car (Subclass of Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def describe(self):
        print(f"This is a car made by {self.brand} (model {self.model}) with {self.doors} doors.")

# Combi, Cabrio, SUV (Subclasses of Car)
class Combi(Car):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model, doors)
        self.model = model

    def describe(self):
        print(f"This is a Combi ({self.brand} {self.model}) with {self.doors} doors!")

class Cabrio(Car):
    def __init__(self, brand, model, doors, roof):
        super().__init__(brand, model, doors)
        self.roof = roof

    def describe(self):
       print(f"This is a Cabrio ({self.brand} {self.model}) with {self.doors} doors!")

class SUV(Car):
    def __init__(self, brand, model, doors, awd):
        super().__init__(brand, model, doors)
        self.awd = awd 

    def describe(self):
       print(f"This is a SUV ({self.brand} {self.model}) with {self.doors} doors!")

train = Train("TGV", "ICE 33", 12)
combi = Combi("BMW", "Family A6", 5)
cabri = Cabrio("Audi", "RS4", 2, "Soft Top")
suv = SUV("Mercedes", "SL99", 5, True)

print()
train.describe()
combi.describe()
cabri.describe()
suv.describe()
msg = 'my message here!'
print(msg)