class Car:
    #class variables-> they are accesible to all the objects created from this class
    wheels = 4

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def drive(self):
        print(f"This {self.make} {self.model} is driving")
    
    def stop(self):
        print(f"This {self.make} {self.model} has stopped driving")


car_1 = Car("Chevy", "Covertte", 2021, "blue")
print(car_1.color)
print(car_1.make)
print(car_1.year)
print(car_1.color)
print(car_1.drive())
print(car_1.stop())

car_2 = Car("Ford", "Mustang", 2022, "red")
print(car_2.color)
print(car_2.make)
print(car_2.year)
print(car_2.color)
print(car_2.drive())
print(car_2.stop())