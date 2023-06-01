#function=a block of code which is executed only when its called

def hello(name):
    print(f"The name that was passed is: {name}")
    print("Hello World")

name = "Dude"
hello(name)

#Return statement- the return statement is used in functions  to send values/objects back to the caller
#These values/objects are known as the functions return value

def add(num1, num2):
    return num1 + num2

result = add(10,20)
print(result)

#keyword arguements= arguements preceded by an identifier when we pass them to a function
#The order of the arguements doesnt matter, unlike positional arguements
#python knows the names of the arguements that our function receives

def fullname(first, middle, last):
    print(f"Hello, {first} {middle} {last}")

fullname(last = "Muthoni", first = "Fridah", middle = "Watetu")