#2D lists- a lists of lists

fruits = ["pineapple", "apples","kiwi","strawberries"]
drinks = ["water", "soda", "tea","coffee"]
deserts = ["cake", "crips", "donuts"]

foods = [fruits, drinks, deserts]

#printing each element in the lists
for food in foods:
    for element in food:
        print(element)