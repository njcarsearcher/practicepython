#!/cygdrive/c/Users/njcar/Anaconda3/python

inputstr = input("Input the string to check for palindrome: ")
print('Checking {0} for palindrome'.format(inputstr))

rvsinputstr = inputstr[::-1]

if inputstr == rvsinputstr:
	print('{0} is a palindrome'.format(inputstr))
else:
	print('{0} is not a palindrome'.format(inputstr))



