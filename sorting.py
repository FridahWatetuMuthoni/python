#sort() method => used with lists
#sorted() function => used with iterables

students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"]
students_2= ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs")

#sorting lists
students.sort(reverse=True) #sorting alphabetically in reverse

for student in students:
    print(student)

#sorting iteratables
#sorted_students = sorted(students_2)
sorted_students = sorted(students_2, reverse=True)

for student in sorted_students:
    print(student)

#sorting complex data-lists
students_3 = [
    ("Squidward", "F", 60),
    ("Sandy", "A", 33),
    ("Patrick", "D", 36),
    ("Spongebob", "B", 20),
    ("Mr.Krabs", "C", 78)
]

grade = lambda grades: grades[1]
ages = lambda ages: ages[2]
#students_3.sort(key=grade)
students_3.sort(key=grade, reverse=True)

for student in students_3:
    print(student)


#sorting complex data-tuple
students_4 = (
    ("Squidward", "F", 60),
    ("Sandy", "A", 33),
    ("Patrick", "D", 36),
    ("Spongebob", "B", 20),
    ("Mr.Krabs", "C", 78)
)

grade = lambda grades: grades[1]
ages = lambda ages: ages[2]
students_sorted = sorted(students_4, key=ages)

for student in students_sorted:
    print(student)