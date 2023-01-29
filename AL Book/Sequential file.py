with open("file.txt", "r") as file:
    for line in file:
        print(line)
# In the above example, the open function is used to open the file with the file name "file.txt"
# and the mode "r" for reading. The with statement is used to automatically close the file after
# reading is completed. The for loop is used to iterate through the lines of the file, and the
# print function is used to print each line.
# Similarly, here is an example of how to write to a sequential file in Python:

with open("file.txt", "w") as file:
    file.write("Hello, World!")

# In this example, the open function is used to open the file with the file name "file.txt" and the mode "w" for writing. The with statement is used to automatically close the file after writing is completed. The write function is used to write the string "Hello, World!" to the file.
#
# The open function can also be used to open a file in append mode, which allows you to add new content to the end of an existing file, instead of overwriting the existing content.

with open("file.txt", "a") as file:
    file.write("\nAppended content")

# In this example, the open function is used to open the file with the file name "file.txt" and the mode "a" for appending. The write function is used to append the string "Appended content" to the end of the file.

# It's important to keep in mind that if the file you're trying to open doesn't exist it will create one, if you're running the script multiple times with the same file name it will overwrite the previous one.