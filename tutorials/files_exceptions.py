# To open a file in python use the open() function then insert the file name and its mode

with open("file.txt") as file:
    text = file.read()

# Splitting without " " handles newlines and multiple spaces perfectly
words_list = text.split() 

file_content = []

for word in words_list:

    file_content.append(word)

## write to a file using the file name if it does not exist python create it 
with open("output.txt", "w") as output:
    output.write(" ".join(file_content))

print(words_list)
print(file_content)

    
import json


data = {
    "Names": [{16: "omafu samuel", 18: "james akpera", 27: "zeddick otukpa", 15: "emmanuel oduh"}],  # Added comma
    "Job": "software engineers",                                # Added comma
    "school": "l2e",                                            # Added comma
    "age" : [14, 17, 21]
}

with open("data.json", "w") as write_file:
    json.dump(data, write_file, indent=10)

## Error and Exception handling in python helps to prevent your program from crashing during runtime and handle the error seemlessly

## the try key word signifies a beginning of a monitored zone, any program under it run and if it fails instead of crashing it check the except block below it 


try:

    num = input("Input a number: ")
    num1 = int(input("input second number: "))

    answer = num + num1
except ValueError:

    print("Input must be in numbers")
except TypeError:
    print(f"cannot perform operation with data of type {type(num)} with type {type(num1)}")
else:
    print(f"your final answer is {answer}")
