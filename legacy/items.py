# Items
# A module for Python Adventure Game containing classes for items (version 2.3.3)
#
# No luck with it so far. Lots of the classes are redundant, and the strings worked so well.
# But I need a new class for foods eventually, and stuff that will change if you leave it. Seeds will be in that class,
# and it opens up a lot of possibilities.
#
# Okay, it just seems like super() isn't working correctly. I'll just have to put all the attributes in class Item()
# and just include functions such as dynamic() and attack() in the new classes, leaving __init__() unchanged.
# Pretty confusing, huh? I'll probably just rewrite the whole think except for the bottom few lines, which would only
# require refitting and are still quite useful. I just need all the attributes in one place, it seems.


import words, constants
import copy, random

class Item(object):
	'''A simple item that you can put in your inventory.
	Functions: get_hurt(), die().
	Cannot be harmful or special. Classes (fuel, weapon, food) have more attributes.'''
	def __init__(self,						name,
				 plural = False,			tool = False,			takeable = True,			burn_chance = 0,
				 weapon = False,			mobile = False,			edible = False,				deadible = False,
				 flammable = False,			burnable = False,		firestarter = False,		armor = False,
				 wounded = False,			alive = False,			dangerous = False,			hostile = False,
				 good_food = False,			gross_food = False,		fryable = False,			food = 0):
				 #FIXME: NOTE: I need to add all the things like "digger/is_digger", "cutter/is_cutter", and so on...)
		self.name = name
		self.is_plural = plural				# not used just yet
		self.is_tool = False
		self.is_takeable = takeable			# whether you can pick it up off the ground (not fire, for instance)
		self.is_edible = edible				# whether it is edible "as is"
		self.is_deadible = deadible			# whether it is edible after it dies
		self.is_hostile = False
		self.is_dangerous = False
		self.is_weapon = False
		self.is_mobile = mobile				# whether it can move of its own free will
		self.is_flammable = flammable
		self.is_burnable = burnable
		self.is_firestarter = firestarter
		self.is_armor = armor				# whether it counts as a piece of armor--e.g., bulletproof vest
		self.is_wounded = False
		self.is_alive = alive
		self.is_dangerous = False
		self.is_hostile = False
		self.is_good = good_food			# Can be one or the other. If it is set to either of these, it will become
		self.is_gross = gross_food			# edible upon dying.
		self.is_fryable = fryable			# If True, you can fry it once it's in your inventory, making it edible
		self.food = int(food)				# how much hunger it subtracts
		self.is_tool = False
		self.is_weapon = False
		self.type = "item"
		
		
	def __str__(self):
		return self.name
	
	def fry(self):
		'''Prepare the food'''
		if self.is_fryable:
			self.is_edible = True
			if self.is_wounded:
				self.name = self.name[8:]
			elif self.is_alive:
				self.name = self.name[5:]	
			self.food += constants.FRIED_FOOD_BONUS
			self.name = "fried " + self.name
			self.is_fryable = False				# You can't refry it
			# Just in case it's not specified (should never happen):
			if not is_gross and not is_good:
				good = random.randrange(2)
				# Randomly makes it good or bad, if not specified
				if good:
					self.is_good = True
				else:
					self.is_gross = True
	
	
	def get_hurt(self):
		if not self.is_wounded and not self.is_alive:
			self.is_wounded = True
			self.name = "wounded " + self.name
				
	def die(self):
		if self.is_alive:
			self.dead = True
			self.is_alive = not self.is_alive
			if self.is_wounded:
				self.name = self.name[8:]
			self.name = "dead " + self.name
		self.is_mobile = False
		self.is_hostile = False
		self.is_dangerous = False
		self.is_takeable = True
		if self.is_deadible:
			self.is_edible = True
		self.type = "item"
		
