#Higher Order Function=> a funciton that either
# 1. accepts a function as an arguement
#2. Returns a function
#In python function are treated as objects

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

def divisor(x):
    def divided(y):
        return y / x 
    return divided

divide = divisor(2)
print(divide(10))