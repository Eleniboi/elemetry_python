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
#       ↓
details("john", 30, "engineer")

#keyword argument
#       ↓
details(age=30,  job= "engineer", name="john")


# Parameter Default Values
# Parameter Default value are asign to them during declaration
def tenant(full_name, house_type="bungalow"):
    print(f"mr/mrs {full_name} your house type is {house_type}")

tenant("john swata") #default value will be used
tenant("john swata", "flat") #default will be override


#return value
#functions can send back information using the return statement

def multiplication(num1, num2):
    return num1 * num2


#Arbitrary argument: Arbitrary arguments in Python allow a function to accept an indefinite number of inputs
# *args: collects extra positional arguments into a tuple, the name must not be args but, it must have the prefix '*'
# **kwargs: collects extra keyword arguments into a dictionary 


#arbitrary positional argument
def register(*students):
    first, second, *others = students
    print(f"{first}, {second}, {others} were present")

register("john","emma","raphel","debby","swata")

#arbitrary keyword argument

def details(name, age, **other_details):
    other_details['name'] = name
    other_details['age'] = age
    return other_details

profile = details("mummy", "90", job="engineer", country="nigeria")
print(profile)


## variable scope
# Local scope: variable declared in a particular block of code is called a local variable it can only be used and accessed in that block
#