'''
 Typecode    C data type	    Python data type
    'b'	    signed char	        int
    'h'	    signed short	    int
    'i'	    signed int	        int
    'l'	    signed long	        int
    'q'	    signed long long	int
    'f'	    float	            float
    'B'	    unsigned char	    int
    'H'	    unsigned short	    int
    'I'	    unsigned int	    int
    'L'	    unsigned long	    int
    'Q'	    unsigned long long	int
    'd'	    double	            float
'''

# print('========= example-1 ==========')

import array as a
studentRoll = a.array('i', [101, 102, 103, 104, 105, 106])  # 'i' for integer

# print(studentRoll)
# print(studentRoll[0])


for i in studentRoll:
    print(i)

print()

for j in range(len(studentRoll)):
    print(studentRoll[j])


# for i in studentRoll:
#     print(i)
'''
# Appending data into an array
studentRoll.append(555)
print(studentRoll)

# Delete any data from the array
del studentRoll[5]
print(studentRoll)

# Replace a value
studentRoll[3]=787
print(studentRoll)

ln = len(studentRoll)
print('Number of items:',ln)

print('Position', 'Value')
for i in range(ln):
    print(i,'       ', studentRoll[i])
# print()
'''
# # print('========= example-2 ==========')
# from array import *
# price = array('f',[10.1,30,10.3,20,34.5]) #'f' for float. float also contains integer
#
# for j in price:
#     print(j)
