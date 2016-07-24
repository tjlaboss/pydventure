# Items
# A module for Python Adventure Game containing classes for items

class Item(object):
	'''A simple item that you can put in your inventory.'''
	def __init__(self,						name,					key,
				 is_tool = False,			is_takeable = True,		is_weapon = False,			is_mobile = False,
				 is_edible = False,			is_cookable = False,	is_flammable = False):
		self.name = name
		self.key = key
		self.is_weapon = is_weapon
		self.is_tool = is_tool
		self.is_takeable = is_takeable
		self.is_mobile = is_mobile 
		self.is_edible = is_edible
		self.is_cookable = is_cookable
		self.is_flammable = is_flammable
		
		self.type = "item"
		
	
	def __str__(self):
		return self.name
	
	
	def fry(self):
		'''Get cooked. Make it edible.'''
		self.is_edible = True
		self.is_cookable = False
		self.is_mobile = False
		
		# Rename appropriately
		if self.name.lower()[:5] == "dead ":
			 self.name = self.name[5:]
		self.name = "cooked " + self.name
	
	
	# More methods to come
	

class Animal(Item):
	'''An Item that is by default alive and mobile, and can die.'''
	def __init__(self,						name,					key,
				 is_tool = False,			is_takeable = False,	is_weapon = False,
				 is_mobile = True,			is_edible = False,		is_cookable = False,
				 is_flammable = False):
		super(Animal, self).__init__(name, key, is_tool, is_takeable, is_weapon, is_mobile,
									 is_edible, is_cookable, is_flammable)
		
		#self.is_edible = False
		#
		self.is_mobile = True
		self.type = "animal"
		
	def die(self):
		'''Become dead, immobile, and cookable'''
		self.name = "dead " + self.name
		self.is_mobile = False
		self.is_cookable = True
		self.is_takeable = True
		self.type = "item"



class Tool(Item):
	'''An Item that can be used to accomplish tasks'''
	def __init__(self,						name,					key,
				 is_tool = True,			is_takeable = True, 	is_weapon = False,			is_mobile = False,
				 is_edible = False,			is_cookable = False,	is_flammable = False,	
				 # New attributes
				 is_digger = False,			is_blade = False,		is_firestarter = False,	uses = -1):
		super(Tool, self).__init__(name, key, is_tool, is_takeable, is_weapon, is_mobile,
									is_edible, is_cookable, is_flammable)
		
		self.is_digger = is_digger
		self.is_blade = is_blade
		self.is_firestarter = is_firestarter
		self.uses = uses
		
		# Set some required behaviors
		self.is_edible = False
		self.is_tool = True
		self.type = "tool"
		
	def __str__(self):
		if self.uses > 0:
			return self.name + " (remaining: " + str(self.uses) + ")"
		elif self.uses == 0:
			return self.name + " (useless)"
		else:
			# Infinite uses
			return self.name
	
	def use(self):
		'''This method is called if the player uses a tool,
		either for its intended purpose or as a weapon.'''
		self.uses -= 1


# Commonly used items
shovel = Tool("shovel", "shovel", is_weapon = True, is_digger = True)
knife  = Tool("knife", "knife", is_weapon = True, is_blade = True)
matchbook = Tool("matchbook", "matches", is_firestarter = True, uses = 5)

# Special items
map = Item("map", "map"); map.type = "map"



