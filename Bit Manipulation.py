# =================Get Bit=================================
# This method is used to find the bit at a particular position(say i)
# of the given number N. The idea is to find the Bitwise AND of the
# given number and 2i that can be represented as (1 << i). If the
# value return is 1 then the bit at the ith position is set. Otherwise, it is unset.
# Function to get the bit at the ith position
def getBit(num, i):
    # Return true if the bit is
    # set. Otherwise return false
    return ((num & (1 << i)) != 0)


# ===================Set Bit===============================
# This method is used to set the bit at a particular position(say i)
# of the given number N. The idea is to update the value of the given
# number N to the Bitwise OR of the given number N and 2i that can be
# represented as (1 << i). If the value return is 1 then the bit at the
# ith position is set. Otherwise, it is unset.
# Function to set the ith bit of the given number num
def setBit(num, i):
    # Sets the ith bit and return
    # the updated value
    return num | (1 << i)



# ===================Clear Bit===============================
# This method is used to clear the bit at a particular position(say i)
# of the given number N. The idea is to update the value of the given
# number N to the Bitwise AND of the given number N and the compliment
# of 2i that can be represented as ~(1 << i). If the value return is 1
# then the bit at the ith position is set. Otherwise, it is unset.
# Function to clear the ith bit of
# the given number N

def clearBit(num, i):
    # Create the mask for the ith
    # bit unset
    mask = ~(1 << i)

    # Return the update value
    return num & mask


N = 70
print("The bit at the 3rd position from LSB is: ", 1 if (getBit(N, 3)) else '0')

print("The value of the given number", "after setting the bit at", "LSB is: ", setBit(N, 0))

print("The value of the given number", "after clearing the bit at", "LSB is: ", clearBit(N, 0))