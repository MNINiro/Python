## Matrix multiplication
## in Matrix multiplication, Number of columns of the first matrix must be  equal to number
## of rows of the second matrix


a = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1] ]

b = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9] ]

c = []


##a = [[1, 0, 0], [0, 1, 0], [0, 0, 1] ]
##b = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]
##c = []
 
for row in range (3):
       c.append ([])

       for col in range (3):
              c[row].append (0)

              for aux in range (3):
                     c[row][col] +=  a[row][aux] * b[col][aux]
 
print (c)
