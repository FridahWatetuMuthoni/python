#filter() = creates a collection of elements from an iterable for which a function returns true
#filter(function, iterable)

friends = [
    ("Rachel", 19),
    ("Monica", 18),
    ("Phoebe", 17),
    ("Joey", 16),
    ("Chandler", 21),
    ("Ross", 20)
]

#this functions filters all the ages of 18 and above
age = lambda data: data[1] >=18

drinking_buddies = list(filter(age, friends))

for friend in drinking_buddies:
    print(friend)