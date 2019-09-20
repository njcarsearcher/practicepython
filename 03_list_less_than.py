#!/cygdrive/c/Users/njcar/Anaconda3/python

#Has a list of numbers, ask user which numbers to print
# we go over a loop to check if the number is smaller, print the number

a = [1,1,2,3,5,6,13,21,34,55,89]

print (*a)
print ('From the above list of numbers choose less than which number u want printed')

numbercheck = int(input("Choose a number: "))
for element in a:
	if element < numbercheck:
		print (f'{element}', end=" ")

