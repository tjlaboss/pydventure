# Medieval Module
# Contains castle map for Pydventure
#
# Written for version 2.0, but is WIP for the latest version (2.3.3)
# Remember to deepcopy() objects containing objects


import location as l
import constants, items
import random, copy

MAP = '''\
 ______________________________________________________________________________________
| Rand McNally, (c) MMX        _  _  _               _  _  _                           |
|                             | || || |      $      | || || |                          |
|          .    _              \     / Top of Castle \     /               N           |
|    ^   ^ /\  /^\              | 0 |      _____      | 0 |                ^           |
|   /_\8/_\^|\/_|_\             |   |     /  _  \     |   |             W< + >E        |
|  /_ _\ |/_\ /_|_\           _ |   |____/  I_I  \____|   | _              v           |
|  _| |_ /_ _\/_|_\          /w |                         | w\             S           |
| ~~~~~~~ | | /_|_\         /ww |           ___           | ww\                        |
| Forest ~~~~~ | |         /ww/ | W. Wing  /   \  E. Wing | \ww\                       |
|             ~~~~~        |ww| |    !    | I I |    &    | |ww|                       |
|                          |ww| |_________|_I_I_|_________| |ww|                       |
|                          \ww\         9Drawbridge        /ww/                        |
|                           \ww\__________________________/ww/                         |
|         *                  \wwwwwwwwwwwwwwwwwwwwwwwwwwwwww/         ___              |
|       __Y                               |   |                       | |   ____       |
|      /   \                              |   |                           __|__|__     |
|     |__n__|                            /    |                          /|      |\    |
|     Village                        ___/     |                           |      |     |
|    -      7  _               _____/     /|  |                Marketplace  4       -  |
|   _       - / \             /      ____/  \  \                        _     _ _      |
|  / \  -     |n|       _____/   ___/    5   \  \______                  |   |         |
|  |n|     -      _____/     ___/  Crossroads \_____   \                /   /          |
|         _   _  /      ____/                       \   \__            |   |           |
|          \  \_/  ____/                             \     \___________/  /            |
|           \_   _/                  ___              \______             |            |
|             \ /                   / w \                    \     _______/            |
|             /-\                  |w % w|                    |   /                    |
|              -                    \_w_/                     |   |                    |
|     i - i - i - i - i            Fountain             _____/   /                     |
|       i - i - i - i - i           \ 2 /        ______/   _   _/       +              |
|       - i - i - i - i - i          | |     ___/      ___/ \  \       _|_             |
|       i - i  6  - i - i -  -   |_  \  \___/    _____/      \  \     / 0 \            |
|     i - i - i - i - i -     -    \__|     ____/             \  \   |  _  |           |
|   i - i - i - i - i - i  -  -  -  ___    /                   \  \  |_/^\_|           |
|          Demense               _ /   |   |                    \  \___ 3__            |
|                               |      |   |                     \______/Church        |
|                                     /     \                                          |
|                                   _/       \_                                        |
|                                        1                                             |
|                                 Outside of Town                                      |
|______________________________________________________________________________________|'''



