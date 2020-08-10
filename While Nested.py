##a = 1
##while a <= 4:
##       
##       b = 1
##       while b <= 12:
##         z = a * b
####         print(a,'*',b,'=',z)
##         print('%d * %d = %d' % (a, b, a*b)) # %d represents output format
##         b=b+1
##       a=a+1  

stud=[]
sub=[]

i = 1
total = 0

while (i <=2):

       x = input("input ID :")
       stud.append(x)
       i=i+1

       j=1
       while (j <= 2):
              sub.append(float(input("input Subject marks :")))
              j=j+1
              print(sub)
       #        total = total + sub[j]
       # print('Total :', total)

print(stud)
print(sub)


# j = 0
# n = 2
# for i in range(len(stud)):
#        print (stud[i])
#
#        total=0
#        for j in range(j,n):
# ##              print (sub[j])
#               total = total + sub[j]
#        print('Total :', total)
#
#        j = j+1
#        n = n+2
       
