#nested function calls=> Function calls inside other function calls
#innermost function calls are resolved first
#returned value is used as an arguement for the next outer function

number = input("Enter a whole positive number:") #number has a global scope

print(round(abs(float(number))))

#scope=The region that a varibale is recognised
#A varibale is only available from inside the region it is created
#a global and locally scoped versions of the varibale can be created

def display_name():
    name = "Code"  #local scope valiable
    print(name)