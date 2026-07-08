import sys

#this is imported to show the python version  
print(sys.version)



# SYNTAX
# python is very strict with indentation 
if 5 > 2:
    print("five is greater than two!")
if 10 > 5:
    print('ten is greater than five!')

# you can use '' or "" to wrap your string both works
""


# OUTPUT
# the print function prints output with a new line at default
# if you want content to be on same line u use the end paremeter it is advisible to use it with space like this end=" " for readability
print("samuel you are", end=" ")
print("a great man", 19)

# VARIABLE

a = 9 
b = "Your Age"

# CASTING: is use to specify a particular variable

interger = int(5)
string = str("this is for string")
Y = float(4.4)
Z = float(4.4)

print(Y+Z)

# GET THE TYPE: you use the type function to get the type of a variable

us = 5

ustr = "string in python"
print(type(us))
print(type(ustr))

