class Animal:
    def eat(self):
        print("This animal is eating")

class Rabit(Animal):
    def eat(self):
        print("The rabit is eating")

rabit = Rabit()
rabit.eat()