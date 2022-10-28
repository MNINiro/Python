# 0984_w21_qp_22
List1 = 0
List2 = 0
List = int(input('Enter List:'))

while List != -1:
    Value = int(input('Enter value:'))
    if List == 1:
        List1 += Value
    elif List == 2:
        List2 += Value
    else:
        print("Input Error")

    List = int(input('Enter List:'))

print("List 1 = ", List1)
print("List 2 = ", List2)
if List1 > List2:
    print("List 1 is the greatest")
else:
    print("List 2 is the greatest")