class Adventure_Map(object):
	'''A medieval map best described by the map above.'''
	def create_locations(self):
		'''Create the locations and descriptions for the castle map'''
		
		# Create and describe the outskirts of town
		outside_town_descript = '''\
You are outside town. How you got here, you have no idea. The area is
dull, gray, and dismal...the weather is harsh. What  *is* this place?
To the north is a splashing fountain of sorts; to the northwest, a
sparse-looking grain field. In the northeast, you can see what you
think is a steeple. Roads lead in all three directions.'''
		self.silver_coin = items.Item(name = "silver coin")
		self.outside_town = l.Location(
							  name = "the outskirts of town",
							  ref = "outskirts",
						      stuff = [copy.copy(self.silver_coin),],
						      adj = (),
						      description = outside_town_descript,
						      num = '1',
						      buried = [],
						      is_dark = False)
		
		
		# Create and describe a fountain
		fountain_descript = '''\
A peaceful and splashing fountain of a knight on horseback. There
is no one and nothing else around. Peering into the fountain, you
can see that some people have thrown coins inside, but out of reach.'''
		self.fountain = l.Location(
							  name = "a fountain",
							  ref = "fountain",
						      stuff = [copy.copy(items.water), copy.copy(items.penny)],
						      adj = (),
						      description = fountain_descript,
						      num = '2',
						      buried = [],
						      is_dark = False)
		church_descript = '''\
What you're doing in the Middle Ages is beyond you. This small and
quaint church has stained glass windows, rows of pews, and a tiny
organ. There is not much else of interest.'''
		self.lit_candle = items.Tool(name = "lit candle", firestarter = True, bright = True)
		self.testlog = items.Tree()
		self.testlog.die()
		self.church = l.Location(
							  name = "a church",
							  ref = "church",
						      stuff = [copy.copy(self.lit_candle),],
						      adj = (),
						      description = church_descript,
						      num = '3',
						      buried = [],
						      is_dark = False)
		
		# Create and describe the marketplace
		market_descript = '''\
A loud and noisy marketplace! People mill about, ignoring you, on
their way to the next stall or shop. Enter "trade" to try to buy
something, if you have money, or to see what's available.'''
		'''for good in for_sale:
			thing = '\n' + good
			market_description += str(thing)
		market_descript = str(market_description[:].replace('\n\n', '\n'))'''
		# create some objects
		junk = items.Item(name = "monkey junk")
		self.gold_coin = items.Item(name = "gold coin")
		self.silver_coin = items.Item(name = "silver coin")
		dead_rabbit = copy.copy(items.rabbit)
		dead_rabbit.die()
		self.market = l.Market(
							name = "a marketplace",
							ref = "market",
						    stuff = [junk,],
						    adj = (),
						    description = market_descript,
						    num = '4',
						    buried = [copy.copy(self.gold_coin),],
						    sale = [copy.copy(items.frying_pan), copy.copy(items.candle), items.map,
								  	copy.copy(items.shovel), copy.copy(items.axe), dead_rabbit],
						    change_given = (copy.copy(self.silver_coin), copy.copy(self.silver_coin),
									 	 	copy.copy(self.silver_coin), copy.copy(self.gold_coin)),
							accepted_currency = ("silver coin", "silver coin", "silver coin", "gold coin"),
						    wanted = ("knife", "axe", "candle", "shovel", "penny", "dead raptor",
									  "clothing", "tronya", "dead deer", "frying pan", "monkey", "fried konquiture",
									  "sword", "helmet", "shield", "chestplate", "chain mail", "ubuntu tapestry",
									  "leather belt", "bread", "fried rabbit", "cape"),
							is_dark = False)
				
		# Create and describe the crossroads
		crossroads_descript = '''\
In the middle of town, the roads converge. Directly south and below
you is the fountain you saw at the start of your journey--you can
probably climb down onto it. In the east is a village; west, the
marketplace. A church is to the southwest, below the ridge you are
now on. Directly north is a ring of filthy water and a humongous,
forboding building. Creepy.'''
		self.crossroads = l.Location(
							  name = "a crossroads",
							  ref = "crossroads",
						      stuff = [],
						      adj = (),
						      description = crossroads_descript,
						      num = '5',
						      buried = [],
						      is_dark = False)
				
		# Create and describe the manor demense
		demense_descript = '''\
A sparse, semi-barren grain field. Upon the matted ground lie stalks
of non-productive crops, straw, and manure. There's not going to be
much of a harvest this year. The field is at a fairly stable
elevation, but extremely bumpy. To the north is a small village;
the area to the west lies outside of town. 
		'''
		self.demense = l.Location(
							  name = "the demense",
							  ref = "demense",
						      stuff = [],
						      adj = (),
						      description = demense_descript,
						      num = '6',
						      buried = [copy.copy(items.seeds), copy.copy(items.shovel)],
						      is_dark = False)
				
		# Create and describe a village
		vill_descript = '''\
A tiny collection of houses off to the side of the town. There's
not much to see (everyone's inside). To the south is a weak-looking
field, to the north a forest, and to the east a crossroads.'''
		self.broken_cart = items.Item(name = "broken cart", takeable = False, burnable = True, burn_chance = 2)
		self.straw = items.Item(name = "piece of straw")
		self.village = l.Location(
							  name = "a village",
							  ref = "village",
						      stuff = [self.broken_cart, self.straw],
						      adj = (),
						      description = vill_descript,
						      num = '7',
						      buried = [],
						      is_dark = False)
		
		# Create and describe a forest
		forest_descript = '''\
A dark, dense forest. The ground is somewhat wet. There are many
trees--mostly pine--growing around you. To the south is a village.'''

		# Create some trees
		self.tree = copy.copy(items.pine_tree)
		self.tree.name = "tree"
		self.log = copy.copy(items.pine_tree)
		self.log.die()
		self.christmas = copy.copy(items.pine_tree)
		self.christmas.name = "christmas tree"
		self.martin = items.Item(name = "purple martin")
		self.tree_fossil = items.Item(name = "fossil")
		self.forest = l.Location(
							  name = "the forest",
							  ref = "forest",
						      stuff = [copy.copy(items.pine_tree), self.tree, copy.copy(items.pine_tree),
									   self.log, self.christmas, self.martin, self.dragon],
						      #adjacent = (self.village)
						      adj = (),
						      description = forest_descript,
						      num = '8',
						      buried = [self.tree_fossil,],
						      is_dark = False)
		
		# Create and describe a drawbridge
		bridge_descript = '''\
Standing before you, of breathtaking size, is a castle! You stand
on the drawbridge, awed by the castle's magnificence. Despite that
the fortress is both forboding and forbidding, you cannot resist
the urge to enter it...for the bridge has just closed!'''
		self.bridge_descript_2 = '''\
Standing before you, of breathtaking size, is a castle! You stand
on the drawbridge, which has been reopened just for you, giving you
access to the outside world again. The crossroads are behind you.'''
		bridgexplanation = "Only armed and armored knights will be let across the moat. Therefore,"
		self.drawbridge = l.Forbidden_Location(
							  name = "the castle drawbridge",
							  ref = "drawbridge",
						      stuff = [],
						      adj = (),
						      description = bridge_descript,
						      num = '9',
						      buried = [],
						      required = self.armor,
						      reason = bridgexplanation,
						      is_dark = False)
				
		# Create and describe the castle's east wing
		w_descript = '''\
Suits of armer line the walls of this wing of the castle. It is
very dark, except for the light from torches. A stone staircase
leads upwards, hopefully to someplace lighter. From time to time,
a rat will dart out and squeak obnoxiously. Spiders work hard on
their webs by the torch light. One of their webs covers a hallway
to another wing of the castle, in the east.'''
		self.torch = items.Tool(name = "torch", flammable = True)
		self.lit_torch = items.Tool(name = "lit torch", bright = True, firestarter = True, tool = True)
		self.rat = items.Hostile_Animal(name = "rat", infected = random.choice(constants.TRUEFALSE), gross_food = True,
									    fryable = True, food = 10, venemous = False, hostility = 3)
		w_stuff = [copy.copy(self.torch), copy.copy(self.lit_torch), copy.copy(self.rat)] + self.armor
		self.w_wing = l.Forbidden_Location(
							  name = "the west wing of the castle",
							  ref = "west wing",
						      stuff = w_stuff,
						      adj = (),
						      description = w_descript,
						      num = '!',
						      buried = [],
						      required = self.armor,
						      reason = self.explanation,
						      is_dark = False)
				
		# Create and describe the castle's west wing
		e_descript = '''\
This wing of the castle is covered in tapestries. Several depict
jousting tournaments; a few more of them, historic battles; and
others, goofy-looking dragons. There is a thick layer of dust on
the floor. A rat gnaws casually on a tapestry and dashes out of
sight. A creaky wooden staircase leads upwards, presumably to the
outside; another section of the castle is to the west.'''
		self.tapestry = items.Item(name = "ubuntu tapestry", flammable = True)
		self.e_wing = l.Forbidden_Location(
							  name = "the east wing of the castle",
							  ref = "east wing",
						      stuff = [copy.copy(self.torch), copy.copy(self.lit_torch), copy.copy(self.rat),
									   copy.copy(items.axe), copy.copy(self.tapestry)],
						      adj = (),
						      description = e_descript,
						      num = '&',
						      buried = [],
						      required = self.armor,
						      reason = self.explanation,
						      is_dark = False)
				
		# Create and describe the castletop
		top_descript = '''\
You made it! The surrounding countryside looks so much more in-
viting from up here. A lush, fenced pasture is north of the castle,
a dark green forest to the east, and a river to the west. In the
southwest is a small village; in the southeast, a marketplace; and
directly south, a crossroads connecting it all. It is all so...so
glorious. But wait! Up here with you is a belligerent knight!'''
		self.top_descript2 = '''\
		You made it! The surrounding countryside looks so much more in-
viting from up here. A lush, fenced pasture is north of the castle,
a dark green forest to the east, and a river to the west. In the
southwest is a small village; in the southeast, a marketplace; and
directly south, a crossroads connecting it all. It is all so...so
glorious. And best of all...it is all yours.'''
		self.gargoyle = items.Item(name = "gargoyle", takeable = False)
		self.castletop = l.Forbidden_Location(
							  name = "the castletop",
							  ref = "castletop",
						      stuff = [self.gargoyle, self.boss],
						      adj = (),
						      description = top_descript,
						      num = '$',
						      buried = [],
						      required = self.armor,
						      reason = self.explanation,
						      is_dark = False)

				
		# Template
		'''_descript = \

		
		self.template = l.Location(
							  name = "",
							  ref = "",
						      stuff = [],
						      #adjacent = (self.)
						      adj = (),
						      description = _descript,
						      num = '',
						      buried = [],
						      is_dark = False)'''
		
		
		# Make certain locations adjacent to one another
		self.outside_town.adj = (self.fountain, self.church, self.demense)
		self.outside_town.adjacent = (self.fountain.name, self.church.name,
									  self.demense.name, self.outside_town.name)
		self.fountain.adj = (self.outside_town,)
		self.fountain.adjacent = (self.outside_town.name, self.fountain.name)
		self.church.adj = (self.outside_town, self.crossroads)
		self.church.adjacent = (self.outside_town.name, self.crossroads.name, self.church.name)
		self.market.adj = (self.crossroads,)
		self.market.adjacent = (self.crossroads.name, self.market.name)
		self.crossroads.adj = (self.church, self.market, self.village, self.demense,
							   self.fountain, self.drawbridge)
		self.crossroads.adjacent = (self.market.name, self.church.name, self.village.name,
								 	self.demense.name, self.fountain.name, self.drawbridge.name,
								 	self.crossroads.name)
		self.demense.adj = (self.crossroads, self.outside_town, self.village)
		self.demense.adjacent = (self.crossroads.name, self.outside_town.name, self.village.name)
		self.village.adj = (self.demense, self.crossroads, self.forest)
		self.village.adjacent = (self.demense.name, self.crossroads.name,
								 self.forest.name, self.village.name)
		self.forest.adj = (self.village,)
		self.forest.adjacent = (self.village.name, self.forest.name)
		self.drawbridge.adj = (self.e_wing, self.w_wing)
		self.drawbridge.adjacent = (self.e_wing.name, self.w_wing.name,	self.drawbridge.name)
		self.e_wing.adj = (self.w_wing, self.drawbridge, self.castletop)
		self.e_wing.adjacent = (self.w_wing.name, self.drawbridge.name, self.castletop.name)
		self.w_wing.adj = (self.e_wing, self.drawbridge, self.castletop)
		self.w_wing.adjacent = (self.e_wing.name, self.drawbridge.name, self.castletop.name)
		self.castletop.adj = (self.e_wing, self.w_wing)
		self.castletop.adjacent = (self.e_wing.name, self.w_wing.name)
		
		self.locations = (self.outside_town, self.fountain, self.crossroads,		# certain places
						  self.church, self.market, self.village,					# town places
						  self.forest, self.demense,								# outside places
						  self.drawbridge, self.e_wing, self.w_wing, self.castletop)# castle places
		
		
	def __init__(self):
		self.name = "Castle Map"
		self.helmet = items.Item(name = "helmet", armor = True)
		self.chain_mail = items.Item(name = "chain mail", armor = True)
		self.chestplate = items.Item(name = "chestplate", armor = True)
		self.shield = items.Item(name = "shield", armor = True)
		self.sword = items.Weapon(name = "sword", damage_range = 27, blade = True, long = True, armor = True)
		self.armor = [self.helmet, self.chain_mail, self.chestplate, self.shield, self.sword]
		self.won = False
		self.bonus = []
		for piece in self.armor:
			self.bonus.append(piece)
		self.dragonames = ("raptor", "konquiture")
		self.dragon = items.Dangerous_Animal(name = random.choice(self.dragonames),
									   		 good_food = True,		fryable = True,
							 		 		 alive = True,			deadible = True,
											 min_damage = 5, 		max_damage = 25,
							  				 hostility = 1,			heal_chance = 5)
		self.explanation = "You need a sword, shield, and full armor inside the castle."
		knight_health = random.randrange(9) + 1
		self.boss = Black_Knight(name = "enemy knight",
								location = None,
								health = knight_health * 10,
								defense = 10,
								weapon = "sword",
								inventory = copy.copy(self.armor),
								attack_factor = 5,
								min_power = 10,
								max_power = 35,
								death_causes_victory = True)
		self.boss.cape = items.Item(name = "cape", flammable = True)
		self.boss.belt = items.Item(name = "leather belt")
		self.create_locations()
		kniventory = [self.boss.belt, copy.copy(self.gold_coin), self.boss.cape, copy.copy(items.knife)]
		self.boss.inventory += kniventory
		self.starting = self.outside_town
		self.finishline = self.castletop
		self.boss.location = self.castletop
		#self.tools = [copy.copy(items.knife), copy.copy(items.clothing)]
		self.tools = [copy.copy(items.knife), copy.copy(items.shovel), copy.copy(items.axe)]
		self.suit = items.Item(name = "somebody's swimsuit")
		self.banana = items.Item(name = "banana", edible = True, good_food = True, food = 10)
		self.tronya = items.Item(name = "tronya", edible = True, good_food = True, food = 50)
		self.tribble = items.Item(name = "tribble", alive = True)
		self.manure = items.Item(name = "manure", burnable = True)
		self.deer = items.Item(name = "deer", alive = True, mobile = True, deadible = True, good_food = True, food = 35)
		self.goody =  [copy.copy(items.frog), copy.copy(items.earthworms), self.suit, self.banana, self.tronya,
					   self.tribble, copy.copy(items.penny), self.manure, self.deer, copy.copy(items.rabbit),
					   copy.copy(items.rabbit), copy.copy(items.rabbit), copy.copy(items.rabbit)]
		self.MAX_PINE_TREES = 2
		self.dragon_timer = random.randrange(8)
		self.bonus_timer = random.randrange(4) + 7
		self.goody_timer = random.randrange(7) + 4
		self.wheat_timer = random.randrange(9) + 16
		self.bosstributes = (self.boss.location, self.boss.health, self.boss.defense,
							 self.boss.weapon, self.boss.inventory, self.boss.attack_factor,
							 self.boss.min_power, self.boss.max_power)
		#self.attributes = (self.goody, self.dragon, self.finishline, self.bonus,
		#				   self.bonus_timer, self.goody_timer, self.wheat_timer)
		
	def do_thing(self):
		'''Make changes, like adding stuff to the market and making animals move.'''
		# Check for victory conditions
		if self.won:
			# Do the drawbridge
			self.won = False
			self.drawbridge.adj += (self.crossroads,)
			self.drawbridge.adjacent += (self.crossroads,)
			self.drawbridge.descript = self.bridge_descript_2
			# Do the castletop
			self.castletop.descript = self.top_descript_2
		# Put a bonus item up for sale
		if not self.bonus_timer:
			if self.bonus:
				random.shuffle(self.bonus)
				choice = self.bonus[0]
				self.market.sale.append(choice)
				del self.bonus[0]
				self.bonus_timer = random.randrange(4) + 7
		else:
			self.bonus_timer -= 1
		# Hide a goody somewhere on the map
		if not self.goody_timer and self.goody:
			random.shuffle(self.goody)
			choice = self.goody[0]
			self.goody = self.goody[1:]
			place = random.choice(self.locations)
			if place.stuff:
				place.stuff.append(choice)
			else:
				place.stuff = [choice,]
			self.goody_timer = random.randrange(6) + 5
		else:
			self.goody_timer -= 1
		# Make the dragon move
		alive = None
		if not self.dragon_timer and self.dragon.is_alive:
			for place in self.locations:
				if self.dragon in place.stuff:
					destination = random.choice(place.adj)
					place.stuff.remove(self.dragon)
					destination.stuff.append(self.dragon)
					self.dragon_timer = random.randrange(8)
		else:
			self.dragon_timer -= 1
		# Keep stuff off the drawbridge--and the dragon out of the castle
		if self.drawbridge.stuff:
			for thing in self.drawbridge.stuff:
				self.drawbridge.stuff.remove(thing)
				self.crossroads.stuff.append(thing)
		# Make trees grow
		for plant in self.forest.stuff:
			if plant.name == "pine tree":
				self.forest.stuff.remove(plant)
		for i in range(self.MAX_PINE_TREES):
			self.forest.stuff.append(copy.copy(items.pine_tree))
		random.shuffle(self.forest.stuff)
		# Make wheat grow
		for item in self.demense.buried:
			if "seed" in item.name:
				self.wheat_timer -= 1
				if not self.wheat_timer:
					self.demense.buried.remove(item)
					self.demense.stuff.append(copy.copy(items.wheat))
		# Make the castle dark if there are no torches
		for place in (self.w_wing, self.e_wing):
			for item in place.stuff:
				if item.is_tool:
					if item.is_bright:
						place.is_dark = False
			else:
				place.is_dark = True
		# Bosses already attack in the player's private update method
		# Make the knight move
		if self.boss:
			if not self.boss.stationary:
				for i in range(self.boss.speed):
					location = random.choice(self.boss.location.adj)
					self.boss.location.remove(self.boss)
					self.boss.move(location)
					self.boss.location.append(self.boss)
		else:
			self.won = True

class Black_Knight(items.Boss):
	'''The bad guy for this map'''
	def move(self, location):
		self.location = location
				
if __name__ == "__main__": print "This is a module for a map for Python Adventure Game."