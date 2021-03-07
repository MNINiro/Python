i = 2 
while(i < 100): 
	j = 2 
	while(j <= (i/j)):
                
		if not(i % j): # The % (modulo) operator yields the remainder
                                #from the division of the first argument by the second.
			break
		j = j + 1 
	if (j > i/j) :
		print (i, " is prime", j)
	i = i + 1 
 
print ("Good bye!")



##A prime number (or a prime) is a natural number greater than 1 that has
##no positive divisors other than 1 and itself. A natural number greater
##than 1 that is not a prime number is called a composite number.
##For example, 5 is prime because 1 and 5 are its only positive integer factors,
##whereas 6 is composite because it has the divisors 2 and 3 in addition to 1 and
##6.
