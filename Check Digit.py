def checkdigit(lst): # [1, 5, 6, 3, 2, 7, 8,0,1 ];

       j = 11
       tot = 0
       
       for i in range(len(lst)): # 9 times
              j -= 1
              print('j:',j)
              tot += lst[i] * j
              print('List element:',lst[i])
              print('Total:',tot)

       rmd = tot % 11
       print('Remainder:',rmd)
       cd = 11 - rmd
       print("Check Digit is :",cd)

#===================================

def checkdigitNew(lst):

       a = 1
       b = 3
       cd = 0
       odd = 0
       even = 0
       
       for i in range(len(lstNew)):

              print('i :',lstNew[i])
              if i % 2 == 1:
                    odd += lstNew[i] * b
                    print("Odd :",odd)
              else:
                     even += lstNew[i] * a
                     print("Even :",even)

       cd = odd + even

       print(cd)
       rmd = cd % 10
       out = 10 - rmd
       print("UPC Check Digit is :",out)

lstIn = [1, 5, 6, 3, 2, 7, 8,0,1 ];
checkdigit(lstIn)

lstNew = [1, 7, 5, 3, 6, 8, 9, 5, 6, 5, 4, 0];
##lstNew = [9,7,8,0,4,3,5,1,8,8,9,3]
checkdigitNew(lstNew)













