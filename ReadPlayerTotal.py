A=0
B=1
C=3
D=5

PlayerTotal = 0
a = 1

while a <= 2:
      
      def SavePlayerTotal(PlayerName, PointsTotal):

            PlayerTotal = 0
            GradeAchieved= input("Enter Grade of Player: ")
            if GradeAchieved==("A"):
                  TA = 0+ PointsTotal 
                  print("Total Point of " + PlayerName.title() + ": ",TA)
            elif GradeAchieved==("B"):
                  TB = 1+ PointsTotal
                  print("Total Point of " + PlayerName.title() + ": ",TB)
            elif GradeAchieved==("C"):
                  TC = 3+ PointsTotal
                  print("Total Point of " + PlayerName.title() + ": ",TC)
            elif GradeAchieved==("D"):
                  TD = 5+ PointsTotal
                  print("Total Point of " + PlayerName.title() + ": ",TD)
            else :
                  print("Invalid Grade")

            PlayerTotal = PlayerTotal + PointsTotal
            return PlayerName.title(), PointsTotal;
                   
      a += 1
      
      PN = input("Enter player name: ")
      PT = int(input("Enter current point: "))
                                 
      SavePlayerTotal(PN, PT)

print(PlayerTotal)
