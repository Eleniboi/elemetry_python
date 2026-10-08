resources = [
    {
        "id": "R001",
        "name": "Laptop",
        "category": "Electronics",
        "total": 10,
        "available": 10
    },
    {
        "id": "R002",
        "name": "Keyboard",
        "category": "Accessories",
        "total": 5,
        "available": 5
    },
    {
        "id": "R003",
        "name": "Headset",
        "category": "Accessories",
        "total": 3,
        "available": 3
    }
]

# Stores fellows who are allowed to borrow resources.
fellows = {
    "F001": "John",
    "F002": "Mary",
    "F003": "David"
}

# Stores the resources currently borrowed by each fellow.
# Example:
# {
#     "F001": {
#         "R001": 2
#     }
# }
borrowings = {}


# ---------------------------------------------------------
# DISPLAY FUNCTIONS
# ---------------------------------------------------------

def display_resources(resource_list=None):
    """Display resources in a table."""

    if resource_list is None:
        resource_list = resources

    if not resource_list:
        print("\nNo resources found.")
        return

    row_format = "{:<10} | {:<20} | {:<20} | {:<10} | {:<10}"

    print("\n" + row_format.format(
        "ID", "Name", "Category", "Total", "Available"
    ))

    print("-" * 80)

    for resource in resource_list:
        print(row_format.format(
            resource["id"],
            resource["name"],
            resource["category"],
            resource["total"],
            resource["available"]
        ))


# ---------------------------------------------------------
# INPUT VALIDATION
# ---------------------------------------------------------

def get_positive_integer(prompt):
    """Get an integer greater than zero."""

    while True:
        value = input(prompt).strip()

        try:
            number = int(value)

            if number <= 0:
                print("Please enter a positive integer.")
                continue

            return number

        except ValueError:
            print("Please enter a valid whole number.")


def get_non_negative_integer(prompt):
    """Get an integer that is zero or greater."""

    while True:
        value = input(prompt).strip()

        try:
            number = int(value)

            if number < 0:
                print("Please enter zero or a positive integer.")
                continue

            return number

        except ValueError:
            print("Please enter a valid whole number.")


# ---------------------------------------------------------
# FINDING DATA
# ---------------------------------------------------------

def find_resource(resource_id):
    """Find a resource by ID."""

    for resource in resources:
        if resource["id"].lower() == resource_id.lower():
            return resource

    return None


# ---------------------------------------------------------
# ADD RESOURCE
# ---------------------------------------------------------

def add_resource():
    """Add a new resource after validating the input."""

    print("\n--- Add New Resource ---")

    while True:
        resource_id = input("Resource ID: ").strip()

        if not resource_id:
            print("Resource ID cannot be empty.")
            continue

        if find_resource(resource_id):
            print("This resource ID already exists.")
            continue

        break

    while True:
        name = input("Resource name: ").strip()

        if not name:
            print("Resource name cannot be empty.")
            continue

        break

    while True:
        category = input("Resource category: ").strip()

        if not category:
            print("Category cannot be empty.")
            continue

        break

    total = get_positive_integer("Total units: ")

    while True:
        available = get_non_negative_integer("Available units: ")

        if available > total:
            print("Available units cannot be greater than total units.")
            continue

        break

    new_resource = {
        "id": resource_id,
        "name": name,
        "category": category,
        "total": total,
        "available": available
    }

    resources.append(new_resource)

    print("\nResource added successfully.")
    display_resources()


# ---------------------------------------------------------
# FELLOW VALIDATION
# ---------------------------------------------------------

def find_fellow(fellow_id):
    """Check whether a fellow exists."""

    fellow_id = fellow_id.strip().upper()

    if fellow_id in fellows:
        return fellow_id

    return None


# ---------------------------------------------------------
# BORROWING
# ---------------------------------------------------------

def borrow_resource():
    """Allow a fellow to borrow a resource."""

    print("\n--- Borrow Resource ---")

    fellow_id = input("Fellow ID: ").strip().upper()

    if not find_fellow(fellow_id):
        print("Borrowing rejected: fellow ID does not exist.")
        return

    resource_id = input("Resource ID: ").strip()

    resource = find_resource(resource_id)

    if resource is None:
        print("Borrowing rejected: resource ID does not exist.")
        return

    quantity = get_positive_integer("Quantity to borrow: ")

    if quantity > resource["available"]:
        print(
            f"Borrowing rejected: only "
            f"{resource['available']} unit(s) are available."
        )
        return

    # All validation has passed.
    # Only now do we change the inventory.
    resource["available"] -= quantity

    if fellow_id not in borrowings:
        borrowings[fellow_id] = {}

    if resource["id"] not in borrowings[fellow_id]:
        borrowings[fellow_id][resource["id"]] = 0

    borrowings[fellow_id][resource["id"]] += quantity

    print(
        f"Borrowing successful: {fellows[fellow_id]} borrowed "
        f"{quantity} unit(s) of {resource['name']}."
    )


# ---------------------------------------------------------
# RETURNS
# ---------------------------------------------------------

