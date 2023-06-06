#list comprehension => a way to create a new list with less syntax, can mimic certain lambda functiond and they are easier to read
#list = [expression ,for item in iterable, if condition]
#list = [expression,(if else statement), for item iterable ]

#USING LOOPS
squares = []
for i in range (1, 11):
    squares.append(i * i)
print(squares)

#USING LIST COMPREHENSION
squares_2 = [i * i  for i in range(1, 11)]
print(squares_2)

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]

#USING A LAMBDA FUNCTION
passed_students = list(filter(lambda student: student >= 60, students))

#USING LIST COMPREHENSION
passed_students2 = [student  for student in students if student >= 60]
passed_students3 = [student if student >= 60 else "FAILED" for student in students]

print(passed_students)
print(passed_students2)
print(passed_students3)