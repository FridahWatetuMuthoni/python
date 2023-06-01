#set= a set is a collection of elements which is unordered, unindexed
#a set has no duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup","knife"}

#adding an item to the set
utensils.add("napkin")

#removing items from the set
utensils.remove("fork")

#adding two sets together
utensils.update(dishes)

for item in utensils:
    print(item)

#joining two sets together and creating a new set
dinner_table = utensils.union(dishes)

for item in dinner_table:
    print(item)

#the difference between the two sets
print(f"utensils difference: {utensils.difference(dishes)}")
print(f"dishes difference: {dishes.difference(utensils)}")

#checking for the common items in both sets
print(utensils.intersection(dishes))

#removing all items from a set
utensils.clear()