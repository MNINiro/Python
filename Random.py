import random

def decomposition(i):
    i = 10
    
    while i > 0:
        n = random.randint(1, i)
##        yield n
        print(n)    
        i -= n
    

decomposition(5)
