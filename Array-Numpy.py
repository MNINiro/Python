import numpy as np

##a = np.array([1, 2, 3])                         # Create a rank 1 array
##print(type(a))                                      # Prints "<class 'numpy.ndarray'>"
##print(a.shape)                                      # Prints "(3,)"
##print(a[0], a[1], a[2])                             # Prints "1 2 3"
##
##a[0] = 5                                                   # Change an element of the array
##print(a)                                                   # Prints "[5, 2, 3]"
##
##b = np.array([[1,2,3],[4,5,6]])             # Create a rank 2 array
##print(b.shape)                                      # Prints "(2, 3)"
##print(b[0, 0], b[0, 1], b[1, 0])              # Prints "1 2 4"
##print(b[1, 0], b[1, 1], b[1, 2])  
##
##
##for i in range(2):
##    for j in range(3):
##        print(b[i,j])


##x = [2, 3, 4, 5, 6]
##nums = np.array([2, 3, 4, 5, 6])
##type(nums)
##print(nums)
##    
#=======================

##a = np.zeros((2,2))   # Create an array of all zeros
##print(a)              # Prints "[[ 0.  0.]
##                      #          [ 0.  0.]]"
##
##b = np.ones((1,2))    # Create an array of all ones
##print(b)              # Prints "[[ 1.  1.]]"
##
##c = np.full((2,2), 7)  # Create a constant array
##print(c)               # Prints "[[ 7.  7.]
##                       #          [ 7.  7.]]"
##
##d = np.eye(2)         # Create a 2x2 identity matrix
##print(d)              # Prints "[[ 1.  0.]
##                      #          [ 0.  1.]]"
##
##e = np.random.random((2,2))  # Create an array filled with random values
##print(e)                     # Might print "[[ 0.91940167  0.08143941]
##                             #               [ 0.68744134  0.87236687]]"

#=======================

##random = np.random.randint(1, 100, 5)
##print(random)
##
##xmin = random.min()             #minimum value out of the random numbers
##print(xmin)
##
##xmax = random.max()             #maximum value out of the random numbers
##print(xmax)
##
##print(random.argmax())          #find the index of the maximum and minimum values
##
##print(random.argmin())

#=======================

nums = np.arange(1, 16)
##print(nums[7])
##print(nums[1:8])

nums2 = nums[0:8]
##print(nums2)

# If you add an array with a scalar value, the value will be added to each element in the array.
# Let's add 10 to the nums array and print the resultant array on the console. Here is how you'd do it:

nums3 = nums2 + 10
##print(nums3)

#============ The log Function ===========
#simply returns an array with the log of all elements in the input array
##nums3 = np.log(nums)
##print(nums3)

#============= The exp Function ==========
# returns an array with exponents of all elements in the input array
##nums3 = np.exp(nums)
##print(nums3)

#============= The sqrt Function ==========
##nums3 = np.sqrt(nums)
##print(nums3)

#============= The sin Function ==========
##nums3 = np.sin(nums)
##print(nums3)

#============== Vector Dot Product =========
# Computing the vector dot product for the two vectors can be calculated by multiplying the
# corresponding elements of the two vectors and then adding the results from the products.

##x = np.array([2,4])
##y = np.array([1,3])
##
##dot_product = 0
##
##for a,b in zip(x,y):
##    dot_product += a * b
##
##print(dot_product)
##
### ============ Alternate way=======
##a = x * y
##print(a.sum())
##
##print(x.dot(y))


#=========== Matrix Multiplication ===================
##In order to multiply two matrices, the inner dimensions of the matrices must match, which means that
##the number of columns of the matrix on the left should be equal to the number of rows of the matrix
##on the right side of the product. For instance, if a matrix X has dimensions [3,4] and
##another matrix Y has dimensions of [4,2], then the matrices X and Y can be multiplied together.
##The resultant matrix will have the dimensions [3,2], which is the size of the outer dimensions.


##X = np.array(([1,2,3], [4,5,6]))
##Y = np.array(([1,2], [4,5], [7,8]))
##Z = np.dot(X, Y)
##print(Z)

##Z = np.multiply(X, Y)         # will show error

# The X matrix was successfully able to multiple with itself because the dimensions of the multiplied matrices matched.

##Z = np.multiply(X, X)
##print(Z)

#========== Finding the Inverse of a Matrix ===========

##Y = np.array(([1,2], [3,4]))
##Z = np.linalg.inv(Y)
##print(Z)
##
### to verify if the inverse has been calculated correctly, we can take the dot product of a matrix with its inverse,
### which should yield an identity matrix.
##
##W = Y.dot(Z)
##print(W)


#================== Finding the Trace of a Matrix ====================
# The trace of a matrix is the sum of all the elements in the diagonal of a matrix.
# The NumPy library contains trace function that can be used to find the trace of a matrix.

X = np.array(([1,2,3], [4,5,6], [7,8,9]))
Z = np.trace(X)

print(Z)












































