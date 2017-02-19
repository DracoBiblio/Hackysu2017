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
	inventory = []

class orc():
	health = 50
	power = 6
	defense = 1
	inventory = []

class goblin():
	health = 15
	power = 8
	defense = 4
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

class jim():
	health = 41
	power = 7
	defense = 5
	inventory = ["Ashes of Jim"]

class dittrich():
	health = 100
	power = 22
	defense = 3
	inventory = ["Napkins, Plastic Bag"]

class character ():
	health = 100
	power = 2
	defense = 0
	inventory = []
	rightarm = ['fists']
	leftarm = []
	gold = 0
	healing_potion = 0
	flag0 = False
	flag1 = False
	flag2 = False
	flag3 = False
	flag3_1 = False
	flag4 = False
	flag5 = False
	flag6 = False
	help = ["Your commands are:", '\n' "move north","look","search 'thing'","status","use 'item'", "attack 'creature'", "inventory", '\n' "*In battle commands*:","run","attack",'\n' "*Vender commands*:","sell","talk","buy"]
# def help ():
# 	commands = ["look",
# 	"search",
# 	"status",
# 	"attack 'creature'",
# 	"*In battle commands*:"
# 	"run",
# 	"buy"
# 	"*Vender commands*:"
# 	"sell"
# 	"talk"]
def reset_enemies():
	mirror.health = 1
	mirror.inventory = ['shard of glass']
	spider.health = 5
	spider.inventory = ["spider venom"]
	orc.health = 20
	orc.inventory = ["club"]
	goblin.health = 15
	goblin.inventory = ["healing potion"]
	bat.health = 10
	bat.inventory = ["bat fang"]
	rat.health = 5
	rat.inventory = ["rat tail"]
	rocktopus.health = 10
	rocktopus.inventory = ["obsidian shield"]
print("Type 'help'")
def areaOne(userInput):
	
	room_inventory = ["shovel"]

	if userInput.lower() == "move north":
		print("Entering Area Two")
		return 2
		
	elif userInput.lower() == 'help':
		for element in character.help:
			print(element)
		return 1
	elif userInput.lower() == 'debug':
		return 10
	elif userInput.lower() == 'use healing potion' and character.healing_potion >= 1:
		character.healing_potion += -1
		character.health += 10
		print('You injested your healing potion.')
		print('Instantly restored 20 health.')
		if character.health > 100:
			character.health = 100
		return 1
	elif userInput.lower() == 'health':
		print(character.health)
		return 1
	elif userInput.lower() == 'inventory':
		print(character.inventory)
		return 1
	elif userInput.lower() == 'status':
		print("You are currently wielding", character.leftarm, character.rightarm, "and you have", character.health, "health", character.power, "power", character.defense, "defense", character.gold, "gold", character.healing_potion, 'healing potions')
		return 1
	# elif userInput.lower() == 'w':
	# 	return 2
	elif character.flag1 == False and userInput.lower() == 'search chest':
		print("You found", room_inventory)
		character.rightarm = ['shovel']
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
		if (character.health <= 0):
			print('You have died')
			print('Game Over')
			return 19
		elif userInput.lower() == 'attack':
			print('You swing at', "mirror", 'with your', character.rightarm, 'dealing', character.power - mirror.defense, 'damage.')
			mirror.health -= (character.power - mirror.defense)
			
			if(mirror.health <= 0):
				print('You have defeated', "mirror")
				print('The mirror shatters, the shards cut you.')
				character.health -= 3
				if(character.health <= 0):
					print('You have died')
					print('Game Over')
					return 19
				print('You find', mirror.inventory, 'on the body.')
				character.inventory = mirror.inventory
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
				break
			else:
				return 101
		elif userInput.lower() == 'run':
			print('You manage to escape.')
			incombat = False
			return character.previous_state
		else:
			return 101


