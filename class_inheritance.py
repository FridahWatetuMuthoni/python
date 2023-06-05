class Animal:

    alive = True

    def eat(self):
        print("The animal is eating")

    def sleep(self):
        print("The animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabit can run")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is fying")

rabbit = Rabbit()
rabbit.eat()
rabbit.run()
fish = Fish()
fish.sleep()
fish.swim()
hawk = Hawk()
hawk.fly()
hawk.alive
