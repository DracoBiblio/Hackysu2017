#user_input = input("Please Enter a Direction:")

#MOVE(user_input)

# each area is represented as a state

# each state is a function in python

# each state takes user input

class mirror():
	health = 1
	power = 0
	defense = 0
	inventory = ['shard of glass']
	
class spider():
	health = 5
	power = 1
	defense = 0
	inventory = ["spider venom"]

class orc():
	health = 20
	power = 5
	defense = 2
	inventory = ["club"]

class goblin():
	health = 15
	power = 4
	defense = 1
	inventory = ["healing potion"]

class bat():
	health = 10
	power = 4
	defense = 1
	inventory = ["bat fang"]

class rat():
	health = 5
	power = 3
	defense = 0
	inventory = ["rat tail"]

class rocktopus():
	health = 10
	power = 6
	defense = 4
	inventory = ["obsidian shield"]


class character ():
	health = 100
	power = 2
	defense = 0
	inventory = []
	rightarm = ['fists']
	leftarm = []
	gold = 0
	flag1 = False
	flag2 = False
	flag3 = False
	flag3_1 = False
	flag4 = False
	flag5 = False

def reset_enemies():
	mirror.health = 1
	mirror.inventory = ['shard of glass']
	spider.health = 5
	spider.inventory = []
	orc.health = 50
	orc.inventory = ["club"]
def areaOne(userInput):

	room_inventory = ["shovel"]

	if userInput.lower() == 'n' or 'north' or 'move n' or 'move north':
		print("Entering Area Two")
		return 2
	elif userInput.lower() == 'health':
		print(character.health)
		return 1
	elif userInput.lower() == 'inventory':
		print(character.inventory)
		return 1
	elif userInput.lower() == 'status':
		print("You are currently wielding", character.leftarm, character.rightarm, "and you have", character.health, "health", character.power, "power", character.gold, "gold")
		return 1
	# elif userInput.lower() == 'w':
	# 	return 2
	elif character.flag1 == False and userInput.lower() == 'search chest':
		print("You found", room_inventory)
		character.rightarm += ['shovel']
		character.power += 2
		character.flag1 = True
		return 1
	elif userInput.lower() == 'search chest':
		print("it is empty")
		return 1
	elif userInput.lower() == 'look':
		print('You see a chest in the corner and a mirror on the wall')
		return 1
	elif userInput.lower() == 'look mirror':
		print('You see someone in the mirror...but it is only you')
		return 1
	elif userInput.lower() == 'attack mirror':
		print('You are in combat with mirror')
		character.previous_state = 1
		return 101
	else:
	 	print("invalid input")
	 	return 1
	pass

def combat_areaOne_mirror (userInput):
	incombat = True
	while(incombat == True):
		if userInput.lower() == 'attack':
			print('You swing at', mirror, 'with your', character.rightarm, 'dealing', character.power - mirror.defense, 'damage.')
			mirror.health -= (character.power - mirror.defense)
			
			if(mirror.health <= 0):
				print('You have defeated', mirror)
				print('The mirror shatters, the shards cut you.')
				character.health -= 3
				if(character.health <= 0):
					print('You have died')
					print('Game Over')
				print('You find', mirror.inventory, 'on the body.')
				character.inventory += mirror.inventory
				reset_enemies()
				incombat = False
				return character.previous_state
			elif(mirror.health > 0):
				print(mirror, 'Attacks you dealing', mirror.power - character.defense, 'damage.')
				character.health -= (mirror.power - character.defense)
				return 101
			elif(character.health <= 0):
				print('You have died')
				print('Game Over')
			else:
				return 101
		elif userInput.lower() == 'run':
			print('You manage to escape.')
			incombat = False
			return character.previous_state
		else:
			return 101


def areaTwo(userInput):

	if userInput.lower() == 'n':
		print("Entering Area Three")
		return 3
	elif userInput.lower() == 'search':
		print('You did not find anything')
		return 2
	elif character.flag2 == False and userInput.lower() == 'look':
		print('You find an abnormally large spider')
		return 2
	elif character.flag2 == False and userInput.lower() == 'attack spider':
		print('You are in combat with spider')
		character.previous_state = 2
		return 100
	elif userInput.lower() == 'attack spider':
		print('you stomp a pile of guts...you monster')
		return 2
	elif userInput.lower() == 'look':
		print('You see a dead spider')
		return 2
	else:
	 	print("invalid input")
	 	return 2
	pass

