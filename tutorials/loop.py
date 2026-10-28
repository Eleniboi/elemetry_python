# loops are use to execute a block of code repeatedly

# in python we two type of loops, the 'for' and the 'while' loop

#for loop is used to iterate over data structures like list, tuple, dictionary and also range function 

students = ["john", "mary", "joel","peace"]
# for x in students:
#     print(x)

# # for loop with the range function
# num = 5
# for k in range(num):
#     print(k)

# while loop will continue to run as long as a condition is true

num = 10

# while num >= 0:
#     print(num)
#     num -= 1

# password = "grooggy123"

# userlogin = input("enter a password: ").strip()
# count = 3

# while userlogin != password:
#     if count == 1:
#         print("too many attempt!!")
#         break
#     count -= 1
#     print("the password is not correct!")
#     userlogin = input("enter a password: ")
   
# else:
#     print("Login was successful!!")


# John_is_a_boy = True


# while John_is_a_boy:

#     print("John is a Boy")

#     Answer = input("Do you want to still be a boy: \n1. no\n2. yes: ").lower()

#     if Answer == "no" or Answer == "1":
#         print("john is not a boy")
#         John_is_a_boy = False

#     else:
#         continue

#         0         1       2
tup = ("samuel", "omafu", "oloche", "oloche")

for i,  x in enumerate(tup):

    print(i, x)
