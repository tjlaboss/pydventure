# Adventurer.py
#
# Module containing a class for the Adventurer (player)

#import location
from words import aN, list_items


# Global variables
HUNGER_THRESHOLD = 30	# turns before hunger manifests
FOOD = 10				# how much hunger goes down with each meal

class Adventurer(object):
	'''The player of this game.
	Required Inputs:
		location:	string; key of the Location object where the player is
	
	Optional Inputs:
		inventory:	dictionary of items the player possesses. Keys are
					the string Item.key; values are Item instances.
					[default: nothing]
					
		health:		integer. [default: 100]
		
		hunger:		integer; how many meals the player needs to eat.
					[default: 0]
		
		has_map:	Boolean; whether the player has access to a
					map or GPS. [default: False]
		 
	
	'''
	def __init__(self,
				 location,
				 name = "",
				 #inventory = ["shovel", "clothing", "flashlight"],
				 inventory = {},
				 health = 100,
				 hunger = 0,
				 has_map = False):
		
		self.name = name
		self.inventory = inventory
		self.health = int(health)
		self.hunger = hunger
		self.hnc = 0	# hunger nag counter
		self.location = location
		
		
		self.is_alive = True
		self.is_diseased = False
		self.moved = False
		self.light = True
		self.won = False
		#self.matches = 5
		#self.skills = 1.0
		
		
		
		# Establish a maximum number of things the player can hold.
		# Someday, I will allow the usage of bags, backpacks, or boxes, but for now, it is constant.
		self.MAX_ITEMS = 9
		
		
		def report(self):
			'''Return a string containing the player's status'''
			rep = self.name
			rep += "'s Status Report:\n"
			rep += "You are " + str(self.health) + "% healthy.\n"
			if self.hunger >= 30:
				rep += "You are hungry.\n"
			rep += "You have "
			for item in self.inventory:
				rep += '\n*' + tool.name
				if item.type == "tool":
					if tool.uses > 0:		# with uses left,
						# say how many uses are remaining
						rep += '\t\t[' + tool.remaining_txt + ': ' + str(tool.uses) + ']'
			if not self.inventory:
				rep += "absolutely nothing..."
			rep += "\n...and you're at " + self.location.name + '.'
			return rep
	
	
		def pick_up(self, item):
			'''Take an item from the surrounding location.'''
			if item.is_takeable:
				self.inventory[item.key] = item
				del self.location.stuff[item.key]
				self.__update()
			else:
				print "You cannot pick up the", item.name
		
		
		def leave(self, item):
			'''Leave some of your stuff behind.'''
			self.location.stuff[item.key] = item
			del self.inventory[item.key]
			self.__update()
		
		
		def check_map(self, level_map):
			'''Take a look at the map.'''
			if self.has_map:
				the_map = level_map[:]								 	# make a copy of the map
				if self.location.num in self.map:
					self.map = self.map.replace(self.location.num, '@')	# shows where you are
					for char in self.map:
						for place in game.locations:
							if char == place.num:
								self.map = self.map.replace(char, 'X')	# shows where you can go
					print the_map										# then displays the edited map
			else:
				print "You have no map."
		
		
		def move(self):
			'''Moves the player to a new location.'''
			old_location = self.location
			count = 0				# organize by columns
			print "You can access:",
			for loc in self.location.adjacent:
				print str(loc) + ';',
				count += 1
				if count == 4:
					print '\n',
			'''
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
		'''
		
		
		
		
		# TODO in self.__update():
		'''
		- update has_map
		- update hunger
		- check for victory conditions
			(self.is_alive, level.has_won)
		
		'''
		
		
		
		
		
		