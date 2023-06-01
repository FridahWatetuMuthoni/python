import random
import math

# generating a random number between one and six
random_num_int = random.randint(1, 6)
print(random_num_int)

# generating a random floating point number
random_number = random.random()
print(math.floor(random_number * 10))

# choosing a random item in a list
fruits = ["bananas", "apples", "kiwi", "strawberries"]
fruit = random.choice(fruits)
print(fruit)

# shuffling cards
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)
