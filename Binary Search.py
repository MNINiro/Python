def binarySearch(array, key):

    left = 0
    right = len(array) - 1

    res = -1

    while left <= right and res == -1:
        mid = (left + right) // 2

        if array[mid] == key:
            res = mid
        else:
            if array[mid] > key:
                right = mid - 1
            else:
                left = mid + 1

    return res


if __name__ == '__main__':
    arr = [1, 5, 6, 9, 10, 12, 14, 16, 20]
    k = int(input("Enter item to search:"))
    pos = binarySearch(arr, k)
    if (pos == -1):
        print("Key not found")
    else:
        print("Key found at position %d" % (pos))