def combat_areaTwo_spider (userInput):
	incombat = True
	while(incombat == True):
		if userInput.lower() == 'attack':
			print('You swing at', spider, 'with your', character.rightarm, 'dealing', character.power - spider.defense, 'damage.')
			spider.health -= (character.power - spider.defense)
			
			if(spider.health <= 0):
				print('You have defeated', spider)
				character.flag1 = True
				print('The spider is now a gross pile of guts')
				print('You find', spider.inventory, 'on the body.')
				character.inventory += spider.inventory
				character.flag2 = True
				reset_enemies()
				incombat = False
				return character.previous_state
			elif(spider.health > 0):
				print(spider, 'Attacks you dealing', spider.power - character.defense, 'damage.')
				character.health -= (spider.power - character.defense)
				return 100
			elif(character.health <= 0):
				print('You have died')
				print('Game Over')
			else:
				return 100
		elif userInput.lower() == 'run':
			print('You manage to escape.')
			incombat = False
			return character.previous_state
		else:
			return 100

def areaThree(userInput):

	if userInput.lower() == 'n':
		print("Entering Area Four. You see a Shop(shop), and a Blacksmith(blacksmith).")
		return 4
	elif character.rightarm == ['shovel'] and userInput.lower() == 'use shovel':
		print('you create a hole')
		character.flag3 = True
		return 3
	elif character.flag3_1 == False and userInput.lower() == 'search hole':
		print('You found a shield')
		character.leftarm += ['shield']
		character.power += 2
		character.flag3_1 = True
		return 3
	elif character.flag3 == False and userInput.lower() == 'look':
		print('You see loose dirt')
		return 3
	elif userInput.lower() =='look':
		print('You see a hole')
		return 3
	elif userInput.lower() == 'search hole':		
		print('It is an empty hole')		
		return 3
	elif userInput.lower() == 'status':
		print("You are currently wielding", character.leftarm, character.rightarm, "and you have", character.health, "health", character.power, "power", character.gold, "gold")
		return 3
	else:
	 	print("invalid input")
	 	return 3
	pass

def areaFour(userInput):
	if userInput.lower() == 'n':
		if character.flag4 == False:
			print("You are ambushed by an orc!")
			print("The orc lands a pre-emptive strike for", orc.power - character.defense, "damage.")
			print('You are in combat with orc')
			character.previous_state = 5
			return 102
		print("Entering Area Five")
		return 5
	elif userInput.lower() == 'shop':
		print('You enter the shop. (Exit) to leave the shop.')
		return 4.1
	elif userInput.lower() == 'blacksmith':
		print('You enter the blacksmith. (Exit) to leave the shop.')
		return 4.2
	elif userInput.lower() == 'search':
		print('You did not find anything')
		return 4
	elif userInput.lower() == 'look':
		print('You did not see anything')
		return 4
	else:
	 	print("invalid input")
	 	return 4
	pass
def shop(userInput):		
	if userInput.lower() == 'exit':
		print("Entering Area Four")		
		return 4		
	elif character.rightarm == ['shovel'] and userInput.lower() == 'talk':
		print("You ask the Shop about her wares.")		
		print("'I only have 5 healing potions, but I am willing to buy your shovel and shield for 15 gold'")		
		return 4.1		
	elif userInput.lower() == 'talk':		
		print("You ask the Shop keep about her wares")		
		print("'I can offer 5 healing potions for 5 gold each.'")		
		return 4.1		
	elif character.gold == 0 and userInput.lower() == 'buy':		
		print('You do not have enough gold.')		
		return 4.1		
	elif character.rightarm == ['shovel'] and userInput.lower() == 'sell':		
		print("You sell your shovel for 15 gold")		
		character.rightarm = []		
		character.power = 2		
		character.gold += 15		
		return 4.1		
	elif userInput.lower() == 'buy':		
		print("You purchase a healing potion for 5 gold.")		
		character.gold -= 5		
		character.inventory += ['healing potion']		
		return 4.1		
	elif userInput.lower() == 'status':		
		print("You are currently wielding", character.leftarm, character.rightarm, "and you have", character.health, "health", character.power, "power", character.gold, "gold")		
		return 4.1		
	
def blacksmith(userInput):		
 	if userInput.lower() == 'exit':		
 		print("Entering Area Four")		
 		return 4		
 	elif userInput.lower() == 'talk':		
 		print("You ask the Blacksmith about his items.")		
 		print("I have a trusty sword for sale for 15 gold.")		
 		return 4.2
def areaFive(userInput):
	if userInput.lower() == 'n':
		print("Entering Area Six")
		return 6
	elif userInput.lower() == 'search':
		print('You did not find anything')
		return 5
	elif userInput.lower() == 'look':
		print('You did not see anything')
		return 5
	else:
	 	print("invalid input")
	 	return 5
	pass
