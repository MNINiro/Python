# Bubble Sort
# Declare Arr[1 to 10] as Integer
def printArray(arr):
    print (' '.join(str(i) for i in arr))

    # The method join() returns a string in which the string elements of sequence
    # have been joined by str separator.
def bubblesort(arr):
# Declare i,j as Integer
    for i in range(len(arr)): # this loop is used for controlling the number of passes
        for j in range(len(arr) - i - 1): # This loop is for actual sorting
            if arr[j] > arr[j + 1]:
                temp = arr[j]                                             
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

        # Print array after every pass

        print ("After pass " + str(i) + "  :"),
        printArray(arr)
        print("==============================")

arr = [7,6,2,1,5]
print ("Initial Array :"),
# printArray(arr)
bubblesort(arr)
