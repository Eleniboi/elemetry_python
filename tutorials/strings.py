#CHECK STRING

# to check if the a particular word or phrase is in a string use the 'in' keyword
# 

# example
txt = "I love God, and his love reigns for ever"
print("God" in txt)


fruit = ["banana","","orange"]

if "apple" in fruit:
    print("apple of my eye")
    print("apple" in fruit)
else:
    print("omo apple no dey oo")
    print("apple" in fruit)

# you can also check if a particular word or phrase is not in a sentence, using the "not" and "in" key word together

print("apple" not in fruit)# true because there is no apple in the fruit list.





# MODIFY STRING

# the upper() method returns a string in upper case

upr = "Upper case"

print(upr.upper())
# am just trying to upper case a single letter from the string
print(upr[:3]+upr[3].upper()+upr[3+1:])

# the lower() method is use to return a string in lower case
lwr = "LOWER CASE"
print(lwr.lower())


# to remove leading and trailing space you need to use the 'strip()' method to do that
trimspace = "   hello, world   "
print(trimspace.strip())


# the replace() method is use to replace string with a particular string placed in the second peremeter
rep = "you are Good"
print(rep.replace("Good", "Excellent"))

# the split() turns a single string into sections using the operator
split = "samuel.today.na.work"

print(len(split.split(".")))
print(split.split("."))

# String Concatenation

# To combine two or more string together you can use the '+' operator to execute that
a = "hello"
b = "world"

c = a + " " + b

print(c)

# FORMAT-STRING

# f-string is used to format string, it provide string with place holder {}
# with the f"and a string {} the bracket stand as a place holder for an item"

num = 90

text = f"the student are up to {num}"

print(text)

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

num1 = 10 

num2 = 3

txt = f"{num1} ÷ {num2} = {num1/num2:.2f}"

print(txt)

# ESCAPE CHARACTER
# to use character that are illegel in a string use escape \ 

txt = "my name is samuel but my friends call me \\ \"Elene\" "

print(txt)

# STRING METHOD