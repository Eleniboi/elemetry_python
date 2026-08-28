## *****Howell Exp*****


def Howell_Exp():


    user_Income = 0
    amount_used = 0 
    used_for = ""
    balace = 0
    total_expenses = 0
    item_price = {}
    
    print("**Welcome to Howell Exp**", end="\n\n")
    user_Income = (input("Input your income : "))

    if user_Income.isdigit():
        user_Income = int(user_Income)   
    else:
        return "input must be a number"

    Exit = True
    while Exit:
        
        choice = input(" 1. continue \n 2. exit \n ...")

        if choice == "continue".lower() or choice == "1":

            amount_used = int(input("Input amount spent : "))

            used_for = (input("What was the money used for : " ))


            item_price[used_for] = amount_used
            
            balace = user_Income - amount_used
            
            total_expenses = (total_expenses +  amount_used)

            Recipt = input("would you like to print recipt? yes/no : ")
            print()

            if Recipt == "yes".lower():

                print("     ****RECIEPT****   ")
                print(f"{'Item':<12}      {'Price':>3}")
                print(f"{'Income':<12}      ₦ {user_Income:>3}")
                print("-" * 25)

                for key, value in item_price.items():

                    print(f"{key:<12}      -₦ {value:>3}")
                print("-" * 25)    
                print(f"{'Balance':<12}      ₦ {balace:>3}")

                continue
        elif choice == "exit".lower() or choice == "2":
            print("Goodbye!!!")
            Exit = False
            

    print(f"income is ₦{user_Income} ")
    print(f"amount spent ₦{amount_used}")
    print(f"money used for {used_for}")

def main():
    Howell_Exp()

if __name__== "__main__" :
    main()


# num = input("input : ")

# if num == num.isdigit(num):
#     print("true")
# else:
#     print("num is not a number")

# print(int("a", 16))