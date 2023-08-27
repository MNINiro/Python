# Pre-conditional loop
# counter = 1     # initialization
#
# while counter <= 5:     # CONDITION MUST BE TRUE
#     print(counter)
#     counter = counter + 1



#================================
# age = int(input('Enter age:'))
#
# while age < 20:
#     print('child! Not allowed for club membership')
#     age = int(input('Enter data:'))
#
# print('Welcome to the club')
#================================

marks = int(input("Enter initial marks between 0 and 100: "))
while marks < 0 or marks > 100:
    print("Invalid input. Please enter a valid mark between 0 and 100.")
    marks = int(input("Enter marks between 0 and 100: "))
print(f"Accepted marks: {marks}")






#================================

# marks = int(input('Enter marks:'))  # Takes an integer input from the user and stores it in the variable 'marks'
#
# total = 0  # Initializes the variable 'total' to 0
#
# while marks >= 0 and marks <= 100:      # While loop that runs as long as the value of 'marks' is between 0 and 100
#     total = total + marks               # Adds the value of 'marks' to 'total'
#     marks = int(input('Enter marks:'))  # Takes another integer input from the user and updates the value of 'marks'
#
# print('Total:', total)                  # Prints the final value of 'total'


#==============================

# age = [15, 17, 20, 22, 25, 11, 14, 29, 35]
#
# ln = len(age)
# print("Length of the list:", ln)
#
# i = 0
# while i < ln:
#     if age[i] <= 20:
#         print(age[i])
#     i = i + 1






















"""
# ===============
y = [] # Initializes an empty list 'y'
x = str(input('Enter flight 2s/4s/hp:')) # Takes a string input from the user and stores it in the variable 'x'
x = x.upper() # Converts the value of 'x' to uppercase

# While loop that runs as long as the value of 'x' is not '2S', '4S', or 'HP'
while (x != '2S') and (x != '4S') and (x != 'HP'):
    print('Wrong flight has been chosen!', x) # Prints an error message along with the current value of 'x'
    x = str(input('Enter data:')) # Takes another string input from the user and updates the value of 'x'
    x = x.upper() # Converts the value of 'x' to uppercase
else:
    y.append(x) # Appends the final value of 'x' to the list 'y'
    print(y) # Prints the final value of list 'y'
"""

# x = 1 #initialize
# total = 0 #initialize
# while x < 10: #start a loop that runs until x is equal to or greater than 10
#     print("Number:",x) #print the current value of x
#     total = total + x #add x to the total and update it
#     print("Total:",total) # print the current value of total
#     x = x + 2 #increase x by 2 and update it

# NoofSubjects = 0
# totalMarks = 0
#
# while NoofSubjects < 3:
#     marks = int(input("Enter Marks:"))
#     totalMarks += marks
#     NoofSubjects += 1
#
# print("Total Marks:",totalMarks)
# print("Average:", totalMarks/3)
