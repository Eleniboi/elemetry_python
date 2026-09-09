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

    
