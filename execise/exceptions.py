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
