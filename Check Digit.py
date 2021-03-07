#=================== MOD 11 Check ===========================
def checkdigit(lst): # [0,7,4,8,7,4,0,4,6]
       j = 11
       tot = 0

       for i in range(len(lst)):   # 9 times
              j -= 1               # j = j-1
              print('j:',j)
              tot += lst[i] * j    #lst[i] value of the ith position
              print('List element:',lst[i])
              print('Total:',tot)
       rmd = tot % 11
       print('Remainder:',rmd)
       cd = 11 - rmd
       print("Check Digit is :",cd)

#=============New Method======================
def checkdigitNew(lst): # lst = [9,7,8,0,4,3,5,1,8,8,9,3]
       a = 1
       b = 3
       cd = 0
       odd = 0
       even = 0
       for i in range(len(lst)):      # len(lst) = 12. Start=0, end=11
              print(i,'th value :',lst[i])     # lst[i] value of the ith position
              if i % 2 == 1:          # here, i is position
                    odd += lst[i] * b # odd = odd + (lst[i] * b)
                    print("Odd :",odd)
              else:
                     even += lst[i] * a # even = 0 + 9*1
                     print("Even :",even)

       total = odd + even
       print('Total',total)
       rmd = total % 10
       print('Remainder:',rmd)
       out = 10 - rmd
       print("UPC Check Digit is :",out)
lstIn = [0,7,4,8,7,4,0,4,6];
checkdigit(lstIn)
lst = [9,7,8,0,4,3,5,1,8,8,9,3]
checkdigitNew(lst)













