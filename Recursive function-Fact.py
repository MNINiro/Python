
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)


print(factorial(997))




#======= Fibonacci=========

# Python program to display the Fibonacci sequence up to n-th term using recursive functions
#
# def recur_fibo(n):
#    """Recursive function to print Fibonacci sequence"""
#    if n <= 1:
#        return n
#    else:
#       # print('n-1 :', n - 1)
#       # print('n-2 :', n - 2)
#       return(recur_fibo(n-1) + recur_fibo(n-2))
#
# print(recur_fibo(8))

# ========= Calling module ========
# nterms = 10

# nterms = int(input("How many terms? "))
#
# # check if the number of terms is valid
#
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
# ##      print('Input :',i)
#       print(recur_fibo(i))










       
