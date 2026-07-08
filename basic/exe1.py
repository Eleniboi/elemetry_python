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

# OUTPUT
# the print function prints output with a new line at default
# if you want content to be on same line u use the end paremeter it is advisible to use it with space like this end=" " for readability
print("samuel you are", end=" ")
print("a great man")