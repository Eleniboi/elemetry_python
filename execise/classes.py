#Exercise 1
# Create a class named 'User' with attributes: 'first_name', 'last_name', and 'username'.
# Add an __init__ method to initialize these attributes.
# Add a method 'describe_user' that prints a summary of the user's information.
# Add a method 'greet_user' that prints a personalized greeting.

class User:

    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def describe_user(self):
        print(f"The users first name is {self.first_name}, and last name is {self.last_name}, {self.username} is his/her username")
    
    def greet_user(self):
        print(f"Good morning {self.username}")

pers1 = User("samuel", "omafu", "Eleni")

pers1.describe_user()

pers1.greet_user()



# TODO: Exercise 3
# Create a child class named 'Admin' that inherits from 'User'.
# Add an attribute 'privileges' initialized as a list: ["can add post", "can delete post", "can ban user"].
# Add a method 'show_privileges' that prints the admin's privileges.
# Instantiate an Admin object and call 'show_privileges()'.

class Admin(User):

    def __init__(self, first_name, last_name, username, privileges = None):

        super().__init__(first_name, last_name, username)

        if privileges == None:
            self.privileges = ["can add post", "can delete post", "can ban user"]
        else:
            self.privileges = privileges

    def show_privileges(self):

      for privilege in self.privileges:
        print(privilege)


privilege = Admin("samuel", "omafu", "Eleni")

privilege.show_privileges()