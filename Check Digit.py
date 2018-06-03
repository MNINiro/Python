def checkdigit(lst):

       j=11
       cd=0
       for i in range(len(lst)):
              j-=1
              cd += lst[i] * j

       print(cd)
       rmd = cd % 11
       out = 11 - rmd
       print("Check Digit is :",out)

#===================================

def checkdigitNew(lst):

       a = 1
       b = 3
       cd = 0
       odd = 0
       even = 0
       
       for i in range(len(lstNew)):

              print(lstNew[i])
              if i % 2 == 1:
                    odd += lstNew[i] * a
                    print("Odd :",odd)
              else:
                     even += lstNew[i] * b
                     print("Even :",even)

       cd = odd + even

       print(cd)
       rmd = cd % 10
       out = 10 - rmd
       print("UPC Check Digit is :",out)


       

lstIn = [1, 7, 5, 3, 6, 8, 9, 5, 0 ];
checkdigit(lstIn)

lstNew = [1, 7, 5, 3, 6, 8, 9, 5, 6, 5, 4, 0];
checkdigitNew(lstNew)













