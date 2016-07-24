# Simple Adventure Game
# Version 2.3.3
#
# A simple adventure game using object-oriented programming. The player can travel
# between various connected locations. This is the last Chapter 9 project.

import time, cPickle, random, commands, copy
import words, query, items, constants, interface


# A map that is independent of any object
MAP = interface.MAP



class Adventurer(object):
	'''The user of this program.'''
	def __init__(self,
				 inventory = ["shovel", "clothing", "flashlight"],
				 health = 100,
				 grossed_out = 0,
				 hunger = 0,
				 hungry = False,
				 location = None,
				 bitten = False,
				 diseased = False,
				 has_map = False):
		'''Sets up the default player values'''
		
		self.inventory = inventory
		self.health = int(health)
		self.grossed_out = grossed_out
		self.hunger = hunger
		self.hnc = 0
		self.hungry = False
		self.location = location
		self.is_alive = True
		self.bitten = bitten
		self.diseased = diseased
		self.wounded = []
		self.moved = False
		self.matches = 5
		self.light = True
		self.won = False
		self.skills = 1.0
		
		# Establish a maximum number of things the player can hold.
		# Someday, I will allow the usage of bags, backpacks, or boxes, but for now, it is constant.
		self.MAX_ITEMS = 9
		
		# Establish a combat damage number
		self.COMBAT_DAMAGE = constants.COMBAT_DAMAGE_FACTOR * self.skills
		self.attributes = ()
		
	def __str__(self):
		rep = self.name
		rep += "'s Status Report:\n"
		rep += "You are " + str(self.health) + "% healthy.\n"
		if self.hungry:
			rep += "You are hungry.\n"
		rep += "You have "
		for tool in self.inventory:
			rep += '\n*' + tool.name
			if tool.type == tool:		# if it's a tool
				if tool.uses > 0:		# with uses left,
					# say how many uses are remaining
					rep += '\t\t[' + tool.remaining_txt + ': ' + str(tool.uses) + ']'
		if not self.inventory:
			rep += "absolutely nothing..."
		rep += "\n...and you're at " + self.location.name + '.'
		return rep
	
	
	def pick_up(self, item):
		'''Take an item that you see lying aroun'.'''
		
		'''if len(self.inventory) >= self.MAX_ITEMS:
			print "Unfortunately, you cannot add", item, "to your inventory, because you can \
only hold", self.MAX_ITEMS, "things."
			print "Try discarding something."
		elif item in constants.UNTAKEABLES:
			print "You cannot take", words.aN(item) + '.'
		elif item == game.boss:
			print "In your attempt to pick up", game.boss + ", you have angered him!"
			game.boss.attack(self)
		elif "tree" in item:
			if "herring" in self.inventory and "axe" not in self.inventory:
				print "Cut down a tree with a herring? It can't be done!"
			elif "axe" not in self.inventory:
				print "You need an axe to cut down trees."
			else:
				print "You have cut down the", item + '.'
				self.location.stuff.remove(item)
				self.location.stuff.append("log")
				self.__update()
		else:
			self.inventory.append(item)
			self.location.stuff.remove(item)
			self.__update()'''
			
		if item.is_takeable:
			self.inventory.append(item)
			self.location.stuff.remove(item)
			self.__update()
	
	def leave(self):
		'''Leave some of your stuff behind.'''
		#FIXME: make it so that you don't leave multiple items behind
		print "What do you leave behind?"
		words.list_items(self.inventory)
		item_name = raw_input("Select an item: ")
		had_thing = False
		for item in self.inventory:
			if item.name == item_name:
				had_thing = True
				self.inventory.remove(item)
				self.location.stuff.append(item)
				print "You leave your", item, "behind."
				self.__update()
		if not had_thing:
			print 'You do not have "' + item_name + '".'
	
	def check_map(self):
		'''Take a look at the map.'''
		if items.map in self.inventory:
			self.map = MAP[:]								 		# make a copy of the map
			if self.location.num in self.map:
				self.map = self.map.replace(self.location.num, '@')	# shows where you are
				for char in self.map:
					for place in game.locations:
						if char == place.num:
							self.map = self.map.replace(char, 'X')	# shows where you can go
				print self.map										# then displays the edited map
		else:
			print "You have no map."
			
	def move(self):
		'''Moves the player to a new location.'''
		location = self.location# old location
		count = 0				# organize by columns
		print "You can access:",
		for loc in self.location.adjacent:
			print str(loc) + ';',
			count += 1
			if count == 4:
				print '\n',
		place = raw_input("You go to: ")
		for area in self.location.adj:
			if area.ref.lower() in place.lower() and area in self.location.adj:
				if area.required:
					can_move, explanation = area.check_permit(self)
				else:
					can_move = True
				if not area.required or can_move:
					self.location = area
				else:
					print explanation

		if location != self.location:   # if you've moved
			self.moved = True
			self.__update()
		else:
			#print "You canna do that."
			print place.upper(), "is not an accessible location."
		
	def dig(self):
		'''Dig up a buried or partially-buried item.'''
		dug = True
		junk = self.location.buried
		chastise = "You have dug for hours fruitlessly."
		if self.location.is_dark and not self.light:
			print "It is effectively too dark to dig."
			print "Hint: See if you can find a flashlight."
			dug = False
		elif junk:
			junkpieces = []
			for piece in junk:
				#if len(piece) != 1:
				junkpieces.append(piece)
				#elif not len(piece):
				#	print chastise
			if junkpieces:
				void = None
				for peice in junkpieces:
					if not peice:
						void = True
				if not void:
					print "You have dug up",
					for piece in junkpieces:
						if piece:
							print piece.name + ',',
							self.location.stuff.append(piece)
						else:
							print chastise
					print '\n'
				else:
					print chastise
			else:
				if junk:
					print "You have dug up", junk.name + '.'
					self.location.stuff.append(junk)
					print '\n'
			self.location.buried = []
		#elif "shovel" not in self.inventory:
		#	print "You have nothing which you can use to dig."
		#	dug = False
		else:
			print chastise
				
		if dug:
			self.hunger += 1
			self.__update()
	
	def bury(self):
		'''Put something back in the ground.'''
		# Dig buried stuff up while burying your own junk
		#self.location.buried:
		#	print "While digging a hole,",
		#	self.dig()
		has_shovel = False
		for item in self.inventory:
			if item.name == "shovel":
				shovel = item
				has_shovel = True
		if has_shovel:
			has_garbage = False
			words.list_items(self.inventory)
			garbage_name = raw_input("Choose an item to bury in the ground: ")
			for item in self.inventory:
				if item.name == garbage_name:
					garbage = item
					has_garbage = True
			#if garbage in self.inventory:
			if has_garbage:
				if garbage.name != "shovel":
					self.inventory.remove(garbage,)
					self.location.buried += (garbage,)
					print "There! It's buried."
					self.hunger += 1
					self.__update()
				else:
					print "You cannot bury your shovel."
			else:
				print "You do not have", garbage, "in your inventory."
		else:
			print "You need a shovel to bury things."
	
	def eat(self, food):
		'''Eat something gross.'''
		if food.is_gross:
			print "Blechh. That", food, "was awful."
			self.hunger -= food.food
			self.grossed_out += 1
		else:
			print "Yum."
			self.hunger -= food.food
		self.inventory.remove(food)
		if self.hunger < 0:
			self.hunger = 0
		self.__update()
		
	def fry(self):
		'''Prepare foods best not eaten raw.'''
		if "frying pan" in self.inventory and "fire" in self.location.stuff:
			eat = []
			for item in self.inventory:
				if item in (constants.FOODS or constants.PEACEFUL):
					eat += [item,]
			print eat
			food = raw_input("Select an item to fry: ")#FIXME:
			if (food.fryable) and (not food.fried) and (food in self.inventory) and (food.is_food):
				# copy the name over...
				name = food.name
				if "dead" in name:
					name = name[4:]
					name = "fried" + name
				else:
					name = "fried " + name
				# ...then restore it after editing
				food.name = name
				print "The food is ready to eat."
				self.__update()
			elif food in constants.UNFRYABLE:
				print "Don't bother trying to fry", food + '.'
			elif food in constants.FRIED_FOODS:
				print "No need to refry it."
			elif food not in constants.FOODS:
				food = words.aN(food)
				print food.capitalize(), "is not a food."
			else:
				print "You do not have" + '"' + food + '".'
		else:
			print "You need a frying pan and fire to fry foods."
			
	def build_fire(self, wood, source):
		'''Set fire to the map.
		FIXME: Let the fire burn out of control sometimes.'''
		if source.can_use():
			source.uses -= 1
			wood.name = "fire"
			wood.is_takeable = False
			wood.is_flammable = False
			wood.is_burnable = False
			wood.is_hostile = False
			wood.is_dangerous = False
			print "You have successfully started a fire. Watch it doesn't burn out of control."
			self.__update()
			
			# Preliminary setup for out-of-control fires
			for item in self.location.stuff:
				item.burn_chance = 0
				if "wood" in self.location.description:
					item.burn_chance += 2
				for item in self.location.stuff:
				  try:
					if "tree" in item.name:
						item.burn_chance += 2
					elif "water" == item.name:
						item.burn_chance = 0
					if item.burn_chance > constants.FIRE_SPREADING_CHANCE:
						item.burn_chance = constants.FIRE_SPREADING_CHANCE
				  except(AttributeError):
				   	print "Another error has occurred; the fire was about to spread, but there is no code"
				   	print "written yet to allow this. Please contact the developer."
		else:
			print "You have used that source up."
		
	def set_fire(self, source, candle):
		'''Set fire to a candle or something.
		Determines whether it's flammable, then calls __ignite().
		NOTE: This is broken and unused. Keep it that way.
		
		EDIT: Right now all this does is call a separate function!
		Rest assured, however, this is meant to do some other stuff before ignition; it won't be entirely useless.'''
		#if not candle.is_flammable or not candle.tool:
		#	print str(candle).capitalize(), "is not flammable."
		#else:										# if it can be burned
		self.ignite(source, candle)
					
					
	def ignite(self, source, candle):
		'''Public method for setting fire directly
		Was private, but this has been changed.'''
		if source.can_use():
			source.uses -= 1
			candle.is_flammable = False								# you can't set fire to something already burning
			candle.is_bright = True									# when it's on fire, it gives off heat and light
			candle.firestarter = True								# you can now use it to set more fires
			candle.uses = -1										# temporary, just so that you can use it for now...
			print "You have successfully set your", candle.name, "on fire."												# print this before renaming
			candle.name = "lit " + candle.name						# now it's a "lit candle"
			self.__update()											# update the player
		else:
			print "The", source, "has been used up."
		
		
	def extinguish(self):
		'''Put out a fire.'''	
		fire = None
		for item in self.location.stuff:
			if item.name == "fire":
				fire = item
		if fire:
			print "Gisssh."
			item.name = "ashes"
			self.burn_chance = False
			self.__update()
		else:
			print "There's no fire burning."
			
	def look(self, area):
		'''Take a look at the surrounding area.'''
		if not area.is_dark:
			print area
		elif area.is_dark and self.light:
			print "It is dark in", area.name.lower() + ',',
			if "flashlight" in self.inventory:
				print "so you turn on your flashlight."
			else:
				print "but you have a flame."
			raw_input("(Press 'Enter' to continue.) ")
			print self.location
		else:
			print "It is too dark to see your surroundings clearly."
			print "You can access the following locations:",
			for place in area.adjacent:
				if place.name != area.name:
					print place + ', ',
			print "and", area.name + '.'
	
	def cut_down(self, tree):
		'''Cut down a tree with a herring? It can't be done!'''
		if "tree" in tree.name and tree.is_burnable and not tree.is_takeable:
			print "You have cut down the", str(tree) + '.'
			tree.die()
			self.hunger += 1
			self.__update()
	
	def attack(self):
		'''Attack a hostile creature.
   		NOTE: This is very confusing right now. I want to rewrite the entire attack() "mechanism" based off each individual
		weapon and creature's traits.

		TODO: Consolidate attack(), fight(), and combat() into one function as not to confuse the user. I'll have to, of course,
	check what the user wants to attack and whether he can do so with his current inventory. Ultimately, I want something
	like this:
			Your action: attack
			rabbit, stone, bandit
			What do you want to attack? stone	|	rabbit			|	  bandit
			You cannot attack that.			|	You kill the rabbit.	|	<combat. . .>
			'''
		if not self.location.is_dark or self.light:
			has_valid_weapon = False
			words.list_items(self.inventory)
			weapon_name = raw_input("Choose a weapon: ").lower()
			#if weapon in constants.LONG_WEAPONS or weapon in constants.REAL_WEAPONS:
			for item in self.inventory:
				if item.name == weapon_name:
					has_valid_weapon = True
					weapon = item
				if has_valid_weapon and weapon in self.inventory:
					# see if there's a valid creature
					has_valid_target = False
					words.list_items(self.location.stuff)
					creature_name = raw_input("Choose a target: ").lower()
					for item in self.location.stuff:
						if item.name == creature_name:
							creature = item
							has_valid_target = True
					if has_valid_target:
						if creature.is_hostile:
							self.skills += 0.05
							self.__kill(creature)
							self.__update()
					#elif creature in constants.DANGEROUS and self.location.stuff:
					elif creature.dangerous:
						print "You must fight", words.aN(creature.name) + '.'
					else:
						print creature.name.capitalize(), "is not harmful."
				else:
					print "You do not have", words.aN(weapon.name) + '.'
			else:
					print weapon.name.capitalize(), "isn't a valid weapon."
		else:
			print "You cannot risk attacking in the dark."
	
	def fight(self, enemy):
		'''Fight a larger foe.
		FIXME: This is entirely broken!!!'''
		has_valid_weapon = False
		words.list_items(self.inventory)
		weapon_name = raw_input("Select a weapon: ").lower()
		for item in self.inventory:
			if item.name == weapon_name:
				if item.is_weapon:
					has_valid_weapon = True
					weapon = item
				else:
					print item.name.capitalize(), "is not a weapon."

		if has_valid_weapon:
			#if weapon in constants.GUNS:
			if weapon.type == "weapon":
				if weapon.is_gun:
					death = random.randrange(2)
					if not death:
						self.skills += 0.1
						self.__kill(enemy)
						self.__update()
					else:
						wounded = random.randrange(3)
						if wounded:
							self.location.stuff.remove(enemy)
							print "You have badly injured the", enemy + '.'
							enemy = "wounded " + enemy
							self.location.stuff.append(enemy)
							self.wounded.append(enemy)
							self.__update()
						else:
							print "Your shot has missed!"
							self.__update()
				elif weapon.is_blade:
					death = random.randrange(6)
					if not death:
						self.skills += 0.15
						self.__kill(enemy)
						self.__update()
					else:
						wounded = random.randrange(3)
						if wounded:
							print "You have injured the", enemy.name + '.'
							enemy.name = "wounded " + enemy.name
							self.wounded.append(enemy)
							self.__update()
				# Help! This doesn't go here
				else:
					print "Your attack has failed!"
					self.__update()
			'''elif enemy.is_hostile:
				print "Simply attack the", enemy + '.'
			elif enemy in constants.PEACEFUL:
			elif not enemy.is_hostile:
				print words.aN(enemy.name).capitalize(), "won't hurt you."
			elif enemy not in constants.ANIMALS:
			elif not enemy.is_animal:
				print words.aN(enemy.name).capitalize(), "isn't an animal."
			elif enemy not in self.location.stuff:
				print "Error: " + '"' + enemy.name + '"' "ain't here."
			else:
				print "This is for debugging purposes."'''
		elif ("cancel" or "no" or "forget" or "never") in weapon_name.lower():
			# "never mind" or "cancel"; means the user wants to forget about it
			print "Canceled."			
		else:
			print words.aN(weapon_name).capitalize(), "is not sufficient for this fight."
		
	def combat(self, boss):
		'''Fight a boss to win the game, or at least rid the game of it.'''
		valid = []
		for item in self.inventory:
			if item.is_weapon:
				valid.append(item)
				print item,
		weapon = raw_input("\nChoose a weapon: ").lower()
		while weapon not in valid and weapon not in "no never stop it":
			weapon = raw_input("\nChoose a weapon: ").lower()
		if boss in self.location.stuff:
			if weapon.is_gun:
				if random.randrange(5 - boss.speed):
					print "You quickly fire your", weapon + '.'
					boss.die()
				else:
					print "...a MISS?!?"
				self.__update()
			#elif weapon in constants.BLADED_WEAPONS and constants.LONG_WEAPONS:
			elif weapon.is_blade and weapon.is_long:
				damage = random.randrange(int(self.COMBAT_DAMAGE))
				print "You forcefully attack with a strength of", str(damage) + "..."
				result = boss.defend(damage)
				self.skills += damage / 100
				if result <= 0:
					self.skills += 1.0
					self.__kill(boss)
					victory = boss.die(self)
					game.boss = None
					if victory:
						self.won = True
						self.__update()
				else:
					retreat = query.ask_yes_or_no("Run away? ")
					if retreat:
						self.move()
					else:
						boss.attack(self)
						self.__update()
						self.combat(boss)
		elif weapon not in self.inventory:
			print "You don't have that weapon."
		elif not weapon.is_weapon:
			print "That", weapon, "will not do for this fight."
		else:
			print "There is nothing to combat."
			
		
	def trade(self, market):
		'''Trade with the location.'''
		if "market" in market.name:
			type = raw_input("Buy or sell? ").lower()
			if "buy" in type:
				for good in market.sale:
					print '*' + good.name
				purchase_name = raw_input("Choose a good to buy: ").lower()
				unavailable = True
				for item in market.sale:
					if purchase_name == item.name:
						unavailable = False
						purchase = item
						
						# then pay for the good
						words.list_items(self.inventory)
						money_name = raw_input("Choose a (valid) piece of money: ").lower()
						has_money = False
						for item in self.inventory:
							if money_name == item.name:
								has_money = True
								money = item
								self.location.accept_trade(self, money, purchase)
								self.__update()
						if not has_money:
							print "You don't have", words.aN(money_name) + '.'
				if unavailable:
					print "They don't have that for sale."
			elif "sell" in type:
				words.list_items(self.inventory)
				item_name = raw_input("Select an item to sell: ").lower()
				has_item = False
				for item in self.inventory:
					if item.name == item_name:
						has_item = True
						itm = item
						market.accept_offer(self, itm)
						break
				if not has_item:
					print "You don't have", item_name + '.'
				self.__update()
			else:
				print "Canceled."
		else:
			print "This isn't a flea market--what do you think you're doing?"
			
	def wait(self):
		'''Skip a turn'''
		print "You wait around for a while."
		self.__update()
		
				
	def __kill(self, creature):
		'''Get rid of a harmful animal.
		Note: This is getting confusing. I'm not sure why this method even exists at this point,
		since creatures can die publicly anyways...'''
		print "You have killed the", creature
		creature.die()

		# some obsolete code to be deleted if this method works without it
		'''try:
		if "wounded" in creature.name:
			# remove 'wounded' before adding 'dead' to name
			creature.name = creature[8:]
		except(TypeError):
			print "Uh-oh. An unknown bug has occurred in private method __kill()."
			if "wounded" in creature.name:
				creature.name = creature.name[8:]
		creature.name = str("dead " + creature.name)
		self.location.stuff.append(creature)'''
			
	def __update(self):
		'''Mostly for future development. Checks for death and such.
		Eventually, add autosave capability ("/tmp/autosave.adv")
		
		I am now converting this over to use the new objects. I will put
		a marker where I have left off each time, just in case I forget.'''
		# Make the game do its thing
		game.do_thing()
		# Check for venemous creatures
		'''for creature in constants.VENEMOUS:
			if creature in self.inventory:
				if creature == "bug":
					damage = random.randrange(10)
				elif creature == "monkey":
					damage = random.randrange(50)
				else:
					damage = random.randrange(100)
				print "\nThe", creature, "you picked up has bitten you!"
				self.health -= damage
				self.bitten = True
				print "You have lost", damage, "percent of your health from the bite."'''
		for creature in self.inventory:
			if creature.is_hostile:
				if not random.randrange(creature.hostility):	# one in however-many chances
					print "\nThe", creature, "you picked up has bitten you!"
					damage = random.randrange(constants.HOSTILE_CREATURE_DAMAGE * 2)
					if creature.venemous:
						self.bitten = True
					if creature.infected:
						self.infected = True
					self.health -= damage
					print "You have lost", damage, "percent of your health from the bite."
		# Check for creature bite
		if self.bitten:
			worse = random.randrange(2)
			if worse:
				print "Your bite has gotten worse."
				damage = random.randrange(constants.HOSTILE_CREATURE_DAMAGE)
				self.health -= damage
				print "Your health is now only", str(self.health) + '%.'
		# Check for injured creatures
		for location in game.locations:
			for creature in location.stuff:
  			  if creature.type == "hostile animal" or "dangerous animal":
				if creature.is_wounded:
					worse = random.randrange(creature.death_chance)
					better = random.randrange(creature.heal_chance)
					if not worse:
						if creature in self.location.stuff:
							print "That", creature, "just died."
						# this comes after so it doesn't say "that dead creature just died"
						creature.die() 
					elif not better:
						# this comes before so it doesn't say "that wounded creature is on the move"
						creature.heal()
						if creature in self.location.stuff:
							print "Look out! That", creature, "is on the move again!"
		# Check for dangerous creatures
		for creature in self.location.stuff:
			if creature.is_dangerous and creature.is_alive and not self.moved:
				attack_chance = random.randrange(creature.hostility)
				if not attack_chance:
					dmg = creature.attack(self)
					if dmg:
						print "You have been injured, costing", dmg, "percent of your health."
					if self.health > 0 and creature.is_alive:
						print "You must now fight the creature."
						self.fight(creature)
					elif self.health > 0 and not creature.is_alive:
						print "But at least you killed the", creature.name + '!'
				else:
					print "Watch out for that", creature + '!'
		# Check for "bosses"
		if game.boss:
			if game.boss.location == self.location and not self.moved:
				game.boss.attack(self)
		# Check for light
		has_light = None
		for item in self.inventory:
			if item.type == "tool":
				if item.is_tool:
					if item.is_bright:
						self.has_light = True
		# Check for hunger
		if self.hunger >= 14:
			self.hungry = True
		else:
			self.hungry = False
		if self.hungry and not self.hnc:
			eting = query.ask_yes_or_no("You're hungry. Stop to eat now? ")
			self.hnc = 4
			if eting:
				foods = []
				for item in self.inventory:
					if item.type == "item":
						if item.is_edible:
							foods.append(item)
				if foods:
					words.list_items(foods)
					food = raw_input("What do you eat? ")
					to_eat = None
					for item in foods:
						if food == item.name:
							to_eat = item
					if to_eat:
						self.eat(to_eat)
					else:
						print str(words.aN(food)).capitalize(), "is not a food."
				else:
					print "Unfortunately, you have nothing edible in your inventory."
					self.eat()
			else:
				self.hunger += 1
		elif self.hnc:
			self.hnc -= 1
		else:
			hunger_chance = random.randrange(constants.HUNGER_INCREASE_FACTOR)
			if not hunger_chance:
				self.hunger += 1
		if self.hunger >= 100:
			self.health -= constants.STARVATION_DEDUCTION
			print "You are starving."
			print "Eat something, pronto."
		elif self.hunger >= 50:
			self.health -= constants.STARVATION_DEDUCTION / 4
			print "You are slowly starving."
		# Check for feeling sick
		if self.diseased or (self.grossed_out > 3):
			print "You feel sick."
		# Check for first aid
		for item in self.inventory:
			if "aid" in item.name:		# first aid kit, band-aide, etc.
				self.bitten = False
				healing = random.randrange(constants.HEALTH_BONUS_FACTOR)
				health = self.health + healing
				if health > self.health:
					print "Good news--you have recovered", healing, "percent of your health."
					self.health += healing
				yummier = random.randrange(constants.FEELING_BETTER_FACTOR)
				if not yummier:
					self.grossed_out -= 1
		# Check for out-of-control fires
		for location in game.locations:
			for thing in location.stuff:
				if thing.name == "fire":
					try:
						if thing.burn_chance:
							# Make it burn, if random() says so
							chance = constants.FIRE_SPREADING_CHANCE - thing.burn_chance
							if chance < 1:
								chance = 1
							chance = random.randrange(chance)
							if not chance:
								# then the fire burns out of control
								la = True
					except(AttributeError):
						print '\n\a\n'
						print "This is an error."
						print "Someone has built a fire, which could potentially spread. However,"
						print "all the code is not yet in to implement a spreading fire. Fixing"
						print "this bug is on the to-do list."
						print "Move along...\n"
		# Check for health values outside a valid range.
		if self.health > 100:
			self.health = 100
		elif self.health < 0:
			self.health = 0
		# Now that everything's done, we can set "moved" to False; if you haven't just walked here, creatures can
		# now attack you.
		self.moved = False
		# Check for death
		# Always keep this one last
		if self.health <= 0:
			self.is_alive = False
			self.die()
		# Win game, if not dead
		if self.won and self.location == game.finishline:
			self.win()
		
		
	def die(self):
		'''One guess.'''
		print "\n\a\nYou have died."
		print "Game Over."
		choice = None
		while choice not in ("yes", "no", True, False):
			choice = query.ask_yes_or_no("\nContinue from a save? ")
			if choice:
				game.load_game()
			elif not choice:
				game.quit()

	def win(self):
		'''Calls the game's win function.'''
		string = 'espeak "You have won, ' + player.name + '!"'
		print "You have won!"
		commands.getoutput(string)
		will_continue = query.ask_yes_or_no("End game now? ")
		if will_continue:
			game.win()


