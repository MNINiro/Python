def insertionSort(alist):
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     print("Current Value :", currentvalue)

     position = index

     while position > 0 and alist[position-1] > currentvalue:
         print("Current Value :", currentvalue)
         alist[position] = alist[position-1]
         position = position-1
         print("Position :", position)

     alist[position] = currentvalue
     print("alist[position] :", alist[position])

     print("Position + 1 :", position+1)
     print("")
     
alist = [85,12,59,45,72,51]
insertionSort(alist)
print(alist)
