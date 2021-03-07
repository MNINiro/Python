no_of_palindromes = 0

for i in range(5):
    
    d1 = input('Enter first digit:')
    d2 = input('Enter second digit:')
    d3 = input('Enter third digit:')
    d4 = input('Enter fourth digit:')

    if (d1 == d4) and (d2 == d3):
        no_of_palindromes += 1

    percentage = no_of_palindromes * 2

print('The numbers were {}% palindromes'.format(percentage))


# =================

count = 0
palindrome = 0
notPalindrome = 0

while count &lt; 50:
    number = str(input(&quot;Please enter a four-digit number: &quot;))
    D1 = number[0]
    D2 = number[1]
    D3 = number[2]
    D4 = number[3]

    if (D4,D3,D2,D1) == (D1,D2,D3,D4):
        palindrome = palindrome + 1
    else:
        notPalindrome = notPalindrome + 1
count = count + 1

total = (palindrome / 50) * 100
print(&quot;The percentage of numbers that were palindromes is&quot;,total,&quot;%&quot;)
