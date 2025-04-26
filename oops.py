class Laptop():
    def __init__(self,brand,display,processor,ram,storage,battery):
        self.brand = brand
        self.display = display
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.battery = battery

    def about(self):
        return f"This is {self.brand} laptop with features such as {self.display}, {self.processor}, {self.ram}, {self.storage}, {self.battery}."
    

laptop1 = Laptop("asus","14 inch","intel i5","16gb","512gb","100whr")
laptop2 = Laptop("hp","15 inch","intel i3","64gb","512gb","100whr")
laptop3 = Laptop("dell","16 inch","intel i5","32gb","512gb","100whr")
laptop4 = Laptop("apple","10 inch","M1","8gb","1024gb","1000whr")

print(laptop1.about())
print(laptop2.about())
print(laptop3.about())
print(laptop4.about())

        