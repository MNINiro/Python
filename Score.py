##score=int(input('Enter Highscore:'))
score = 0
for i in range (3):
    A = int(input('Enter Number:'))

    if A > score:
      score = A
      
print(score)
   
