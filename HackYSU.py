#user_input = input("Please Enter a Direction:")

#MOVE(user_input)

# each area is represented as a state

# each state is a function in python

# each state takes user input


def areaOne(userInput):

        if userInput.lower() == 'n':
                return 2
        #elif userInput.lower() == 'w':
                #return 
        #elif userInput.lower() == 'e':
                #return 
        else:
                print("invalid input")
                return 1
        pass

def areaTwo(userInput):
        if userInput.lower() == 'n':
                return 3
            print("You are in area 3")
        pass

def areaThree(userInput):
        if userInput.lower() == 'n':
                return 4
        pass

def areaFour(userInput):
        if userInput.lower() == 'n':
                return 5
        pass
dictionaryOfAreas = {
        1: areaOne,
        2: areaTwo,
        3: areaThree,
        4: areaFour
}

def gameLoop():
        continueGame = True
        currentState = 1
        while continueGame:
                newInput = input('what direction? ')
                currentState = dictionaryOfAreas[currentState](newInput)

gameLoop()
