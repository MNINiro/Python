def binarySearch(array, search):
    low = 0
    high = len(array) - 1  # to adjust with position
    # print(len(arr))
    found = False

    while (low <= high) and (found == False):
        mid = (low + high) // 2

        if array[mid] == search:
            found = mid
        else:
            if array[mid] > search:
                high = mid - 1
            else:
                low = mid + 1
    return found


if __name__ == '__main__':
    arr = [2, 5, 8, 12, 16, 23, 56, 38, 72, 91]

    search = int(input("Enter item to search:"))
    pos = binarySearch(arr, search)
    if pos == False:
        print("Value not found")
    else:
        print("Value found at position %d" % (pos))

# ===============

# def find(L, target):
#     start = 0
#     end = len(L) - 1
#     found = False
#     while start <= end:
#         middle = (start + end) // 2
#
#
#         if L[middle] == target:
#             found = True
#             print(L[middle])
#             continue
#         else:
#             if L[middle] > target:
#                 end = middle - 1
#             elif L[middle] < target:
#                 start = middle + 1
#
#
# L = ["Brian", "Joe", "Lois", "Meg", "Peter", "Stewie"]
# L = sorted(L)
# result = find(L, "Lois")
# if result == True:
#     print('Name found')
# else:
#     print('Not found')
