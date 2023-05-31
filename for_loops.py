fruits = ["bananas", "apples", "pineapples", "kiwi"]

print(f"fruit at index 2 is: {fruits[2]}")

for fruit in fruits:
    print(fruit)

# prints (0 => 9)
for index in range(10):
    print(index)

# prints (50 => 99)
for index in range(50, 100):
    print(index)

# You can also add a step as an additional parameter in the range
# the step parameter determines the numbers it skips before it prints the next
for i in range(50, 100, 5):
    print(i)
