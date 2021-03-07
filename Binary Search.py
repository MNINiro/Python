def binarySearch(array, SearchValue):
    left = 0
    right = len(array) - 1
    found = False

    while left <= right and found == False:
        mid = (left + right) // 2

        if array[mid] == searchValue:
            found = mid
        else:
            if array[mid] > searchValue:
                right = mid - 1
            else:
                left = mid + 1
    return found

if __name__ == '__main__':
    arr = [2, 5, 3, 12, 16, 23, 38, 56, 72, 91]
    searchValue = int(input("Enter item to search:"))
    pos = binarySearch(arr, searchValue)
    if (pos == False):
        print("Data not found")
    else:
        print("Data found at position %d" % (pos))
