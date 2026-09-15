#reading a file's content

# Open "learning.txt" in read-only mode using a context manager
with open("learning.txt", "r") as file:
    # Read all lines from the file into a list of strings
    file_content = file.readlines()
    print(file_content)

    # Append a new sentence 
    file_content.append("\n       I am learning to write code.")
    
    # Initialize an empty list to store the freshly formatted lines
    clean_content = []

    # Loop through the list while tracking the index position of each item
    for indx, line in enumerate(file_content):
        # Remove any existing leading/trailing whitespaces and newline characters (\n)
        line = line.strip()
        
        # If it's NOT the very first line, prepend a newline to separate it from the previous line
        if indx > 0:
            clean_content.append("\n" + line)
        # If it IS the first line, append it raw to prevent an unwanted blank line at the top
        else:
            clean_content.append(line)

# Open "learning.txt" in write mode, which wipes the file clean to start fresh
with open("learning.txt", "w") as appy:
    # Write the entire list of uniquely formatted lines back into the file
    appy.writelines(clean_content)


#Global variables 
Input_errors = 0
Rows_Processed = 0
Total_money = 0.0
file_name = "expense.txt"

#The first instance of a exception block, it only handles "file not found" 
try:
    with open(file_name, "r") as file:

        lines = file.readlines()


        for line in lines:

            line = line.strip()

            if not line:
                continue

            try:
                parts = line.split(",")

                price = float(parts[1])
                Rows_Processed += 1
                Total_money += price

            except (ValueError, IndexError):
                print(f"Value could'nt be coverted or index error found in is line {line}")
                Input_errors += 1
                continue

except FileNotFoundError:

    print(f"{file_name} file does not exist, create one")

finally:
    output = (
        f"=== EXPENSE SUMMARY REPORT === \n"
        f"Total Valid Rows Processed: {Rows_Processed}\n"
        f"Total Skipped Rows (Errors): {Input_errors}\n"
        f"Total Money Spent: {Total_money:.2f}"
    )

    with open("expense_summary.txt", "w") as summay:
        summay.write(output)
