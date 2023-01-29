n = int(input('Enter value:'))
stars = 1
spaces = n * 2 - 2

for i in range(n * 2 - 1):
    if abs(i - n + 1) <= (n / 6):
        lines = n * 4 - spaces
    else:
        lines = 0
    print(" " * spaces, end="")
    print("*" * max(lines, stars))
    if i < n - 1:
        stars += 2
        spaces -= 2
    else:
        stars -= 2
        spaces += 2
