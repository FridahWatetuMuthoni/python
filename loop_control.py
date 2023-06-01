#loop control statements-loop control statements change a loop's execution from its normal sequence

#break=> used to terminate the loop entirely
#continue=>skips to the next interation of the loop
#pass=> does nothing acts as a placeholder

while True:
    name = input("Enter your name: ")
    if(name != ""):
        print(f"Your name is : {name}")
        break

phone_number = "123-456-7090"
for num in phone_number:
    if(num.isdigit()):
        print(num, end="")
    else:
        continue
print()

for i in range(21):
    if(i == 13):
        pass
    else:
        print(i)