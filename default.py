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
		towel = items.Item(name = "towel", key = "towel", is_flammable = True)
		wreck = items.Item(name = "piece of wreckage", key = "wreckage")
		palm_tree = items.Item(name = "palm tree", key = "tree", is_takeable = False)
		coconut = items.Item("coconut", is_edible = True)
		earthworms = items.Item("earthworms", is_edible = True)
		# buried objects
		bottle = items.Item(name = "bottle")
		suit = items.Item(name = "somebody's swimsuit", key = "swimsuit")
		
		
		# the beach itself
		self.beach = l.Location(name = "the beach",
							  	key = "beach",
							    stuff = {towel.key:towel, wreck.key:wreck, palm_tree.key:palm_tree, coconut.key:coconut},
							    #adjacent = (self.hill),
							    description = beach_descript,
							    num = '1',
							    buried = {bottle.key:bottle, suit.key:suit},
							    is_dark = False)
		
		# Create a hill
		hill_descript = '''\
A grassy hill overlooking the island. The sea and beach to the east look
more forbidding atop your perch. You can hear water in the north. In the
west is a field of some sort. In the distance, to the northwest, is some
sort of rocky, clayish terrain.'''
		self.hill = l.Location(name = "a hill",
							   key = "hill",
							   #adjacent = (self.beach, self.stream),
							   description = hill_descript,
							   num = '2',
							   buried = {earthworms.key:earthworms,},
							   is_dark = False)
	
		# Create the cave
		cave_descript = '''\
With your flashlight, you can make out much of the cave. Though this
place gives you "the creeps", you are grateful for shelter. Rocks and
pebbles are strewn all over the floor.'''
		rocks = items.Item("rocks")
		pebbles = items.Item("pebbles")
		#snake = items.snake
		self.cave = l.Location(name = "the cave",
							   key = "cave",
							   #stuff = [self.rocks, self.pebbles, items.snake],
							   stuff = {"rocks":rocks, "pebbles":pebbles},
							   #adjacent = (self.stream),
							   description = cave_descript,
							   num = '3',
							   buried = {"map":items.map,},
							   is_dark = True)
	
		# Create a stream
		stream_descript = '''\
A peaceful freshwater stream. Now you have plenty to drink and a place
to wash. Farther downstream, to the east, a school of minnows swims.
Farther upstream, to the west, are what appear to be rocky caverns.
You have a good view of the hill you recently descended.	'''
		self.stream = l.Location(name = "a small stream",
							     key = "stream",
							     #adjacent = (self.hill, self.cave),
							     description = stream_descript,
							     num = '4',
							     is_dark = False)
	
		# Create a field
		field_descript = '''\
A quiet field with what appears to be wheat growing. To the north-
east is the hill you recently descended, and to the southeast, a 
shelter of sorts! Could there somehow be life on this deserted island?'''
		seeds = copy.copy(items.seeds)
		self.field = l.Location(name = "a wheat field",
							    key = "field",
							    stuff = [],
							    #adjacent = (self.hill, self.shack),
						        description = field_descript,
						        num = '5',
						        buried = {seeds.key:seeds},
						        is_dark = False)
	
		# Create an old, abandoned shack
		shack_descript = '''\
This shaky shack looks like it's been deserted since the Middle Ages.
To your disappointment, there is no one here, or any food. But at
least you have a snake-free place to sleep.'''
		axe = copy.copy(items.axe)
		knife = copy.copy(items.knife)
		skeleton = items.Item("skeleton")
		pan = copy.copy(items.frying_pan)
		self.shack = l.Location(name = "an old shack",
							    key = "shack",
							    stuff = {axe.key:axe, knife.key:knife},
							    #adjacent = (self.field),
							    description = shack_descript,
							    num = '6',
							    buried = {skeleton.key:skeleton, pan.key:pan},
							    is_dark = False)
	
		# Location object template
		'''_descript = 
		template = l.Location(name = "",
							  key = "",
						      stuff = {},
						      # adj = {},
						      description = _descript,
						      num = '',
						      buried = {},
						      is_dark = False)'''

		# Make some locations adjacent to one another
		self.beach.adj = {self.hill.key:self.hill,}
		self.hill.adj = (self.beach, self.stream, self.field)
		self.cave.adj = {self.stream.key:self.stream,}
		self.stream.adj = {self.hill.key:self.hill, self.cave.key:self.cave}
		self.field.adj = {self.hill.key:self.hill, self.shack.key:self.shack}
		self.shack.adj = {self.field.key:self.field,}
		
		self.locations = (self.beach, self.hill, self.cave, self.stream, self.field, self.shack)
	
	def do_thing(self):
		'''Make wheat grow'''
		if "seeds" in self.field.buried:
			self.grow_timer -= 1
			if not self.grow_timer:
				del self.field.buried["seeds"]
				self.wheat = copy.copy(self.seeds)
				self.wheat.name = "wheat"; self.wheat.key = "wheat"
				self.field.stuff["wheat"] = self.wheat

if __name__ == "__main__": print "This is a module with the default map for Python Adventure Game."





