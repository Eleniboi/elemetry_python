def userInfo():

    underage = "you are not yet an adult"
    age18 = "you are currently 18 years old"
    age = int(input("Enter your age: "))

    if age < 18:
        return underage
    if age == 18:
        return age18
    return "you are an adult"

print(userInfo())
