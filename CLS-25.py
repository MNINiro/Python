Array = [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0]
left = 0
NumberOf1 = 0
count = 0
k = int(input("Enter the value of number of zero to be converted to 1:"))
for right in range(len(Array)):
    if Array[right] == 0:
        count = count+1
    while count > k:
        if Array[left] == 0:
            count = count -1
        left = left +1
    if right - left + 1 > NumberOf1:
        NumberOf1 = right - left + 1
if NumberOf1 == 0:
    print('no sequence...')
else:
    print('The longest sequence has length', NumberOf1)