class Tree(Item):
	def __init__(self,						burn_chance = 8,
				 name = "tree",				plural = False,			tool = False,				takeable = False,
				 weapon = False,			mobile = False,			edible = False,				deadible = False,
				 flammable = False,			burnable = True,		firestarter = False,		armor = False,
				 wounded = False,			alive = False,			dangerous = False,			hostile = False,
				 good_food = False,			gross_food = False,		fryable = False):#,			burn_chance = 8):
		super(Item, self).__init__()
		self.name = name
		self.is_burnable = burnable
		self.takeable = False
		self.is_wounded = False
		self.is_alive = False
		self.is_dangerous = False
		self.is_hostile = False
		self.is_fryable = False
		self.is_takeable = takeable
		self.burn_chance = burn_chance
		self.type = "tree"
		
	def die(self):
		'''Turn into a log'''
		self.burnable = True
		self.name = "log"
		self.takeable = True
		

class Hostile_Animal(Item):
	'''A simple, hostile animal.'''
	def __init__(self,		name,			hostility,				food,						venemous,
				 plural = False,			takeable = True,		weapon = False,				mobile = False,
				 edible = False,			deadible = False,		heal_chance = 0,			death_chance = 150,
				 flammable = False,			burnable = False,		firestarter = False,		armor = False,
				 wounded = False,			alive = True,			dangerous = False,			hostile = True,
				 good_food = False,			gross_food = False,		fryable = False,			infected = False):
		#super(Item, self).__init__(name,	plural,		tool,	takeable,	edible,		deadible,	hostile,
		#						   hostile,	dangerous,	weapon,	mobile,		flammable,	burnable,	armor)
		super(Item, self).__init__()	#FIXME: it says it takes no parameters but I know that it does
		#NOTE: FIXME: This is not supposed to all be here, this is just for debugging purposes!!
		self.name = name
		self.hostility = hostility
		self.is_plural = plural				# not used just yet
		self.is_edible = edible
		self.is_tool = False
		self.is_flammable = flammable
		self.is_burnable = burnable
		self.is_firestarter = False
		self.is_armor = armor				# whether it counts as a piece of armor--e.g., bulletproof vest
		self.is_wounded = False
		self.is_alive = alive
		self.is_dangerous = False
		self.is_hostile = True				#FIXME: is there a case where it could be non-hostile?
		self.is_good = good_food			# Can be one or the other. If it is set to either of these, it will become
		self.is_gross = gross_food			# edible upon dying.
		self.is_fryable = fryable			# If True, you can fry it once it's in your inventory, making it edible
		self.food = int(food)				# how much hunger it subtracts
		
		
		self.is_tool = False
		self.is_weapon = False
		self.takeable = True
		self.is_armor = False
		self.is_hostile = True
		self.is_wounded = wounded
		self.is_alive = False			# to start , it must be a simple Item
		self.is_firestarter = False		# only tools can be, unless it's set on fire...
		self.hostility = hostility		# one in how many chances of acting ferociously
		self.is_venemous = venemous		# whether a bite injects venom
		self.is_infected = infected		# whether a bite introduces disease
		self.type = "hostile animal"
	
	
	
	def heal(self):
		'''Get better if hurt'''
		if self.is_wounded:
			if self.heal_chance:
				shall_heal = random.randrange(heal_chance)
				if not shall_heal:
					self.wounded = False
					self.name = self.name[8:]		# cut off "wounded" from name


