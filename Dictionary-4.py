"""
# Using curly braces
students = {}

# Using dict() function
# students = dict()

# To add 5 StudentID and Name as keys and values,
# you can use the assignment operator = or the update() method. For example:

# Using assignment operator
students[101] = "Alice"
students[102] = "Bob"
students[103] = "Charlie"
students[104] = "David"
students[105] = "Eve"

# Using update() method
# students.update({101: "Alice", 102: "Bob", 103: "Charlie", 104: "David", 105: "Eve"})
#
print(students)
"""

# """
# ================Nested Dictionary==================================================
nested_dict = {
  '101': {'key_1': 'value_1'},
  '102': {'key_2': 'value_2'}
}
print(nested_dict)

for inner_dict in nested_dict.values():
    for value in inner_dict.values():
        print(value)
# """

"""
# ==================================================================
# To delete a key-value pair from the dictionary,
# you can use the del keyword or the pop() method. For example:

# Using del keyword
del students[101] # Deletes the key-value pair with key 101
print(students)

"""
"""
# ==================================================================
# To merge two dictionaries,
# you can use the update() method or the | operator. For example:

# Using update() method
# students1 = {101: "Alice", 102: "Bob"}
# students2 = {103: "Charlie", 104: "David"}
# students3 = {105: "Amel", 106: "Biden"}
#
# students1.update(students2) # Updates students1 with key-value pairs from students2
# print(students1)

# Using | operator
students1 = {101: "Alice", 102: "Bob"}
students2 = {103: "Charlie", 104: "David"}

students4 = students1 | students2 | students3 # Creates a new dictionary with key-value pairs from both dictionaries
print(students4)
"""


"""
# ==================================================================
# If you want to keep both values for duplicate keys,
# you can use a custom function that combines the values in a list or a tuple. For example:

# Define a custom function that takes two values and returns a list
def combine_values(v1, v2):
    return [v1, v2]


# Use the | operator with the custom function
students1 = {101: "Alice", 102: "Bob"}
students2 = {102: "Don", 103: "Charlie"}
students3 = students1 | students2  # Creates a new dictionary with key-value pairs from both dictionaries
print(students3)

for key in students3:
    if key in students1 and key in students2:
        # If the key is present in both dictionaries, use the custom function to combine the values
        students3[key] = combine_values(students1[key], students2[key])

print(students3)

# # Output: {101: 'Alice', 102: ['Bob', 'Bobby'], 103: 'Charlie'}
#
# # Alternatively, you can use a dictionary comprehension to achieve the same result. For example:
# # Use a dictionary comprehension with the custom function
# students1 = {101: "Alice", 102: "Bob"}
# students2 = {102: "Bobby", 103: "Charlie"}
# students3 = {k: combine_values(students1[k], students2[k])
# if k in students1 and k in students2
# else (students1.get(k) or students2.get(k))
#              for k in (students1.keys() | students2.keys())}
#
# print(students3)
# Output: {101: 'Alice', 102: ['Bob', 'Bobby'], 103: 'Charlie'}
"""

"""
# ==================================================================
# Create an empty dictionary. Store 5 StudentID and their 3 subjects mark.
# Add these 3 marks then store in a variable called Total.
# Store these total along with their ID in a separate dictionary. Finally, display the result.

# To create an empty dictionary in python, use the curly braces {} or the dict() function. For example:

# Using curly braces
marks = {}

# Using dict() function
# marks = dict()

# To store 5 StudentID and their 3 subjects mark,
# you can use nested dictionaries. For example:

marks = {
  101: {"Math": 80, "English": 75, "Science": 90},
  102: {"Math": 85, "English": 70, "Science": 95},
  103: {"Math": 90, "English": 80, "Science": 100},
  104: {"Math": 95, "English": 85, "Science": 105},
  105: {"Math": 100, "English": 90, "Science":110}
}
# To add these three marks then store in a variable called Total.
# Store these total along with their ID in a separate dictionary. Finally display it. You can use a for loop and the sum() function. For example:

total_marks = {} # Create an empty dictionary for storing total marks

for student_id in marks:
    # Loop through each student ID in marks dictionary
    total = sum(marks[student_id].values()) # Add the values of the nested dictionary and store in total variable
    total_marks[student_id] = total # Store the total along with the student ID in total_marks dictionary

print(total_marks) # Display the total_marks dictionary
# Output: {101:245 ,102:250 ,103:270 ,104:285 ,105:300}
"""

"""
# =================================================================
# Take input from the user then store it in the dictionary

marks = {} # Create an empty dictionary for storing marks

for i in range(5):
    # Loop 5 times to input data for 5 students
    student_id = int(input("Enter student ID: ")) # Input student ID as an integer
    math_mark = int(input("Enter math mark: ")) # Input math mark as an integer
    english_mark = int(input("Enter english mark: ")) # Input english mark as an integer
    science_mark = int(input("Enter science mark: ")) # Input science mark as an integer
    
    marks[student_id] = {"Math": math_mark, "English": english_mark, "Science": science_mark} # Store the marks in a nested dictionary with student ID as key

total_marks = {} # Create an empty dictionary for storing total marks

for student_id in marks:
    # Loop through each student ID in marks dictionary
    total = sum(marks[student_id].values()) # Add the values of the nested dictionary and store in total variable
    total_marks[student_id] = total # Store the total along with the student ID in total_marks dictionary

print(total_marks) # Display the total_marks dictionary
"""
