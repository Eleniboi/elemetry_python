# functions: a function is a reuseable block of code which perform a specific task
# perimeters: are variable which are place holder for values pass into the function
# Arguments: are the actual value pass into the function when using it

# THE 'def' KEYWORD 
# The standard way to define a function in Python is using the def keyword, followed by the function name, parentheses for optional parameters, and a 


#        parameter
#            |
def greeting(name):
    print(f"Good morning, {name} how are you today")

#       argument
#           |
greeting("samuel") #output: 'Good morning, samuel how are you today'

#Positional vs Keyword Arguments 

# Positional Argument: use position to pass argument into the function wrong positioning can cause bug
# Keyword Argument: here the position of the argument does not matter

def details(name, age, job):
    print(f"welcome {name} you are {age} years old and you work as a/an {job}")

#positional argument
#       |
details("john", 30, "engineer")

#keyword argument
#       |
details(age=30,  job= "engineer", name="john")
#Arbitral argument