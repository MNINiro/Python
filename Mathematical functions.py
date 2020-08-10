import math

x = 2.0

y = -0.0

print(math.copysign(x,y)) # Returns x with the sign of y

print(math.ceil(4.27)) # Returns the smallest integer greater than or equal to x

print(math.floor(3.973)) #Return the floor of x, the largest integer less than or equal to x.

print(math.fabs(-25)) # Return the absolute value of x.

print(math.factorial(5))

print(math.exp(3)) # Return e**x.
##
##
print(math.cos(0)) #Return the cosine of x radians
##
print(math.sin(90)) #Return the sine of x radians
##
print(math.tan(45)) #Return the tangent of x radians.
##
##
print(math.degrees(45)) # Convert angle x from radians to degrees.
##
print(math.radians(2578.3100780887044)) # Convert angle x from degrees to radians.
##
print(math.pi)
##
print(math.trunc(85.265)) # Return the Real value x truncated to an Integral (usually an integer).


##print(math.frexp(2)) # Return the mantissa and exponent of x as the pair (m, e).
##                     # m is a float and e is an integer such that x == m * 2**e exactly.
##                     # If x is zero, returns (0.0, 0), otherwise 0.5 <= abs(m) < 1. 
##
##
##print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])) ##Return an accurate floating point sum of values
                     # in the iterable. Avoids loss of precision by tracking multiple intermediate
                     # partial sums:
