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

#tip - if you want to print on same line, use a comma at the end of print statement
#tip - to print a variable, use {0} {1} ... with .format(elem1,elem2, ...)
#		print ('{0} '.format(element), end=" ")

#tip - range (2,11,2) - returns a list of even numbers from 2 to 11
print('\n Printing Range of numbers:', end=" ")
for i in range(2,11,2):
	print(i, end=" ")

print ("\nNew Example\n\n")
my_list = [1,3, "Michele", [5,6,7]]
print (*my_list)
for elem in my_list:
	print(elem)
