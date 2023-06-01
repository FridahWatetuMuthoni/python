#*args = parameter that will pack all arguements into a tuple
#it is used in a function so that a function can accept a varying amount of arguements

# **kwargs= key word arguements
# the **kwargs parameter packs all arguemnets into a dictonary
#it is usefull in that a function can accept a varying amount of keyword arguments

def add(*args):
    sum = 0
    print(args)
    for num in args:
        sum += num
    return sum;

result = add(10, 20, 30, 40)
print(result)


#casting tuples to lists
def addition(*args):
    sum = 0
    print(args)
    numbers  = list(args)
    numbers[0] = 4
    print(numbers)
    for num in numbers:
        sum += num
    return sum;

result = addition(10, 20, 30, 40)
print(result)

def keyword_arguements(**kwargs):
    for key,value in kwargs.items():
        print(f"key: {key}, value: {value}")

#passing the keyword arguements
keyword_arguements(name="Anna", age=22, city="Nairobi")

def key_words(**kwargs):
    for key, value in kwargs.items():
        print(value, end=" ")

key_words(first="fridah", middle="watetu", last = "muthoni")
print()