def return_resource():
    """Allow a fellow to return resources currently on loan."""

    print("\n--- Return Resource ---")

    fellow_id = input("Fellow ID: ").strip().upper()

    if not find_fellow(fellow_id):
        print("Return rejected: fellow ID does not exist.")
        return

    if fellow_id not in borrowings or not borrowings[fellow_id]:
        print("This fellow currently has no resources on loan.")
        return

    resource_id = input("Resource ID: ").strip()

    resource = find_resource(resource_id)

    if resource is None:
        print("Return rejected: resource ID does not exist.")
        return

    borrowed_quantity = borrowings[fellow_id].get(resource["id"], 0)

    if borrowed_quantity == 0:
        print(
            "Return rejected: this fellow does not currently "
            "have this resource on loan."
        )
        return

    quantity = get_positive_integer("Quantity to return: ")

    if quantity > borrowed_quantity:
        print(
            f"Return rejected: this fellow only has "
            f"{borrowed_quantity} unit(s) of this resource on loan."
        )
        return

    # All validation has passed.
    resource["available"] += quantity
    borrowings[fellow_id][resource["id"]] -= quantity

    # Remove the resource from the fellow's record
    # if they have returned all units.
    if borrowings[fellow_id][resource["id"]] == 0:
        del borrowings[fellow_id][resource["id"]]

    # Remove the fellow if they have no loans left.
    if not borrowings[fellow_id]:
        del borrowings[fellow_id]

    print(
        f"Return successful: {fellows[fellow_id]} returned "
        f"{quantity} unit(s) of {resource['name']}."
    )


# ---------------------------------------------------------
# SEARCH
# ---------------------------------------------------------

def search_resources():
    """Search resources by name."""

    print("\n--- Search Resources ---")

    search_term = input("Enter resource name: ").strip().lower()

    if not search_term:
        print("Search term cannot be empty.")
        return

    matches = []

    for resource in resources:
        if search_term in resource["name"].lower():
            matches.append(resource)

    if matches:
        display_resources(matches)
    else:
        print("No resources matched your search.")


# ---------------------------------------------------------
# FILTER BY CATEGORY
# ---------------------------------------------------------

def filter_by_category():
    """Filter resources by category."""

    print("\n--- Filter Resources ---")

    category = input("Enter category: ").strip().lower()

    if not category:
        print("Category cannot be empty.")
        return

    matches = []

    for resource in resources:
        if resource["category"].lower() == category:
            matches.append(resource)

    if matches:
        display_resources(matches)
    else:
        print("No resources were found in that category.")


# ---------------------------------------------------------
# REPORTS
# ---------------------------------------------------------

def reports():
    """Generate inventory reports."""

    print("\n--- Resource Reports ---")

    total_units = 0
    available_units = 0

    for resource in resources:
        total_units += resource["total"]
        available_units += resource["available"]

    borrowed_units = total_units - available_units

    print(f"\nTotal units: {total_units}")
    print(f"Available units: {available_units}")
    print(f"Units currently borrowed: {borrowed_units}")

    # Resources with fewer than 3 available units
    low_stock = []

    for resource in resources:
        if resource["available"] < 3:
            low_stock.append(resource)

    print("\nResources with fewer than 3 available units:")

    if low_stock:
        for resource in low_stock:
            print(
                f"- {resource['name']} "
                f"({resource['available']} available)"
            )
    else:
        print("None")

    # Find resource(s) with the most borrowed units
    most_borrowed = []
    highest_borrowed = 0

    for resource in resources:
        borrowed = resource["total"] - resource["available"]

        if borrowed > highest_borrowed:
            highest_borrowed = borrowed
            most_borrowed = [resource]

        elif borrowed == highest_borrowed and borrowed > 0:
            most_borrowed.append(resource)

    print("\nResource(s) with the most units currently borrowed:")

    if highest_borrowed == 0:
        print("None. No resources are currently borrowed.")
    else:
        for resource in most_borrowed:
            print(
                f"- {resource['name']}: "
                f"{highest_borrowed} borrowed"
            )


# ---------------------------------------------------------
# VIEW CURRENT LOANS
# ---------------------------------------------------------

def view_borrowings():
    """Display current borrowing records."""

    print("\n--- Current Borrowing Records ---")

    if not borrowings:
        print("No resources are currently on loan.")
        return

    for fellow_id, loans in borrowings.items():

        print(f"\n{fellow_id} - {fellows[fellow_id]}")

        for resource_id, quantity in loans.items():

            resource = find_resource(resource_id)

            if resource:
                print(
                    f"  {resource['name']}: {quantity} unit(s)"
                )


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main():

    while True:

        print("\n" + "=" * 50)
        print("      LEARN2EARN RESOURCE MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. View resources")
        print("2. Add resource")
        print("3. Borrow resource")
        print("4. Return resource")
        print("5. Search resources")
        print("6. Filter by category")
        print("7. View reports")
        print("8. View current loans")
        print("9. Exit")

        choice = input("\nChoose an option (1-9): ").strip()

        if choice == "1":
            display_resources()

        elif choice == "2":
            add_resource()

        elif choice == "3":
            borrow_resource()

        elif choice == "4":
            return_resource()

        elif choice == "5":
            search_resources()

        elif choice == "6":
            filter_by_category()

        elif choice == "7":
            reports()

        elif choice == "8":
            view_borrowings()

        elif choice == "9":
            print("\nThank you for using Learn2Earn Resource Manager.")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 9.")


if __name__ == "__main__":
    main()