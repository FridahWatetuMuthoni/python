#tuple => collection which is ordered and unchangeable 
#they are used to group related items together

student = ("Bro", 21, "male")

#counting how many "bro" are in tuple
print(student.count("Bro"))

#finding the index of an item in the tuple
print(student.index("male"))

for item in student:
    print(item)

if "Bro" in student:
    print("There is a bro here")