class Dangerous_Animal(Hostile_Animal):
	'''A more complex animal that will attack you.'''
	def __init__(self,
				 name = "dragon",			plural = False,			takeable = False,			
				 weapon = False,			mobile = False,			heal_chance = 5,			death_chance = 4,
				 wounded = False,			alive = True,			dangerous = True,			hostile = False,
				 good_food = False,			gross_food = False,		fryable = False,			deadible = False,
				 hostility = 1,				venemous = False,		infected = False,			food = 30,
				 min_damage = 0,			max_damage = 20):
		super(Hostile_Animal, self).__init__(name, plural, takeable, hostility, alive)
		self.is_dangerous = True
		self.hostility = hostility
		self.min_damage = min_damage				# minimum damage it can inflict in one attack
		self.max_damage = max_damage - min_damage	# the range for the damage it can cause
		self.type = "dangerous animal"
		self.is_takeable = False
		self.is_alive = True
		
	def attack(self, player):
		'''Says that it attacks the player, then, if its damage is greater than zero,
		actually does it. '''
		print self.name.capitalize(), "has attacked!"
		damage = random.randrange(self.max_damage) + self.min_damage
		if damage and not self.is_wounded:
			#print "The", self, "has attacked you, causing",
			protection = 0
			for piece in player.inventory:
				armor = []
				if piece.is_armor:
					protection += constants.DAMAGE_REDUCTION_FACTOR
					armor.append(piece)
			damage -= protection
			if damage < 0:
				new_damage = 0
			if damage:
				player.health -= damage
			else:
				print "Your ",
				words.list(armor)
				print "have kept you from all harm."
			#print damage, "damage!"
			if player.health:
				print "You must now fight the", str(self) + '.'
				player.fight(self)
			else:
				print "The", self, "has killed you."
				player.die()
		else:
			print "You luckily escaped unscathed."
		# for use in the fight report
		if damage:
			return int(damage)
		else:
			return damage == 0
		
		
				
class Tool(Item):
	'''A tool'''
	def __init__(self,
				 name = "tool",				plural = False,			tool = True,			takeable = True,
				 weapon = True,				remaining_txt = "uses",	uses = -1,
				 flammable = False,			burnable = False,		firestarter = False,	armor = False,
				 digger = False,			cutter = False,			fryer = False, 			bright = False):
		super(Item, self).__init__()
		self.is_tool = tool
		self.name = name
		self.uses = uses
		if weapon:
			# then it's a makeshift weapon
			self.is_weapon = True		
			self.uses = -1					# you can use it as often as you like
			self.damage_range = 0			# can't use for fighting--only self-defense
		self.is_digger = digger				# if you can dig with it (a shovel comes most prominently to mind)
		self.is_cutter = cutter				# if it can be used to cut things (trees, wood, etc.)
		self.fryer = fryer					# if it's a frying pan (like you can't tell)
		self.is_bright = bright				# if it's a light of some sort (flashlight, usually)
		self.is_firestarter = firestarter	# if you can use it to start a fire (such as a lit torch)
		self.is_flammable = flammable		# if you can set it on fire (like a candle or your clothing)
		self.is_armor = armor				# if possessing it can help protect you
		
		self.is_fryable = False
		self.good_food = False
		self.gross_food = False
		self.is_dangerous = False
		self.is_hostile = False
		self.is_wounded = False
		self.is_takeable = True
		self.is_alive = False
		self.type = "tool"
				
	def can_use(self):
		'''Handle usage'''
		if self.uses != 0:
			self.uses -= 1
			return True
		else:
			return False

			
class Weapon(Tool):
	'''A weapon you can use to fight.'''
	def __init__(self,
				 name = "knife",			plural = False,			tool = False,
				 takeable = True,			heal_chance = 0,		remaining_txt = "uses",
				 flammable = False,			burnable = False,		firestarter = False,		armor = False,
				 digger = False,			cutter = False,			fryer = False,				bright = False,
				 blade = True, 				long = False,			gun = False,	uses = -1,	damage_range = 15):
		super(Tool, self).__init__(name, cutter, flammable, armor, bright)
		self.name = name
		self.is_weapon = True					# duh
		self.is_tool = tool
		self.type = "weapon"					# duh
		self.is_armor = armor					# if it can be used for protection, like, say, a sword
		self.is_bright = bright					# whether if it gives light
		self.is_cutter = cutter					# if it can be used to chop things (an axe comes to mind)
		self.is_blade = blade					# is a bladed weapon (knife, sword, axe)
		self.is_long = long						# is a long weapon (gun with bayonet, sword, spear, axe)
		self.is_gun = gun						# is a gun (machine gun, rifle, pistol, shotgun, etc.)
		self.uses = uses						# number of uses; represents ammunition, etc. Set to -1 for infinite.
		self.damage_range = damage_range		# amount of damage it can conceivably cause
		#self.is_tool = tool						# if it's also a tool, like a knife or an axe
		# if it's not a blade, a long weapon, or a gun, it is a "makeshift" weapon.
		
		if self.uses > 0:
			self.remaining_txt = "ammunition"
		else:
			self.remaining_txt = remaining_txt


		