class Adventure_Game(interface.Constructor):
	'''A simple adventure game.'''
	def __init__(self):
		'''Put a random thing somewhere.
		#location = random.choice(self.locations)
		#location.stuff.append(constants.bonus)'''
		super(Adventure_Game, self).__init__()
		
			
	def load_game(self, saved_game):
		'''A new way to load, directly through parameters and 'for' loops. Untested as yet.'''
		try:
			for attribute in self.player.attributes:
				attribute = cPickle.load(saved_game)
			self.player.moved = False
			for attribute in self.attributes:
				attribute = cPickle.load(saved_game)
			for location in self.locations:
				location = cPickle.load(saved_game)
			if self.bosstributes:
				for attribute in self.bosstributes:
					attribute = cPickle.load(saved_game)
		except(EOFError, IOError):
			print "Data corrupted, load failed."
		saved_game.close()
		return attribute, location
	def load(self):
		'''Load a saved game
		Note: This _used_ to be the default load method; this is now under reconstruction.
		FIXME: For yet another time, it is not working. It doesn't load a thing.'''
		shall_save = query.ask_yes_or_no("Save this game first? ")
		if shall_save:
			self.save(self.player)
		path = raw_input("Please specify a valid file path of the current version of the game: ")
		try:
			to_load = open(path, 'r')
		except(IOError):
			try_again = query.ask_yes_or_no("Invalid file path. Try again? ")
			if try_again:
				path = raw_input("Please enter the new file: ")
				try:
					to_load = open(path, 'r')
				except(IOError):
					try:
						print "Invalid file path, trying default..."
						to_load = open("/tmp/autosave.adv", 'r')
					except(IOError):
						try:
							to_load = open("/tmp/enture.adv", 'r')
						except:
							print "No valid saves found. You'll have to go on from where you are."
						else:
							self.load_game(to_load)
					else:
						self.load_game(to_load)
				else:
					self.load_game(to_load)
			print "Canceled."
		else:
			self.load_game(to_load)		

	def save(self, player, path):
		''''Save the player's progress.
		The latest way to save. This is a bit neater than before, and works with autosave.'''
		# Check if file path is valid
		try:
			success = None
			file = open(path, 'w')
		except(IOError):
			print "Invalid file path, saving to /tmp."
			try:
				file = open("/tmp/enture.adv", 'w')
			except(), e:
				print "Oddly, Python cannot save today:", e
				print "Please contact the developer."
				success = False
			else:
				print "Saving to default."
				success = True
		else:
			success = True
		# Write to the file
		if success:
			self.player.attributes = (self.inventory, self.health, self.grossed_out, self.hunger,
									  self.hungry, self.location, self.bitten, self.diseased,
									  self.wounded, self.matches, self.light, self.won, self.skills)
			try:
				for attribute in self.player.attributes:
					cPickle.dump(attribute, file)
				for attribute in self.attributes:
					cPickle.dump(attribute, file)
				for location in self.locations:
					cPickle.dump(location, file)
				if self.boss:
					for attribute in self.bosstributes:
						cPickle.dump(attribute, file)
			except:
				print "Oh, great. An error. No luck saving."
		file.close()
			
						
	def start(self):
		'''Start the game'''
		name = raw_input("What is your name? ")
		if not name:
			name = "Some weirdo"
		# instantiate the player
		self.player = Adventurer()
		self.player.name = name.title()
		self.player.location = self.starting
		self.player.inventory = self.tools
		self.play()
	
	def restart(self):
		'''Begin another round'''
		print "Reloading maps..."
		import interface
		self.__init__()
		self.player.__init__()
		for location in self.locations:
			location.__init__()

	def play(self):
		'''Play the game for the person's entire life :P'''
		while self.player.is_alive:
			self.get_usr_input(self.player)
	
	def help(self):
		'''Give the clueless user some much-needed help.'''
		print '''\
You can do the following:
help, h		-	display this help message
status		-	check how you're doing
look		-	look around
take		-	pick up an item
leave		-	leave an item behind
move		-	go to another location
dig 		-	dig for buried items
cut down	-	chop down a tree
eat 		-	eat something
fry 		-	fry something
set fire	-	build a fire
put out		-	put out a fire
light		-	burn a flammable item
attack		-	attack a dangerous animal
fight		-	fight a larger threat
combat		-	combat an enemy
wait		-	wait for a turn
check map	-	look at your map (if applicable)
clear		-	clear the screen
save		-	save the game (please specify path)
load		-	load another game (will prompt for save)
restart		-	start another game (will prompt for save)
quit, exit	-	leave the game (will prompt for save)'''
		
	def get_usr_input(self, player):
		'''Do stuff
		FIXME: Have it so that the player can do everything in one line. Use parameters.'''
		action = None
		while not action:
			action = raw_input("Your action ('h' for help): ")
			action.lower()
		# correspond commands to player functions
		if action == "look":
			player.look(player.location)
		elif "take" in action:
			item_name = raw_input("Take what? ")
			'''if item.lower() not in self.player.location.stuff:
				print "Error:", item.lower(), "is not available at this time."'''
			has_taken = False
			for thing in player.location.stuff:
				if item_name == thing.name:
					item = thing
					has_taken = True
					if item.is_takeable:
						self.player.pick_up(thing)
					else:
						print "You cannot take the", item_name + '.'
			if not has_taken:
				print "Error:", item_name, "is not available at this time."
		elif "leave" in action:
			player.leave()
		elif "map" in action:
			player.check_map()
		elif "move" in action:
			player.move()
		elif "status" in action:
			print player
		elif "dig" in action:
			has_shovel = False
			for item in player.inventory:
				if item.type == "tool":
					if item.is_digger:
						has_shovel = True
						player.dig()
			if not has_shovel:
				print "You have nothing which you can use to dig."
		elif "bury" in action:
			player.bury()
		elif "eat" in action:
			foods = []
			for item in player.inventory:
				if item.type == "item":
						if item.is_edible:
							foods.append(item)
			if foods:
				words.list_items(foods)
				food = raw_input("What do you eat? ")
				to_eat = None
				for item in foods:
					if food == item.name:
						to_eat = item
				if to_eat:
					player.eat(to_eat)
				else:
					print str(words.aN(food)).capitalize(), "is not a food."
			else:
				print "Unfortunately, you have nothing edible in your inventory."
		elif "fry" in action:
			self.player.fry()
		elif "put out" in action:
			self.player.extinguish()
		elif "fire" in action:
			trees = []
			for thing in player.location.stuff:
				if thing.is_burnable:
					trees.append(thing)
			words.list_items(trees, error = "Sorry, you have nothing with which to start a fire.")
			wood = raw_input("Choose a source of wood: ").lower()
			log = None
			for tree in trees:
				if wood == tree.name:
					wood = tree
					log = True
			firestarter = False
			firestarters = []
			for item in player.inventory:
				if item.is_firestarter:
					firestarters.append(item)
			words.list_items(firestarters)
			fire_name = raw_input("Choose a source of flame: ").lower()
			for item in player.inventory:
				if item.name == fire_name:
					firestarter = True
					source = item
			if log and firestarter:
				self.player.build_fire(wood, source)
			else:
				print str(wood).capitalize(), "is not available at this time."
		elif "light" in action:
			firestarters = []
			candles = []
			has_firestarter = False
			has_flammable = False
			for item in player.inventory:
				#if item.type == "tool":
				if item.is_firestarter:
						has_firestarter = True
						firestarters.append(item)
				if item.is_flammable:
					has_flammable = True
					candles.append(item)
			if has_firestarter and has_flammable:
				words.list_items(firestarters)
				starter = raw_input("Choose a source of flame to light with: ")
				for firestarter in firestarters:
					if starter == firestarter.name:
						starter = firestarter
				words.list_items(candles)
				candle = raw_input("Choose an item to light: ")
				for cndl in candles:
					if candle == cndl.name:
						candle = cndl
				self.player.set_fire(starter, candle)
			elif not has_firestarter:
				print "You have nothing to light a fire with."
			elif not has_flammable:
				print "You have nothing flammable to set fire to."
			else:
				print "Very weird bug. Please contact the developer."
				print "Include in your report exactly what you did, and the version of the game."
		elif ("chop" or "cut") in action:
			# I'm a lumberjack and I don't care
			lumberjack = None
			for tool in player.inventory:
				if tool.type == "tool" or tool.type == "weapon":
					if tool.is_cutter:
						lumberjack = tool
			if not lumberjack:
				print "You need an axe or something similar to cut down trees."
			else:
				trees = []
				for item in player.location.stuff:
					if "tree" in item.name and not item.takeable:
						trees.append(item)
				words.list_items(trees)
				tree_name = raw_input("Select a tree to cut: ")
				wood = None
				for tree in trees:
					if tree.name == tree_name:
						wood = tree
				if wood:
					self.player.cut_down(wood)
				else:
					print tree_name.capitalize(), "is not available at this time."
		######
		elif "attack" in action:
			self.player.attack()
		elif "fight" in action:
			targets = []
			for creature in player.location.stuff:
				if creature.is_dangerous:
					targets.append(creature)
				elif creature.is_hostile:
					print "Simply attack the", creature, player.name + '.'
				else:
					print creature.name.capitalize(), "won't hurt you."
			if targets:
				words.list_items(targets)
				target_name = raw_input("Select a target: ").lower()
				for target in targets:
					if target.name == target_name:
						creature = target
						self.player.fight(creature)
			else:
				print "There are no dangerous creatures, animals, or enemies around."
		elif "combat" in action:
			self.player.combat(self.boss)
		elif len(action) >=3 and action in "trade buy sell":
			self.player.trade(self.player.location)
		elif "wait" in action:
			self.player.wait()
		elif action in ("help", 'h') or "help" in action:
			self.help()
		elif action == "clear":
			print commands.getoutput('clear')
		elif "save" in action:
			file = raw_input("Please specify a name and file path to save to in the format \
/folder/name.adv: (nothing to cancel) ")
			self.save(self.player, file)
		elif "load" in action:
			self.load()
		elif "restart" in action:
			self.restart(False)
		elif action in ("quit", "exit", "close"):
			will_quit = query.ask_yes_or_no("Quit and save (or abort) game? ")
			if will_quit:
				will_save = query.ask_yes_or_no("Save first? ")
				if will_save:
					self.save(self.player)
				self.quit()
			else:
				print "Canceled."
		else:
			print "Unknown action."
		
	def win(self):
		'''Write the player's name to a file, and then quit()'''
		scores = open("scores.txt", 'a+')
		output = self.player.name
		output += '\t-\t' + str(self.player.health) + '\t-\t'
		output += time.ctime()
		scores.write(output)
		print scores.read()
		scores.close()
		self.quit()
		
	def quit(self):
		'''Quit the game gracefully.'''
		print "Thank you for playing. Please do so again."
		quit()



# main
if __name__ == "__main__":
	game = Adventure_Game()
	game.start()
