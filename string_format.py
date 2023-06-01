# str.format() = optional method that gives users more control when diplaying output

animal = "cow"
item = "moon"

print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item))
print("The {1} jumped over the {1}".format(animal, item))
print("The {animal} jumped over the {item}".format(animal="lion", item="sun"))
print("The {animal} jumped over the {animal}".format(animal="lion", item="sun"))

fullname = "My fullname is {} {}"
print(fullname.format("fridah", "watetu"))

name = "Bro"

print("Hello my name is {}".format(name))
print("Hello my name is {:10}. Nice to meet you".format(name))
print("Hello my name is {:<10}. Nice to meet you".format(name))
print("Hello my name is {:>10}. Nice to meet you".format(name))
print("Hello my name is {:^10}. Nice to meet you".format(name))

number = 3.14235

#this displays only the two digits after the decimal point
print("The number pie is {:2f}".format(number))

#this displays only the three digits after the decimal point
print("The number pie is {:3f}".format(number))

num = 100000

#adding a comma at the a thounsand's place
print("The number is {:,}".format(num))

#displaying a number as binary
print("The number is {:b}".format(num))


#displaying a number as octal
print("The number is {:o}".format(num))

#displaying a number as hexadecimal
print("The number is {:X}".format(num))

#displaying a number as scientific notaion
print("The number is {:E}".format(num))


