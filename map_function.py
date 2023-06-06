#map() = applies a function to each item in an iterable (list, tuple, etc)
#map(function, iterable)

store =[
    ("shirt",20.00),
    ("pants", 25.00),
    ("jacket", 50.00),
    ("socks",10.00)
]

to_euros = lambda data: (data[0], data[1] * 0.82 )
to_dollar = lambda data: (data[0], data[1] / 0.82)

euros_store = map(to_euros, store)
dollar_store = map(to_dollar,store)

for item in euros_store:
    print(item)


for item in dollar_store:
    print(item)