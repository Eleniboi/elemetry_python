## *****Howell Exp*****


def Howell_Exp():


    user_Income = 0
    amount_used = 0
    used_for = ""
    balace = 0
    total_expenses = 0
    item_price = {}
    count = 5

    print("**Welcome to Howell Exp**", end="\n\n")
    user_Income = (input("Input your income : "))
    # print(user_Income)
    # ***Input validation check***

     ## THIS IS A USER VALIDATION CHECK

    # while True:
    #     user_Income = (input("Input your income : "))

        # if user_Income.isdigit():# isdigit is a string attribute which check if a string is an interger
        #     user_Income = int(user_Income)
        #     break
        # else:
        #     count -= 1
        #     print("input must be a number")
        #     print(f"you are left with {count} trials\n")
        #     if count == 0:
        #         print("Please you have to input a valid number!!!")
        #         break
    


    Exit = True

    while Exit:# Loop for users options
            
        choice = input(" 1. continue \n 2. exit \n ...")

        if choice == "continue".lower() or choice == "1":

            amount_used = (input("Input amount spent : "))

            used_for = (input("What was the money used for : " ))

            try:
                amount_used = int(amount_used)
                user_Income = int(user_Income)

                balace = user_Income - amount_used
                item_price[used_for] = amount_used  
                total_expenses = (total_expenses +  amount_used)

            except ValueError:
                count -= 1
                print("user_input or amount_used must be a number")
                print(f"you have {count} more trails!!")
                print(f"{user_Income} cannot perform this operation '-' with {amount_used}")




            Receipt = input("would you like to print recipt? yes/no : ").lower()
            print()

                ## Receipt generator

            if Receipt == "yes":

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
    

   
   
            

def main():
    print(Howell_Exp())

if __name__== "__main__" :
    main()