def areaTwo(userInput):

	if userInput.lower() == "move north":
		print("Entering Area Three")
		return 3
	elif userInput.lower() == 'search':
		print('You did not find anything')
		return 2
	elif userInput.lower() == 'use healing potion' and character.healing_potion >= 1:
		character.healing_potion += -1
		character.health += 10
		print('You injested your healing potion.')
		print('Instantly restored 20 health.')
		if character.health > 100:
			character.health = 100
		return 2
	elif userInput.lower() == 'help':
		for element in character.help:
			print(element)
		return 2
	elif character.flag2 == False and userInput.lower() == 'look':
		print('You find an abnormally large spider')
		return 2
	elif character.flag2 == False and userInput.lower() == 'attack spider':
		print('You are in combat with spider')
		character.previous_state = 2
		return 100
	elif userInput.lower() == 'status':
		print("You are currently wielding", character.leftarm, character.rightarm, "and you have", character.health, "health", character.power, "power", character.defense, "defense", character.gold, "gold", character.healing_potion, 'healing potions')
		return 2
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
		if (character.health <= 0):
			print('You have died')
			print('Game Over')
			return 19
		elif userInput.lower() == 'attack':
			print('You swing at', 'spider', 'with your', character.rightarm, 'dealing', character.power - spider.defense, 'damage.')
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
				print('spider', 'Attacks you dealing', spider.power - character.defense, 'damage.')
				character.health -= (spider.power - character.defense)
				return 100
			elif(character.health <= 0):
				print('You have died')
				print('Game Over')
				return 19
			else:
				return 100
		elif userInput.lower() == 'run':
			print('You manage to escape.')
			incombat = False
			return character.previous_state
		else:
			return 100

def areaThree(userInput):

	if userInput.lower() == "move north":
		print("Entering Area Four. You see a Shop(shop), and a Blacksmith(blacksmith).")
		return 4
	elif character.rightarm == ['shovel'] and userInput.lower() == 'use shovel':
		print('you create a hole')
		character.flag3 = True
		return 3
	elif userInput.lower() == 'help':
		for element in character.help:
			print(element)
		return 3
	elif character.flag3_1 == False and userInput.lower() == 'search hole':
		print('You found a shield')
		character.leftarm += ['shield']
		character.defense = 1
		character.flag3_1 = True
		return 3
	elif userInput.lower() == 'use healing potion' and character.healing_potion >= 1:
		character.healing_potion += -1
		character.health += 10
		print('You injested your healing potion.')
		print('Instantly restored 20 health.')
		if character.health > 100:
			character.health = 100
		return 3
	elif character.flag3 == False and userInput.lower() == 'look':
		print('You see loose dirt')
		return 3
	elif userInput.lower() =='look':
		print('You see a hole')
		return 3
	elif userInput.lower() == 'inventory':
		print(character.inventory)
		return 3
	elif userInput.lower() == 'search hole':		
		print('It is an empty hole')		
		return 3
	elif userInput.lower() == 'status':
		print("You are currently wielding", character.leftarm, character.rightarm, "and you have", character.health, "health", character.power, "power", character.defense, "defense", character.gold, "gold", character.healing_potion, 'healing potions')
		return 3
	else:
	 	print("invalid input")
	 	return 3
	pass

def areaFour(userInput):
	if userInput.lower() == "move north":
		if character.flag4 == False:
			print("You are ambushed by an orc!")
			print("The orc lands a pre-emptive strike for", orc.power - character.defense, "damage.")
			character.health -= orc.power - character.defense
			print('You are in combat with orc')
			character.previous_state = 5
			return 102
		print("Entering Area Five")
		return 5
	elif userInput.lower() == 'help':
		for element in character.help:
			print(element)
		return 4
	elif userInput.lower() == 'use healing potion' and character.healing_potion >= 1:
		character.healing_potion += -1
		character.health += 10
		print('You injested your healing potion.')
		print('Instantly restored 20 health.')
		if character.health > 100:
			character.health = 100
		return 4	
	elif userInput.lower() == 'shop':
		print('You enter the shop. (Exit) to leave the shop.')
		return 4.1
	elif userInput.lower() == 'inventory':
		print(character.inventory)
		return 4
	elif userInput.lower() == 'status':
		print("You are currently wielding", character.leftarm, character.rightarm, "and you have", character.health, "health", character.power, "power", character.defense, "defense", character.gold, "gold", character.healing_potion, 'healing potions')
		return 4
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
		print("Entering Area Four. You see a Shop(shop), and a Blacksmith(blacksmith).")
		return 4
	elif userInput.lower() == 'help':
		for element in character.help:
			print(element)
		return 4.1
	elif character.rightarm == ['shovel'] and userInput.lower() == 'talk':
		print("You ask the Shop about her wares.")
		print("'I only have 5 healing potions, but I am willing to buy your shovel for 15 gold'")
		return 4.1
	elif userInput.lower() == 'talk':
		print("You ask the Shop keep about her wares")
		print("'I can offer healing potions for 5 gold each.'")
		return 4.1
	elif character.gold == 0 and userInput.lower() == 'buy':
		print('You do not have enough gold.')
		return 4.1
	elif character.rightarm == ['shovel'] and userInput.lower() == 'sell':
		print("You sell your shovel for 15 gold")
		character.rightarm = ['fists']
		character.power = 2
		character.gold += 15
		return 4.1
	elif userInput.lower() == 'buy':
		print("You purchase a healing potion for 5 gold.")
		character.gold -= 5
		character.healing_potion += 1
		return 4.1
	elif userInput.lower() == 'status':
		print("You are currently wielding", character.leftarm, character.rightarm, "and you have", character.health, "health", character.power, "power", character.defense, "defense", character.gold, "gold", character.healing_potion, 'healing potions')
		return 4.1
	elif userInput.lower() == 'inventory':
		print("inventory", character.inventory)
		return 4.1
	else:
		print("invalid input")
		return 4.1
	
	
