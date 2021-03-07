x = 0
y = 0

num = int(input("Enter number :"))

while num != -1:
    if num > 1000:
        x += 1
    else:
        y += 1
    num = int(input("Enter number :"))

print("values above 1000", x, "times")
print("values below 1000", y, "times")