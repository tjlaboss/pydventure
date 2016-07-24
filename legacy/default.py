# Adventures module
# Contains a map and classes

import items
import location as l
import copy, random

# A map that is independent of any object
MAP = '''\
 ______________________________________
|         stream               \ w w w |
|cave    /****4                 \ w w w|
|____   ***                      \ w w |
| 3 O                __           \ w w|
|\_/                /  \           \ w |
|                  / 2           __|  w|
|                 hill    beach /  w w |
|   i-i-i field             1  |  w w  |
|  i-i-i-i 5    _              | w w w |
|             6/ \ shack      /   w w  |
|_____________|_n|_____________________|'''

class Adventure_Map(object):
	'''A constructor class for the island map.'''
	def __init__(self):
		'''Creates locations, sets the player's starting variables, and other stuff.'''
		self.name = "Default Island"
		self.create_locations()
		self.starting = self.beach
		self.tools = [copy.copy(items.shovel), copy.copy(items.clothing), copy.copy(items.flashlight)]
		self.boss = None
		self.bosstributes = None
		self.grow_timer = random.randrange(20) + 5
		self.attributes = (self.name, self.grow_timer)
		
		
	def create_locations(self):
		'''Create the locations and descriptions for the default island map'''
		
		# Create the beach
		beach_descript = '''\
Sandy ground. To the east is the sea. Were you not stranded here,
you'd set up a chair, umbrella, and towel, and go for a swim.'''
		# objects lying around
		self.towel = items.Item(name = "towel", flammable = True)
		self.wreck = items.Item(name = "piece of wreckage")
		self.palm_tree = items.Item(name = "palm tree", takeable = False)
		self.coconut = items.Item(name = "coconut", edible = True, good = True)
		# buried objects
		self.bottle = items.Item(name = "bottle")
		self.suit = items.Item(name = "somebody's swimsuit")
		# the beach itself
		self.beach = l.Location(name = "the beach",
							  	ref = "beach",
							    #stuff = ["towel", "piece of wreckage", "palm tree", "coconut"],
							    stuff = [self.towel, self.wreck, self.palm_tree, self.coconut],
							    #adjacent = (self.hill),
							    adj = (),
							    description = beach_descript,
							    num = '1',
							    buried = [self.bottle, self.suit],
							    is_dark = False)
		
		# Create a hill
		hill_descript = '''\
A grassy hill overlooking the island. The sea and beach to the east look
more forbidding atop your perch. You can hear water in the north. In the
west is a field of some sort. In the distance, to the northwest, is some
sort of rocky, clayish terrain.'''
		self.hill = l.Location(name = "a hill",
							   ref = "hill",
							   stuff = [],
							   #adjacent = (self.beach, self.stream),
							   adj = (),
							   description = hill_descript,
							   num = '2',
							   buried = [items.earthworms,],
							   is_dark = False)
	
		# Create the cave
		cave_descript = '''\
With your flashlight, you can make out much of the cave. Though this
place gives you "the creeps", you are grateful for shelter. Rocks and
pebbles are strewn all over the floor.'''
		self.rocks = items.Item(name = "rocks")
		self.pebbles = items.Item(name = "pebbles")
		self.cave = l.Location(name = "the cave",
							   ref = "cave",
							   stuff = [self.rocks, self.pebbles, items.snake],
							   #adjacent = (self.stream),
						 	   adj = (),
							   description = cave_descript,
							   num = '3',
							   buried = ["map",],
							   is_dark = True)
	
		# Create a stream
		stream_descript = '''\
A peaceful freshwater stream. Now you have plenty to drink and a place
to wash. Farther downstream, to the east, a school of minnows swims.
Farther upstream, to the west, are what appear to be rocky caverns.
You have a good view of the hill you recently descended.	'''
		self.stream = l.Location(name = "a small stream",
							     ref = "stream",
							     stuff = [],
							     #adjacent = (self.hill, self.cave),
							     adj = (),
							     description = stream_descript,
							     num = '4',
							     buried = [],
							     is_dark = False)
	
		# Create a field
		field_descript = '''\
A quiet field with what appears to be wheat growing. To the north-
east is the hill you recently descended, and to the southeast, a 
shelter of sorts! Could there somehow be life on this deserted island?'''
		self.seeds = copy.copy(items.seeds)
		self.field = l.Location(name = "a wheat field",
							    ref = "field",
							    stuff = [],
							    #adjacent = (self.hill, self.shack),
						 	    adj = (),
						        description = field_descript,
						        num = '5',
						        buried = ["seeds",],
						        is_dark = False)
	
		# Create an old, abandoned shack
		shack_descript = '''\
This shaky shack looks like it's been deserted since the Middle Ages.
To your disappointment, there is no one here, or any food. But at
least you have a snake-free place to sleep.'''
		self.shack = l.Location(name = "an old shack",
							    ref = "shack",
							    stuff = [copy.copy(items.axe), copy.copy(items.knife)],
							    #adjacent = (self.field),
							    adj = (),
							    description = shack_descript,
							    num = '6',
							    buried = ["skeleton", "frying pan"],
							    is_dark = False)
	
		# Location object template
		'''_descript = 
		template = l.Location(name = "",
							  ref = "",
						      stuff = [],
						      #adjacent = (self.)
						      adj = (),
						      description = _descript,
						      num = '',
						      buried = (),
						      is_dark = False)'''

		# Make some locations adjacent to one another
		self.beach.adj = (self.hill,)
		self.beach.adjacent = (self.hill.name, self.beach.name)
		self.hill.adj = (self.beach, self.stream, self.field)
		self.hill.adjacent = (self.beach.name, self.stream.name, self.field.name, self.hill.name)
		self.cave.adj = (self.stream,)
		self.cave.adjacent = (self.stream.name, self.cave.name)
		self.stream.adj = (self.hill, self.cave)
		self.stream.adjacent = (self.hill.name, self.cave.name, self.stream.name)
		self.field.adj = (self.hill, self.shack)
		self.field.adjacent = (self.hill.name, self.shack.name)
		self.shack.adj = (self.field,)
		self.shack.adjacent = (self.field.name, self.shack.name)
		
		self.locations = (self.beach, self.hill, self.cave, self.stream, self.field, self.shack)
	
	def do_thing(self):
		'''Make wheat grow'''
		if self.seeds in self.field.buried:
			self.grow_timer -= 1
			if not self.grow_timer:
				self.field.buried.remove(self.seeds)
				self.wheat = copy.copy(self.seeds)
				self.wheat.name = "wheat"
				self.field.stuff.append(self.wheat)

if __name__ == "__main__": print "This is a module with the default map for Python Adventure Game."