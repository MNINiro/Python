def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
##     print("Current Value :", currentvalue)
##     print("alist[index] :", alist[index])
     
     position = index
##     print("Position :", position)

     
     while position > 0 and alist[position-1] > currentvalue:
##         print("Current Value :", currentvalue)
##         print("alist Position-1 :", alist[position-1])

         alist[position]=alist[position-1]
##         print("alist[position] :", alist[position])
     
         position = position-1
##         print("Position :", position)
         
         
     alist[position]=currentvalue
##     print("alist[position] :", alist[position])
##     
##     print("Position + 1 :", position+1)
##     print("")
     
##alist = [54,26,93,17,77,31,44,55,20]
alist = [85,12,59,45,72,51]
insertionSort(alist)
print(alist)