def combat_areaFive_orc (userInput):
	incombat = True
	while(incombat == True):
		character.flag4 = True
		if userInput.lower() == 'attack':
			print('You swing at', orc, 'with your', character.rightarm, 'dealing', character.power - orc.defense, 'damage.')
			orc.health -= (character.power - orc.defense)
			
			if(orc.health <= 0):
				print('You have defeated', orc)
				character.flag1 = True
				print('The orc collapses.')
				print('You find', orc.inventory, 'on the body.')
				character.inventory += orc.inventory
				print("Entering Area Five")	
				reset_enemies()
				incombat = False
				return character.previous_state
			elif(orc.health > 0):
				print(orc, 'Attacks you dealing', orc.power - character.defense, 'damage.')
				character.health -= (orc.power - character.defense)
				return 102
			elif(character.health <= 0):
				print('You have died')
				print('Game Over')
			else:
				return 102
		elif userInput.lower() == 'run':
			print('You manage to escape.')
			print("Entering Area Five")	
			incombat = False
			return character.previous_state
		else:
			return 102
def areaSix(userInput):
	if userInput.lower() == 'n':
		print("Entering Area Seven")
		return 7
	elif userInput.lower() == 'search':
		print('You did not find anything')
		return 6
	elif userInput.lower() == 'look':
		print('You did not see anything')
		return 6
	else:
	 	print("invalid input")
	 	return 6
	pass

def areaSeven(userInput):
	if userInput.lower() == 'n':
		print("Entering Area Eight")
		return 8
	elif userInput.lower() == 'search':
		print('You did not find anything')
		return 7
	elif character.flag5 == False and userInput.lower() == 'look':
		print('You see the entrance to a cave being "guarded" by a sleeping goblin')
		return 7
	elif character.flag5 == True and userInput.lower() == 'look':
		print('You see the entrance to the cave being guarded by a dead goblin')
	elif character.flag5 == False and userInput.lower() == 'enter cave':
		print("The sound of your approach wakes the goblin!")
		print("The goblin springs to action, landing the first strike on you for", goblin.power - character.defense, "damage!")
		character.health -= goblin.power - character.defense
		print('You are in combat with goblin')
		character.previous_state = 7
		return 103
	elif character.flag5 == True and userInput.lower() == 'enter cave':
		print("Entering Dungeon")
		return 90	
	elif userInput.lower() == 'attack goblin':
		print('You are in combat with goblin')
		character.previous_state = 7
		return 103
	else:
	 	print("invalid input")
	 	return 7
	pass

def combat_areaSeven_goblin(userInput):
	incombat = True
	while(incombat == True):
		if userInput.lower() == 'attack':
			print('You swing at the goblin with your', character.rightarm, 'dealing', character.power - goblin.defense, 'damage.')
			goblin.health -= (character.power - goblin.defense)
			
			if(goblin.health <= 0):
				print('You have defeated goblin')
				character.flag5 = True
				print('You find', goblin.inventory, 'on the body.')
				character.inventory += goblin.inventory
				print("Entering Dungeon")	
				reset_enemies()
				incombat = False
				return character.previous_state
			elif(goblin.health > 0):
				print('The goblin attacks you dealing', goblin.power - character.defense, 'damage.')
				character.health -= (goblin.power - character.defense)
				return 103
			elif(character.health <= 0):
				print('You have died')
				print('Game Over')
			else:
				return 103
		elif userInput.lower() == 'run':
			print('You manage to escape.')
			print("Returning to area 7")	
			incombat = False
			return character.previous_state
		else:
			return 103

def dungeoneOne_roomOne(userInput):
	if userInput.lower() == 'n':
		print("Entering Dungeon Room 2")
		return 91
	elif userInput.lower() == 's' or 'south' or 'exit' or 'leave' or 'move south':
		return 7
	elif userInput.lower() == 'search':
		print('You did not find anything')
		return 90
	elif userInput.lower() == 'look':
		print('You did not see anything')
		return 90
	else:
		 print("invalid input")
		 return 90
	pass
def areaEight(userInput):
	if userInput.lower() == 'n':
		print("Entering Area Nine")
		return 9
	elif userInput.lower() == 'search':
		print('You did not find anything')
		return 8
	elif userInput.lower() == 'look':
		print('You did not see anything')
		return 8
	else:
		 print("invalid input")
		 return 8
	pass

def areaNine(userInput):
	if userInput.lower() == 'n':
		return 9
	elif userInput.lower() == 'search':
		print('You did not find anything')
		return 9
	elif userInput.lower() == 'look':
		print('You did not see anything')
		return 9
	else:
	 	print("invalid input")
	 	return 9
	pass
dictionaryOfAreas = {
	1: areaOne,
	2: areaTwo,
	3: areaThree,
	4: areaFour,
	4.1: shop,
	4.2: blacksmith,
	5: areaFive,
	6: areaSix,
	7: areaSeven,
	8: areaEight,
	9: areaNine,
	90: dungeoneOne_roomOne,
	100: combat_areaTwo_spider,
	101: combat_areaOne_mirror,
	102: combat_areaFive_orc,
	103: combat_areaSeven_goblin
}

def gameLoop():
	continueGame = True
	currentState = 1
	while continueGame:
		newInput = input('What would you like to do next? ')
		currentState = dictionaryOfAreas[currentState](newInput)

gameLoop() 