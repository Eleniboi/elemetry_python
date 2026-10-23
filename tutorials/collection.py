## LIST 


collection = ["omafu", "jireh","victor","eboh", 1,2,3,4,True,False]

# print(collection)

# boyjireh = collection.pop(1)

# print(collection)
# print(boyjireh)

# collection.insert(3, "jireh")

# print(collection)


# for item in collection:

#     print(item)

# for num in range(len(collection)):

#     print(num)


def Guest_Manager():
    """Manages the guest registration, VIP additions, and security removals."""

    guest_list = []
    for i in range(1, 4):

        name = input(f"Guest {i} Enter your Name: ")
        guest_list.append(name)

    guest_list.insert(0, "VIP_Sherlock")
    guest_list.append("Unwanted_Guest")
    print(guest_list)

    guest_list.remove("Unwanted_Guest")

    removed_guest = guest_list.pop()

    print(f"Sorry, {removed_guest}, the venue is full.")

    print(guest_list)

def main():

    Guest_Manager()

if __name__ == "__main__":
    main()