def blacksmith(userInput):
	if userInput.lower() == 'exit':
		print("Entering Area Four. You see a Shop(shop), and a Blacksmith(blacksmith).")
		return 4
	elif userInput.lower() == 'help':
		for element in character.help:
			print(element)
		return 4.2
	elif userInput.lower() == 'talk':
		print("You ask the Blacksmith about his items.")
		print("'I have a trusty sword for 14 gold.'")
		return 4.2
	elif character.gold >= 15 and userInput.lower() == 'buy':
		print('You purchased the sword')
		character.gold -= 14
		character.rightarm = ['sword']
		character.power = 10
		return 4.2
	elif character.gold < 15 and userInput.lower() == 'buy':
		print('You do not have enough coins')
		return 4.2
	elif userInput.lower() == 'status':
		print("You are currently wielding", character.leftarm, character.rightarm, "and you have", character.health, "health", character.power, "power", character.defense, "defense", character.gold, "gold", character.healing_potion, 'healing potions')
		return 4.2
	else:
		print("Invalid input")
		return 4.2

def areaFive(userInput):
	if userInput.lower() == "move north":
		print("Entering Area Six.")
		print("A mist slowly fills around you, covering everything you once saw")
		print("A voice echos, You must go into the dongeon to find the eight peices of the trinity to activate the portal in Young's town")
		return 6
	elif userInput.lower() == 'help':
		for element in character.help:
			print(element)
		return 5
	elif userInput.lower() == 'use healing potion' and character.healing_potion >= 1:
		character.healing_potion += -1
		character.health += 10
		print('You injested your healing potion.')
		print('Instantly restored 20 health.')
		if character.health > 100:
			character.health = 100
		return 5
	elif userInput.lower() == 'search':
		print('You did not find anything')
		return 5
	elif userInput.lower() == 'look':
		print('You did not see anything')
		return 5
	elif userInput.lower() == 'inventory':
		print(character.inventory)
		return 1
		5
	elif userInput.lower() == 'status':
		print("You are currently wielding", character.leftarm, character.rightarm, "and you have", character.health, "health", character.power, "power", character.defense, "defense", character.gold, "gold", character.healing_potion, 'healing potions')
		return 5
	else:
	 	print("invalid input")
	 	return 5
	pass
