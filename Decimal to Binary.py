def convertToBinary(n):
   """Function to print binary number
   for the input decimal using recursion"""
   if n > 1:
       convertToBinary(n//2)
       print(n)
   print(n % 2,end = '') # end = '' to print side by side

# decimal number
dec = 65
convertToBinary(dec)
