# dictonary = a changeab;e, unordered collection of unique key:value pairs
# fast because they use hashing, allow us to access a value quickly

capitals = {
    "USA": "Washington DC",
    "India": "New Dehli",
    "China": "Beijing",
    "Russia": "Moscow"
}

#adding a key:value element to our dictonary
capitals.update({"Germany": "Berlin"})

#updating the already existing ones
capitals.update({"USA": "Neveda"})

#printing the capital of Russia
#This method returns an error if that key is not found so use "get" instead
print(capitals["Russia"])

#using "get" to check if the key is available
#if the key is available it returns the value else it returns None
value = capitals.get("Germany")
if value != None:
    print(value)
else:
    print("That key was not found in the dictornary")


#listing all the keys in the dictonary
print(capitals.keys())

#printing all the values in the dictonary
print(capitals.values())

#printing the keys and the values of the dictonary
print(capitals.items())

#using pop to remove key pairs in a dictonary
capitals.pop("USA")

#looping thru a dictonary
for element in capitals.items():
    #they are listed as tuples hence can not be changed
    print(element)

#clearing a dictonary
capitals.clear()