age = int(input("Enter your age: "))

if (age <= 18 & age != 0):
    print("You are too young to drink")
elif (age >= 18):
    print("You can drink")
else:
    print("Just enter your damn age")

temp = int(input("Enter the current temperature: "))
# when you use "and" (both conditions must be true for the statement to be executed)
if (temp >= 0 and temp <= 30):
    print("The temperature looks amazing go outside")
# when you use "or" (only one must be true for the statement to be executed)
elif (temp < 0 or temp > 30):
    print("The temperature is bad today stay outside")
