##Global vs. Local variables
##Variables that are defined inside a function body have a local scope,
##and those defined outside have a global scope.
##This means that local variables can be accessed only inside the function
##in which they are declared, whereas global variables can be accessed
##throughout the program body by all functions. When you call a function,
##the variables declared inside it are brought into scope.
##Following is a simple example −

total = 50; # This is global variable.

# Function definition is here

def sum( arg1, arg2 ):

   # Add both the parameters and return them."
     
   total = arg1 + arg2; # Here total is local variable.
   print( "Inside the function local total : ", total)
    
   return total;

##print('Total :',total);
   
   
# Now you can call sum function

sum( 10, 20 );

print('with return value :', sum(5,5)+ total)

print ("Outside the function global total : ", total )