# Commonly used objects
# Note: there can only be one, and I can't use an object as a class. I *could* have a class for each individual
# object, but...
map = Item(name = "map")
shovel = Tool(name = "shovel", digger = True)
clothing = Item(name = "clothing", flammable = True)
flashlight = Tool(name = "flashlight", bright = True)
candle = Tool(name = "candle", flammable = True)
earthworms = Item(name = "earthworms", plural = True, edible = True, gross_food = True, fryable = True)
rabbit = Item(name = "rabbit", alive = True, edible = False, gross_food = True, fryable = True)
frog = Item(name = "frog", edible = True, gross_food = True, fryable = True)
snake = Hostile_Animal(name = "snake",		venemous = True,	hostility = 1,	deadible = True,
					   gross_food = True,	food = 4,			fryable = True)
seeds = Item(name = "seeds", edible = True)
pine_tree = Tree(name = "pine tree")
frying_pan = Tool(name = "frying pan", weapon = True, fryer = True)
knife = Weapon(name = "knife", blade = True)
penny = Item(name = "penny")
water = Item(name = "water", takeable = False)
axe = Weapon(name = "axe", long = True, cutter = True, tool = True, blade = True, damage_range = 22)


# Transferred from 'constants'
class Boss(Item):
	'''A bad guy you can (optionally) defeat to win.'''
	def __init__(self, name = "Your boss",					# whatever the boss is called
				 location = None,							# where he starts
				 health = 50,								# higher is more difficult
				 defense = 0,								# how much damage he won't take
				 weapon = copy.copy(knife),					# a weapon from his inventory	# what he wears (if defined)
				 inventory = [copy.copy(knife), copy.copy(clothing)],
				 attack_factor = 2,							# set to 1 to disable
				 stationary = True,							# whether it can move
				 speed = 1,									# how fast it can move--must be < 5
				 min_power = 5,								# minimum damage he can cause
				 max_power = 20,							# maximum additional damage he can cause
				 death_causes_victory = True):
		super(Item, self).__init__()
		self.name = name
		self.location = location
		self.health = health
		self.defense = defense
		self.weapon = weapon
		self.inventory = inventory
		self.attack_factor = attack_factor
		self.stationary = stationary						# becomes False upon finding it
		self.speed = speed
		self.min_power = min_power
		self.max_power = max_power
		self.victory = death_causes_victory					# if True, causes player to win
		self.type = "boss"
		self.is_wounded = False
		
	def __str__(self):
		'''Prints the boss's name'''
		return self.name
		
	def attack(self, player):
		'''Fight the innocent player'''
		attack_chance = random.randrange(self.attack_factor)
		print self, "has attacked you!"
		if attack_chance:
			damage = random.randrange(self.max_power) + self.min_power
			for piece in ARMOR:
				if piece in player.inventory:
					damage -= 2
			player.health -= damage
			print "You have suffered a loss of", damage, "percent of your total health!!"
			if player.health <= 0:
				print self, "has killed you."
				player.die()
			else:
				print "Fight!"
				player.combat(self)
		
	def defend(self, damage):
		'''Defend against the player's attacks.'''
		damage -= self.defense
		if damage < 0:
			damage = 0
		self.health -= damage
		int(self.health)
		#FIXME: this sounds downright dumb with most boss names.
		print self, "is down to", self.health, "percent."
		return self.health
	
	def move(self):
		'''Go to another location, if mobile'''
		if not self.stationary:
			for i in range(self.speed):
				destination = random.choice(self.location.adj)
				self.location = destination
	
	def die(self, player):
		'''Since he's already cleaned up in the player's private __kill() method,
		all we need to do is pronounce him dead, and return the victory attribute.'''
		#self.location.remove(self)
		print "He's dead,", player.name + '.'
		return self.victory