#user_input = input("Please Enter a Direction:")

#MOVE(user_input)

# each area is represented as a state

# each state is a function in python

# each state takes user input


def areaOne(userInput):

	if userInput.lower() == 'n':
		print("Entering Area Two")
		return 2
	# elif userInput.lower() == 'w':
	# 	return 2
	# else:
	# print("invalid input")
	#	 return 1
	pass

def areaTwo(userInput):
	if userInput.lower() == 'n':
		print("Entering Area Three")
		return 3
	pass

def areaThree(userInput):
	if userInput.lower() == 'n':
		print("Entering Area Four")
		return 4
	pass

def areaFour(userInput):
	if userInput.lower() == 'n':
		print("Entering Area Five")
		return 5
	pass

def areaFive(userInput):
	if userInput.lower() == 'n':
		print("Entering Area Six")
		return 6
	pass

def areaSix(userInput):
	if userInput.lower() == 'n':
		print("Entering Area Seven")
		return 7
	pass

def areaSeven(userInput):
	if userInput.lower() == 'n':
		print("Entering Area Eight")
		return 8
	pass

def areaEight(userInput):
	if userInput.lower() == 'n':
		print("Entering Area Nine")
		return 9
	pass

def areaNine(userInput):
	if userInput.lower() == 'n':
		return 9
	pass
dictionaryOfAreas = {
	1: areaOne,
	2: areaTwo,
	3: areaThree,
	4: areaFour,
	5: areaFive,
	6: areaSix,
	7: areaSeven,
	8: areaEight,
}

def gameLoop():
	continueGame = True
	currentState = 1
	while continueGame:
		newInput = input('what direction? ')
		currentState = dictionaryOfAreas[currentState](newInput)

gameLoop() 