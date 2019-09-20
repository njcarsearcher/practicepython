#!/cygdrive/c/Users/njcar/Anaconda3/python

#Ask the user for a number and check if it is odd or even

inputnumber = int(input("Enter a number: "))
x = inputnumber % 2

if x == 0:
	print ('{0} is even'.format(inputnumber))
else:	
	print ('{0} is odd'.format(inputnumber))
