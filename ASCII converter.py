# function to convert number to alphabetic equivalent
def numberToAlphabetic(num):
    if num < 5 or num > 30:  # check for valid input
        return "Invalid input"
    else:
        return chr(num + 60)


# test the function
print(numberToAlphabetic(5))  # should return 'A'
print(numberToAlphabetic(30))  # should return 'Z'
print(numberToAlphabetic(3))  # should return 'Invalid input'
print(numberToAlphabetic(35))  # should return 'Invalid input'
