resources = [
    {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
    {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
    {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
    ]

# class Resource_Manager:


 

def Resource_Manager():

    row_format = "{:<15} | {:<15} | {:<15} | {:<15} | {:<15}"

    print("\nWelcome To Learn2Earn Resource Manager")
    print("Current Resources:\n")

    print(row_format.format("ID", "Name", "Category", "Total", "Available\n"))

    for  item in resources:
        print(row_format.format(

            item["id"],
            item["name"],
            item["category"],
            item["total"],
            item["available"]
        ))

    print("\n----Add New Resources----")

    new_id = input("Resources ID: ")

    duplicate = False

    for item in resources:

        if item["id"] == new_id:
            duplicate = True
            break
        
    if duplicate:
        print("this ID already exist")

    else:
        new_name = input("Enter a name: ")
        new_category = input("Enter a category: ")
        new_total = int(input("What the total: "))
        new_available = int(input("Enter it Quantity: "))

        new_resources = {

            "id": new_id,
            "name": new_name,
            "category": new_category,
            "total": new_total,
            "available": new_available
        }

        resources.append(new_resources)

    print("----Updated Resources----")
    for item in resources:
        print(row_format.format(
            item["id"],
            item["name"],
            item["category"],
            item["total"],
            item["available"]
            ))
    
                # print(resources)

def main():
    Resource_Manager()
if __name__ == "__main__":
    main()






    # for  i in range(len(resources)):

    #     for key, value in resources[i].items():
    #         # print(key)
    #         General_Rec[key] = value
    
    #     print(row_format.format(General_Rec["id"],    General_Rec["name"],   General_Rec["category"],   General_Rec["total"],   General_Rec["available"]))
    