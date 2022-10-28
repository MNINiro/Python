M1 = [
    [8,14,-6],
    [12,7,4],
    [-11,3,21]
]

M2 = [[3, 16, -6],
      [9,7,-4],
      [-1,3,13]]

M3  = [[0,0,0],
       [0,0,0],
       [0,0,0]]

t1=0
for i in range(len(M1)):
    r1 = 0
    for j in range(3):
        print('r1:',r1)
        print("M1[i][j]:",M1[i][j])
        r1 = r1 + M1[i][j]
    t1 = t1 + r1
    print('Row sum:',r1)
    print()
print('total matrix sum:',t1)


#To Add M1 and M2 matrices
for l in range(len(M1)):
    for k in range(len(M2)):
        M3[l][k] = M1[l][k] + M2[l][k]

#To Print the matrix
print("The sum of Matrix M1 and M2 = ", M3)