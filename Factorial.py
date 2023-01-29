# ans = 1
# f = 5
#
# for i in range(f):
#     ans = ans * f
#     f -= 1
#     print('Factorial is :', ans)


# =================================

# ans = 1
# i = 1
#
# while i <= 5:
#     ans = ans * i
#     i = i + 1
#     print(ans)


# ==========================
# ans = 1
# i = 5
#
# while i > 1:
#     ans = ans * i
#     i = i - 1
#     print(ans)

# ===========================

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# x = factorial(998)
# print(x)


def recur_fibo(n):
    # Recursive function to print Fibonacci sequence
    if n <= 1:
        return n
    else:
        print(n-1)
        print(n-2)
        return recur_fibo(n - 1) + recur_fibo(n - 2)

print(recur_fibo(10))