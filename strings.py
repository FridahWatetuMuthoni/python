string = "Hello World"

# returns the length of the string
print(len(string))

# returns the index at which the charater is found
# returns -1 if the charater is not found
print(string.find('x'))

# capatizes the first letter of each world
print(string.capitalize())

# converts string to lowercase
print(string.lower())

# converts string to uppercase
print(string.upper())

# checks if the string is a digit
print(string.isdigit())

# checks if the string contains alphabets
# if there is a space included in the string it returns false
print(string.isalpha())

# counts the occurence of a charater in a string
print(string.count("l"))

# replacing charaters in a string
print(string.replace("l", "x"))

# printing a string multiple times
print(string * 5)

# STRINGS SLICING

# slicing=> create a substring by extracting elements from another string
# using indexing[] or slice()
# [start: stop: step]
str = "Hello World"
