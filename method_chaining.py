#method chaining= calling multiple methods sequentially. each call performs an action on the same object and returns self

class Car:
    def turn_on(self):
        print("You start the engine")
        return self
    
    def drive(self):
        print("You drive the car")
        return self
    
    def brake(self):
        print("You step on the brake")
        return self
    
    def turn_off(self):
        print("You turn the car off")
        return self

car = Car()

car.turn_on().drive().brake().turn_off()

