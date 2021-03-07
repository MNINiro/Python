count = 0
palindrome = 0
notPalindrome = 0

while count < 5:
    number = str(input("Please enter a four-digit number: "))
    D1 = number[0]
    D2 = number[1]
    D3 = number[2]
    D4 = number[3]
    if (D4,D3,D2,D1) == (D1,D2,D3,D4):
        palindrome = palindrome + 1
    else:
        notPalindrome = notPalindrome + 1

    count = count + 1

total = (palindrome / count) * 100
print("The percentage of numbers that were palindromes is",total,"%")