def combat_areaFive_orc (userInput):
	incombat = True
	while(incombat == True):
		character.flag4 = True
		if (character.health <= 0):
			print('You have died')
			print('Game Over')
			return 19
		elif userInput.lower() == 'attack':
			print('You swing at', 'orc', 'with your', character.rightarm, 'dealing', character.power - orc.defense, 'damage.')
			orc.health -= (character.power - orc.defense)
			
			if(orc.health <= 0):
				print('You have defeated', orc)
				character.flag4 = True
				print('The orc collapses.')
				# print('You find', orc.inventory, 'on the body.')
				# character.inventory += orc.inventory
				print("Entering Area Five")	
				reset_enemies()
				incombat = False
				return character.previous_state
			elif(orc.health > 0):
				print('orc', 'Attacks you dealing', orc.power - character.defense, 'damage.')
				character.health -= (orc.power - character.defense)
				return 102
			elif(character.health <= 0):
				print('You have died')
				print('Game Over')
				return 19
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
	if userInput.lower() == "move north":
		print("Entering Area Seven")
		return 7
	elif userInput.lower() == 'help':
		for element in character.help:
			print(element)
		return 6
	elif userInput.lower() == 'use healing potion' and character.healing_potion >= 1:
		character.healing_potion += -1
		character.health += 10
		print('You injested your healing potion.')
		print('Instantly restored 20 health.')
		if character.health > 100:
			character.health = 100
		return 6
	elif userInput.lower() == 'search':
		print('You did not find anything')
		return 6
	elif userInput.lower() == 'look':
		print('You did not see anything')
		return 6
	elif userInput.lower() == 'status':
		print("You are currently wielding", character.leftarm, character.rightarm, "and you have", character.health, "health", character.power, "power", character.defense, "defense", character.gold, "gold", character.healing_potion, 'healing potions')
		return 6
	else:
	 	print("invalid input")
	 	return 6
	pass

def areaSeven(userInput):
	if userInput.lower() == 'search':
		print('You did not find anything')
		return 7
	elif userInput.lower() == 'help':
		for element in character.help:
			print(element)
		return 7
	elif userInput.lower() == 'inventory':
		print(character.inventory)
		return 7
	elif userInput.lower() == 'use healing potion' and character.healing_potion >= 1:
		character.inventory.remove("healing potion")
		character.health += 10
		print('You injested your healing potion.')
		print('Instantly restored 20 health.')
		if character.health > 100:
			character.health = 100
		return 7
	elif character.flag5 == True and userInput.lower() == 'move north':
		return 8
	elif userInput.lower() == 'status':
		print("You are currently wielding", character.leftarm, character.rightarm, "and you have", character.health, "health", character.power, "power", character.defense, "defense", character.gold, "gold", character.healing_potion, 'healing potions')
		return 7
	elif character.flag5 == False and userInput.lower() == 'look':
		print('You see the entrance to a cave being "guarded" by a sleeping goblin to your north')
		return 7
	elif character.flag5 == True and userInput.lower() == 'look':
		print('You see the entrance to the cave being guarded by a dead goblin')
		return 7
	elif character.flag5 == False and userInput.lower() == 'move north':
		print("The sound of your approach wakes the goblin!")
		print("The goblin springs to action, landing the first strike on you for", goblin.power - character.defense, "damage!")
		character.health -= goblin.power - character.defense
		print('You are in combat with goblin')
		return 103
	elif character.flag5 == True and userInput.lower() == 'attack goblin':
		print("The goblin is already dead")
		return 7

	elif userInput.lower() == 'attack goblin':
		print('You are in combat with goblin')
		return 103

	elif character.inventory == ['shard of glass'] and userInput.lower() == 'use':
		print('You used the shard of glass on the goblin')
		print('The goblin is horrified by its own reflection')
		print('As if by shear disgust, the goblins head explodes!!')
		print('You find', goblin.inventory, 'on the body.') 
		character.healing_potion += 1
		character.flag5 = True
		return 8

	else:
	 	print("invalid input")
	 	return 7
	pass

def combat_areaSeven_goblin(userInput):
	incombat = True
	while(incombat == True):
		if (character.health <= 0):
			print('You have died')
			print('Game Over')
			return 19
		elif userInput.lower() == 'attack':
			print('You swing at the goblin with your', character.rightarm, 'dealing', character.power - goblin.defense, 'damage.')
			goblin.health -= (character.power - goblin.defense)
			
			if(goblin.health <= 0):
				print('You have defeated goblin')
				character.flag5 = True
				print('You find', goblin.inventory, 'on the body.')
				character.healing_potion += 1
				print("Entering Dungeon")	
				reset_enemies()
				incombat = False
				return 8
			elif(goblin.health > 0):
				print('The goblin attacks you dealing', goblin.power - character.defense, 'damage.')
				character.health -= (goblin.power - character.defense)
				return 103
			elif(character.health <= 0):
				print('You have died')
				print('Game Over')
				return 19
			else:
				return 103
		elif userInput.lower() == 'run':
			print('You manage to escape.')
			print("Returning to area 7")	
			incombat = False
			return 7
		else:
			return 103


