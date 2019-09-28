#!/cygdrive/c/Users/njcar/Anaconda3/python

# Divisors of a number
# ask the user to input a number, find divisors of that number

userinput = int(input("Divisors of which number: "))
xlist = range(2,userinput)
print (*xlist)
print ("Divisors of {0} are:".format(userinput), end = " ")

for numb in xlist:
	if (userinput % numb) == 0:
		print (numb, end=" ")
