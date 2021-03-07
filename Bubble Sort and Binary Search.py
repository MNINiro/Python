def binary(arr, key):
    start = 0
    end = len(arr) - 1

    r = -1

    while start <= end and r == -1:
        mid = (start + end) // 2

        if arr[mid] == key:
            r = mid
        else:
            if arr[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
    return r

j = 0

def Bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                t = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = t

        print('After pass' + str(i) + ':'),
        print(arr)

    searchItem = int(input("Enter item to search: "))
    found = binary(arr, searchItem)
    if (found == -1):
        print("Key not found")
    else:
        print("Key found in postition: %d " % (found))

#=============== Main Body ===================

arr = []

n = int(input('How many items do you want to sort?'))
for i in range(n):
    data = int(input("Enter data :"))
    arr.append(data)

print("Initial Array: ",arr),
Bubble(arr)





     




