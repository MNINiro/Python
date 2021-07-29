def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    print('Length:',len(arr),' Pivot:',pivot)

    low = [x for x in arr if x < pivot]
    print('Low :',low)

    middle = [x for x in arr if x == pivot]
    print('Middle: ',middle)

    high = [x for x in arr if x > pivot]
    print('High: ',high)
    print()
    return quicksort(low) + middle + quicksort(high)

print(quicksort([4,2,5,1,3,1,7,6,8]))

