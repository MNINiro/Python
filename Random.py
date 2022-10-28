import random

##def decomposition(i):
##    i = 10
##    
##    while i > 0:
##        n = random.randint(1, i)
####        yield n
##        print(n)    
##        i -= n
##    
##
##decomposition(5)


def bowling(i):
    score = 0
    result = 0
    
    while i <= 10:
        score = random.randint(1,10)
        print('Score:', score)
        if score == 10:
            score += 5
            print('STRIKE!!!')
        result += score
        i += 1
    print('Total score:',result)

bowling(1)
