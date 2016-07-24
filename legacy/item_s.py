# Items
# 
# A module for Python Adventure Game containing classes for items such as tools, weapons, foods,
# and especially animals. This began as part of constants.py
#
# 5/25/10 --> created (as yet unused) classes for animals and items, largely dependent on each other.
# I need to do a lot of reworking on several maps before I use these; song of the day was 'Canon'.



# A WIP class for an item; should be a constructor for weapons and animals, but in itself be a "junk"
class Item(object):
	'''A class for a takeable item.'''
	def __init__(self, type = "junk", name = "", edible = False, fryable = False, size = 1):
		if edible:
			self.TYPE = "food"
		else:
			self.TYPE = type		# e.g., armor, light, junk, etc.
		self.name = str(name)		# i.e., "shovel"
		self.is_fryable = fryable	# whether you can fry it
		self.size = int(size)		# how much room in the inventory it takes up
	def __str__(self):
		'''Returns the object's name'''
		return self.name
	
class Weapon(Item):
	'''A weapon for warding off enemies'''
	def __init__(self, name, size, klass):
		super(Item, self).__init__()#name, size)
		self.TYPE = "weapon"
		self.klass = klass		# tuple object; names all that apply: ("cutters", "guns")
		
class Animal(Item):
	'''A constructor class for an animal; also works for the simplest animals.'''
	def __init__(self, name = "", edible = False, fryable = False, size = 1):
		super(Item, self).__init__()#name, edible, fryable, size)
		self.name = str(name)
		self.is_fryable = fryable
		if not edible:
			self.TYPE = "peaceful"
		self.wounded = False
	def __str__(self):
		return self.name
	def die(self, location):
		'''Kill the animal, and replace it with a dead animal.
		FIXME: Eventually have a prefix variable; for instance, prefix = "dead "/prefix = "fried "'''
		location.stuff.remove(self)
		if self.TYPE == "dangerous":
			if self.wounded:
				self.name[7:]			# removes "wounded" from creature name
		dead = "dead " + self.name		# turns "creature" into "dead creature"
		dead_creature = Dead_Animal(name = dead, fryable = self.is_fryable, edible = self.is_edible)
		location.stuff.append(dead_creature)
			
	
class Hostile_Animal(Animal):
	'''A hostile animal; also see Dangerous_Animal'''
	def __init__(self, name = "", fryable = True, venemous = False, infected = False, damage = 0):
		super(Animal, self).__init__()#name, fryable)
		self.TYPE = "hostile"
		self.is_venemous = venemous		# whether a bite will be life-threatening
		self.is_infected = infected		# whether a bite will cause disease
		self.damage = int(damage)		# the range for a random amount of damage it can cause
	
class Dangerous_Animal(Hostile_Animal):
	'''A dangerous animal that you may have to fight.'''
	def __init__(self, 				name = "",
				fryable = True, 	damage = 34,
				venemous = False, 	infected = False,
				danger = 3):#,			):
		super(Hostile_Animal, self).__init__(name, fryable, damage, venemous, infected)
		self.TYPE = "dangerous"
		#self.is_mobile = mobile	-->		is determined, like speed, in the map module
		
class Dead_Animal(Animal):
	def __init__(self, fryable, edible):
		self.is_fryable = fryable
		self.is_edible = edible
		
class Fried_Animal(object):		#..._Animal(Food):
	'''A fried animal. A type of food.'''
	def __init__(self, name):
		self.is_fryable = False
		self.name = name
		self.is_edible = True	# FIXME: I have both is_edible and self.type = "food". I need to
		self.TYPE = "food"		# consolidate them into one, to avoid unnecessary obfuscation.
	def __str__(self):
		return self.name
# When this section is finished, adventure.py will say, "if item.TYPE == 'weapon': . . . "

def test():
	'''A unit test'''
	import location
	axe = Weapon("bladed", "shovel", False)
	rabbit = Animal("rabbit", False, True)
	yeti = Dangerous_Animal("yeti", False, 34, 3)
	place = location.Location("Nowhere", "no", [rabbit, yeti], (),
							  "The middle of nowhere", 0, (), False)
	print "Death of a rabbit."
	rabbit.die(place)
	print "Death of a yeti."
	yeti.die(place)
	
if __name__ == "__main__": test()