def toDec(lst):
       out = 0
       
       for i in reversed(range(len(lst))):
               print(i,lst[i])
               result = list(map(lambda i: 2 ** i, range(len(lst)))) 
                     
               print("2 to the power",i,"is",result[i])
               
               if lst[i] == 1:
                      out += result[i] * lst[i]
                      print(out)
               else:
                      result[i] = 0
                      
         

fst = [0,1,1,1,1,0,1]

lst=[]

for x in reversed(range(len(fst))):
       lst.append(fst[x])
       print(lst)

toDec(lst)
