p = 0
i = 0
for i in range(5):
    D1 = int(input("Enter 1st digit :"))
    D2 = int(input("Enter 2nd digit :"))
    D3 = int(input("Enter 3rd digit :"))
    D4 = int(input("Enter 4th digit :"))
    print(D1, D2, D3, D4)

    if (D1 == D4) and (D2 == D3):
        p += 1
print("Percentage of palindrome is", p/i * 100, "%")

# p = 0
# for i in range(3):
#     d1 = int(input("Enter 1st number: "))
#     d2 = int(input("Enter 2nd number: "))
#     d3 = int(input("Enter 3rd number: "))
#     d4 = int(input("Enter 4th number: "))
#     print(d1,d2,d3,d4)
#
#     if (d1 == d4) and (d2 == d3):
#         p += 1
#         print(p)
#     print(i)
#     i += 1
# print(f"Percentage of palindrome is {p/i *100}")