def dungeonOne_roomOne(userInput):
	
	if userInput.lower() == 'help':
		for element in character.help:
			print(element)
		return 8
	elif userInput.lower() == 'use healing potion' and character.healing_potion >= 1:
		character.healing_potion += -1
		print('You injested your healing potion.')
		print('Instantly restored 20 health.')
		character.health += 10
		if character.health > 100:
			character.health = 100
		return 8		
	elif userInput.lower() == 'status':
		print("You are currently wielding", character.leftarm, character.rightarm, "and you have", character.health, "health", character.power, "power", character.defense, "defense", character.gold, "gold", character.healing_potion, 'healing potions')
		return 8
	elif userInput.lower() == 'search':
		print('You did not find anything')
		return 8
	elif userInput.lower() == 'look':
		print('You did not see anything')
		return 8
	elif userInput.lower() == 'inventory':
		print(character.inventory)
		return 8
	elif userInput.lower() == 'move north':
			print("As you enter the next room of the dungeon the entrance crumbles behind you.")
			print("The ground below you shakes and a deafening roar can be heard.")
			print("The Rocktopus emerges from below!")
			print('You are now in combat with Rocktopus')
			return 104
	else:
		print("invalid input")
		return 8

def combat_dungeon_rocktopus (userInput):
	incombat = True
	while(incombat == True):
		if (character.health <= 0):
			print('You have died')
			print('Game Over')
			return 19
		elif userInput.lower() == 'attack':
			print('You swing at the Rocktopus ', character.rightarm, 'dealing', character.power - rocktopus.defense, 'damage.')
			rocktopus.health -= (character.power - rocktopus.defense)
			
			if(rocktopus.health <= 0):
				print('You have defeated the Rocktopus!')
				
				print('The Rocktopus flails around and drops the trinity.')
				print('You find', rocktopus.inventory, 'on the body.')
				character.leftarm = rocktopus.inventory
				character.defense = 3
				print("The Rocktopus corpse evaporates into a portal")	
				reset_enemies()
				incombat = False
				character.rightarm = 'Trinity Sword'
				character.power = 20
				print('Rockropus dies and the hero builds the trinity sword')
				print('A portal to Casttle Dittrich Opens')
				print('The hero walks through...')
				return 9
			elif(rocktopus.health > 0):
				print('The Rocktopus attacks you dealing', rocktopus.power - character.defense, 'damage.')
				character.health -= (rocktopus.power - character.defense)
				return 104
			elif(character.health <= 0):
				print('You have died')
				print('Game Over')
				return 19
			else:
				return 104
		elif userInput.lower() == 'run':
			print('The exit is blocked')
			return 104
		else:
			return 104

def staircase (userInput):
	if userInput.lower() == "move north":
		print("The hero climbs the Stairway to Dittrich's greedy Right Hand, Jim")
		print('You are now in Battle with Jim.')
		return 105
	elif userInput.lower() == 'look':
		print('You see a mighty staircase, stories high. Leading to the mighty Jim')
		return 9
	elif userInput.lower() == 'search':
		print('You only find traces of previous victims.')
		return 9
	elif userInput.lower() == 'help':
		for element in character.help:
			print(element)
		return 9
	elif userInput.lower() == 'use healing potion' and character.healing_potion >= 1:
		character.healing_potion += -1
		character.health += 10
		print('You injested your healing potion.')
		print('Instantly restored 20 health.')
		if character.health > 100:
			character.health = 100
		return 9
	elif userInput.lower() == 'status':
		print("You are currently wielding", character.leftarm, character.rightarm, "and you have", character.health, "health", character.power, "power", character.defense, "defense", character.gold, "gold", character.healing_potion, 'healing potions')
		return 9
	elif userInput.lower() == 'inventory':
		print(character.inventory)
		return 9
	elif character.gold == 1 and userInput.lower() == 'use':
		print('You attempt to bribe Jim with your remaining 1 gold piece.')
		print('Being as greedy as Jim is, and since Dittirch is stingy with his pay, Jim accepts with no hesitation.')
		return 10
	else:
		print('invalid input')
		return 9

