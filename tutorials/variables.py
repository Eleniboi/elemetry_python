
# Typed variable

number1 = int 

number2 = int 


number1 = "sam's age is "

number2 = 9


print(number1 + str(number2))
# "jitj" 333
# "65" 65
# 44 "44"

# "lkkjj"


# name = input("input your name: ")
# print(f"your name is {name}")

# number1 = input("input first number: ")
# number1 = input("input second number: ")

# if isinstance(number1, int) and isinstance(number2, int):

#     total = int(number1) + int(number2)
#     print(f"your name is {name} and the sum of your number is {total}")
# else:
#     print("can not perform that operation")

# #talentnationairebuild


def elseif(age):


    if age >= 20:
        return "You got the job successfully"
    elif age >= 50:
        return "you are old for this job"
    return "you are a child"

def Checkadult(age):

    allow = False

    if age <= 10:
        print("you are under age")
        return allow

    elif age == 18:
        print("You just became an adult")
        allow = True
        return allow

    print("you are an adult fulltime")
    return allow





def Ticket_calculator():

    print("====Welcome To Ticket Calculator====")

    
    price = 0
    age = int(input("Enter your age: "))

    is_student = bool(input("Are you a student: \n1. True\n2. False ...: ").title())


    if age < 12:
        return f"children pay ${price}"

    elif age >= 12 and age <= 17:
        price += 8
        if is_student == True:
            return f"Teenagers pay ${price - 2} to enter"
        return f"Teenagers pay ${price} to enter"

    elif age >= 18 and age <= 64:
        price += 12
        if is_student == True:
            return f"Adults pay ${price - 2} to enter"
        return f"Adults pay ${price} to enter"
        
    else:
        price += 7
        if is_student == True:
            return f"Adults pay ${price} to enter"
        return f"Seniors pay ${price} to enter"


def main():

    age = 18
    # print(elseif(age))
    # print(Checkadult(age))
    print(Ticket_calculator())

if __name__ == "__main__":
    main()
