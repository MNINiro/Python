def binary(arr, key):

    start = 0
    end = len(arr) - 1

    r = -1

    while start <= end and r == -1:
        m = (start + end) // 2

        if arr[m] == key:
            r = m
        else:
            if arr[m] > key:
                end = m - 1
            else:
                start = m + 1
    return r

j = 0

def hw(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                t = arr[j]
                arr[j] = arr[j + 1]
                arr[j +  1] = t

        print('After pass' + str(i) + ':'),
        print(arr)

    k = int(input("Enter item to search: "))
    p = binary(arr, k)
    if (p == -1):
        print("Key not found")
    else:
        print("Key found in postition: %d " % (p))



arr = []

n=int(input('How many items do you want to sort?'))
for i in range(n):
    data = int(input("Enter data :"))
    arr.append(data)

print("Initial Array: "),
hw(arr)





     




