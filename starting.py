def MOVE(user_input):
	if(user_input == "NORTH"):
		print("You are going North")
	elif(user_input == "NORTH"):
		print("You are going East")
	elif(user_input == "NORTH"):
		print("You are going West")
	elif(user_input == "NORTH"):
		print("You are going South")
	else:
		print("error")

#user_input = input("Please Enter a Direction:")

#MOVE(user_input)

# each area is represented as a state

# each state is a function in python

# each state takes user input


def areaOne(userInput):

	if userInput.lower() == 'n':
		return 3
	elif userInput.lower() == 'w':
		return 2
	else:
		print("invalid input")
		return 1
	pass

def areaTwo(userInput):
	if userInput.lower() == 'n':
		return 5
	pass


dictionaryOfAreas = {
	1: areaOne,
	2: areaTwo,
}

def gameLoop():
	continueGame = True
	currentState = 1
	while continueGame:
		newInput = input('what direction? ')
		currentState = dictionaryOfAreas[currentState](newInput)

gameLoop()