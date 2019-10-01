#!/cygdrive/c/Users/njcar/Anaconda3/python
#import sys

def compare(u1, u2):
	if u1 == u2:
		return ("Its a tie")
	elif u1 == 'rock':
		if u2 == 'scissors':
			return ("Rock wins!")
		else:
			return("Paper wins!")
	elif u1 == 'scissors':
		if u2 == 'paper':
			return ("Scissors wins!")
		else:
			return ("Rock wins!")
	elif u1 == 'paper':
		if u2 == 'rock':
			return ("Paper wins!")
		else:
			return ("Scissors wins!")
	else:
		return ("Invalid input! try again")
		sys.exit()

print ("Want to Play Rock Paper Scissors")
option = input("Enter 'quit' if you want to stop: ")

if (option != "quit"):
	option1 = input("User1 choose rock/paper/scissors: ")
	option2 = input("User2 choose rock/paper/scissors: ")
	print (compare(option1, option2))

