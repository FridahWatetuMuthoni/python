#multiple inheritance=> when a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("This animal flees")


class Preditor:
    def hunt(self):
        print("This animal is hunting")

class Rabit(Prey):
    pass

class Fish(Prey,Preditor):
    pass

class Hawk(Preditor):
    pass

fish = Fish()
fish.flee()
fish.hunt()