fruits = ["pineapple", "apples","kiwi","strawberries"]

for fruit in fruits:
    print(fruit)

#adding an element at the end of the list
fruits.append("bananas")
print(fruits)

#removing an element from a list
for fruit in fruits:
    if(fruit != "kiwis"):
        pass
    else:
        fruits.remove("kiwis")
print(fruits)

#pop() removes the last element of a list or the specified element

#removing the last element
popped_fruit = fruits.pop()
print(popped_fruit)
print(fruits)

#inserting elements at specific indexes
fruits.insert(0, "pears")
print(fruits)

#sorting a list alphabetically
fruits.sort()
print(fruits)
