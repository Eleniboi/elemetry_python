## OOP: is a programming method that is use to group code into reusable unit called object

## Classes: are blue print use to create an object, it define the structure and behaviour an object

## Object: is an instance of a class which contain the actual data

## Method : a method is a function that is define inside a class and it is tied to an object

class Bank:

    def __init__(self, name="guest", balance=0):
        
        self.name = name
        self.balance = balance
    def deposit(self, amount):

        self._amount = amount
        self.balance = self._amount + self.balance
        print(f"you successfully deposited {self._amount}")

    def withdraw(self, amount):
        self._amount = amount

        if self._amount < self.balance:
            self.balance = self.balance - self._amount
            print(f"withdrawal of {self._amount} was successful")
            return
        else:
            print("Insulficient balance!!")
            print(f"Dear {self.name} would you mind depositing before withdrawing??")
            return
    

user = Bank("samuel")

##the flow of your method in a class matters and also affect how data flows

user.withdraw(5000)#Insulficient balance!!
user.deposit(10000)
user.withdraw(5000)# withdrawal of 5000 was successful



## inheritance the ability of a child class to use attribute and method in a parent class 
class DogBreed:

    def __init__(self, breed):

        self.breed = breed 

# while define the child class the parent class goes into the parenthesis ()
class DogDetails(DogBreed):

    def __init__(self, name, age, breed="Garman shephard"):

        super().__init__(breed)
        self.name = name
        self.age = age 


    def details(self):


        return f"{self.name} is {self.age} years old it a {self.breed}"

dog1 = DogDetails("twilla", 4)

print(dog1.details())