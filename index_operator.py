#index operator [] = gives access to a sequence's element (str,list, tuples)

name = "bro code!"

#checking if the first letter in string is lowercase
if(name[0].islower):
    name = name.capitalize()

print(name)

first_name = name[:3].upper()
last_name = name[4:].lower()
last_charater = name[-1]
print(first_name)
print(last_name)
print(last_charater)