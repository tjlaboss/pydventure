# Adventurer.py
#
# Module containing a class for the Adventurer (player)


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
				 #inventory = ["shovel", "clothing", "flashlight"],
				 inventory = {},
				 health = 100,
				 hunger = 0,
				 has_map = False):
		
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
		
		self.name = ""
		
		# Establish a maximum number of things the player can hold.
		# Someday, I will allow the usage of bags, backpacks, or boxes, but for now, it is constant.
		self.MAX_ITEMS = 9
		
		
		def report(self):
			'''Return a string containing the player's status'''
			rep = self.name
			rep += "'s Status Report:\n"
			rep += "You are " + str(self.health) + "% healthy.\n"
			if self.hunger >= 3:
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
	
		
		
		
		
		