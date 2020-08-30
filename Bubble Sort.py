# Bubble Sort
# Declare Arr[1 to 10] as Integer

def printArray(arr):
    print (' '.join(str(i) for i in arr))
    
    # The method join() returns a string in which the string elements of sequence
    # have been joined by str separator.
    

def bubblesort(arr):
# Declare i,j as Integer

    for i in range(len(arr)):
        print("i :",i)
        print("len(arr):",len(arr))

        for j in range(len(arr) - i - 1):
            print("j :",j)
            print("len(arr) - i - 1 :",len(arr) - i - 1)
            
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                
                print("arr[j] :", arr[j])
                print("arr[j + 1] :",arr[j + 1])
                print("temp :",temp)
                
                arr[j] = arr[j + 1]
                print("arr[j] :", arr[j])
                
                arr[j + 1] = temp
                print("arr[j + 1] :",arr[j + 1])
                print("")
##               
        # Print array after every pass

        print ("After pass " + str(i) + "  :"),
        printArray(arr)

        print("==============================")

        

arr = [40,20,60,10,50,30]

print ("Initial Array :"),

printArray(arr)

bubblesort(arr)
