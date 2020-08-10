purchase=[]
sales=[]
names=[]


def pur(name,price):
        while (name != '*') or (price !=0):
            
            names.append(name)
            purchase.append(price)
            print(name,' ',price)
            name=input('enter name:')
            price=float(input('enter purchase price:'))

            
##    return pur;

def sale():
    i=0
    while i < len(purchase):
        s = 0.1 * purchase[i]
        sal = s + purchase[i]
        sales.append(sal)
        print('sales price is:',sal)
        i += 1
##   return sale

nm=input('Enter name:')
pr=float(input('Enter purchase price:'))

pur(nm,pr)

        
print(names)
print(purchase)

sale()
print(sales)
