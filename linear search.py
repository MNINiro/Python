list = [10,5,7,65,20,8,54]

searchitem = int(input('enter a number:'))

found = 0

for i in range (len(list)):
    if searchitem == list[i]:
        found=1
        print('item found',searchitem, 'in position:',i)

if found==0:
   print('item not found')
   

        
   