def combat_staircase_jim(userInput):
	incombat = True
	if character.gold == 1 and userInput.lower() == 'use':
		print('You attempt to bribe Jim with your remaining 1 gold piece.')
		print('Being as greedy as Jim is, and since Dittirch is stingy with his pay, Jim accepts with no hesitation.')
		return 10

	while(incombat == True):
		if (character.health <= 0):
			print('You have died')
			print('Game Over')
			return 19
		elif userInput.lower() == 'attack':
			print('You swing at Jim with your', character.rightarm, 'dealing', character.power - jim.defense, 'damage.')
			jim.health -= (character.power - jim.defense)
			
			if(jim.health <= 0):
				print('You have defeated Jim')
				print('Jim is engulfed in flame and burns away')
				print('You find', jim.inventory, 'on the body.')
				print("You hear a maniacal laughter. Followed by 'WHO LIES IN GRANTS TOMB?!?!'")
				character.inventory += jim.inventory
				reset_enemies()
				#incombat = False
				return 10
			elif(jim.health > 0):
				print('Jim attacks you dealing', jim.power - character.defense, 'damage.')
				character.health -= (jim.power - character.defense)
				return 105
			elif(character.health <= 0):
				print('You have died')
				print('Game Over')
				return 19
			else:
				return 105
		elif userInput.lower() == 'run':
			print('Jim has blocked your escape!')
		else:
			return 105

def final(userInput):

	if userInput.lower() == "move north":
		print("There are three holes, I'm not in the first or third. Where am I?")
		print('You are now in battle with Dittrich')
		return 106
	elif userInput.lower() == 'help':
		print('Really....? No')
		return 10
	elif userInput.lower() == 'search':
		print('You only find very old references older students understand.')
		return 10
	elif userInput.lower() == 'look':
		print("You fail to take your eyes off of Dittrich's chalk board.")
		return 10
	elif userInput.lower() == 'status':
		print("You are currently wielding", character.leftarm, character.rightarm, "and you have", character.health, "health", character.power, "power", character.defense, "defense", character.gold, "gold", character.healing_potion, 'healing potions')
		return 10
	elif userInput.lower() == 'use healing potion' and character.healing_potion >= 1:
		character.healing_potion += -1
		character.health += 10
		print('You injested your healing potion.')
		print('Instantly restored 20 health.')
		if character.health > 100:
			character.health = 100
		return 10
	else:
	 	print("invalid input")
	 	return 10
	pass

def final_combat(userInput):
	incombat = True
	while(incombat == True):
		if (character.health <= 0):
			print('You have died')
			print('Game Over')
			return 19
		elif userInput.lower() == 'attack':
			print('You swing at Dittrich with your', character.rightarm, 'dealing', character.power - dittrich.defense, 'damage.')
			dittrich.health -= (character.power - jim.defense)
			
			if(dittrich.health <= 0):
				print("Dittrich is defeated?????")
				print('You find', dittrich.inventory, 'on the body.')

				character.inventory += dittrich.inventory
				reset_enemies()
				#incombat = False
				print("Game Over")
				break
			elif(character.health <= 0):
				print('You have died')
				print('Game Over')
				return 19
			elif(dittrich.health > 0):
				print('Dittrich attacks you dealing', dittrich.power - character.defense, 'damage.')
				character.health -= (dittrich.power - character.defense)
				return 106
	
			else:
				return 106
		elif userInput.lower() == 'run':
			print("You can't leave now!")
		else:
			return 106


def graveyard(userInput):
	print('you are dead')
	continueGame = False

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
	8: dungeonOne_roomOne,
	9: staircase,
	10: final,
	19: graveyard,
	100: combat_areaTwo_spider,
	101: combat_areaOne_mirror,
	102: combat_areaFive_orc,
	103: combat_areaSeven_goblin,
	104: combat_dungeon_rocktopus,
	105: combat_staircase_jim,
	106: final_combat
}
def gameLoop():
	continueGame = True
	currentState = 1
	while continueGame:
		newInput = input('What would you like to do next? ')
		currentState = dictionaryOfAreas[currentState](newInput)

gameLoop() 
