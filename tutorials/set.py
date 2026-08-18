#set is an unordered collection of unique element enclosed in a curly bracket, it does not accept duplicate, value in a set can not be access using index

kitchen_items = {"knife", "cup","pot", "pot", "plate","oven"}

print(kitchen_items) #OUTPUT:   {'pot', 'knife', 'cup', 'plate', 'oven'}



#the set() function can also be used to change a list into a set

friends_name = ["samuel", "james", "omafu", "omafu", "lolo"]

unique_friends = set(friends_name)
print(unique_friends)



#the .add() function is used add more content to the set after declaration

unique_friends.add("john")

print(unique_friends)#OUTPUT:  {'omafu', 'james', 'samuel', 'lolo', 'john'}

if len(unique_friends) != 6:
    unique_friends.add("destiny")
print(unique_friends)

# the .update method is use to unpack iterables into a set

children = {"mimi"}

children.update(["job", "abra", "max"])

print(children)



# to get the union of two or more sets use the '|' sign between those sets

first = {1,2,3,3}
second = {3,4,5,6,7}
third = {8,9,9}

union = first | second | third #the union take place here, remember set don't take duplicates

print(union)

# to get the Intersection of two or more sets use the '&' sign between them, it keeps only the items that appeals in all the sets

Intersect = first & second
print(Intersect)