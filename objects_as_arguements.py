class Car:

    color  = None

def change_color(car,color):
    car.color = color

car1 = Car()
change_color(car1, "red")
car2 = Car()
change_color(car2, "blue")
car3 = Car()
change_color(car3, "white")

print(car1.color)
print(car2.color)
print(car3.color)