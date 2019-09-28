#!/cygdrive/c/Users/njcar/Anaconda3/python

# Have two lists find the common elements between these two lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#tip empty set should be initialized only with set(), not {}
cset = set()

for elem in a:
	if elem in b:
		cset.add(elem)

print (*cset)
