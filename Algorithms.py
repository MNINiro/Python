"""
# Algorithm-1
total = 0
count = 0
num = 1

while num > 0:
    num = int(input("Enter a number: "))
    if num > 0:
        total += num
        count += 1

average = total / count if count > 0 else 0

print("Count: ", count)
print("Total: ", total)
print("Average: ", average)
"""

'''
# "What is the algorithm that inputs 8 numbers,
# finds the largest and smallest numbers among them,
# and outputs both the largest and smallest numbers?"

largest = -1
smallest = 1000001

for count in range(1, 9):
    number = int(input("Enter a number: "))
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
    print(number)

print("Largest number is ", largest)
print("Smallest number is ", smallest)
'''


import statistics

numbers = [4, 3, 8]
count, total, average = statistics.calculate_statistics(numbers)

print("Count: ", count)
print("Total: ", total)
print("Average: ", average)

