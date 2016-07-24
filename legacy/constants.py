# A module with all the mathematical (and some other) constants used in Python Adventure Game.
# 9/03/11--LOL, look at the comment I used to have! Everything that is not a constant has been moved into items.py
#
# Basically, a huge module stocked with all flavors of constants for the
# adventure game. Also contains a useful class or two.

import random
import items, words, copy

''' Some foods
good_foods = ("wheat", "dead fish", "seeds", "coconut", "dead fish") + ("chicken", "potato", \
			  "apple", "corn", "dead boar", "dead konquiture", "dead raptor", "banana", "dead bear", "dead deer", \
			  "trail mix", "egg", "MRE", "chocolate bar", "tronya")
gross_foods = ("earthworms", "dead snake") + ("bug", "frog", "dead skunk", "dead monkey",\
											  "dead rabbit", "dead tribble")
foods = good_foods + gross_foods
# Fry some food
UNFRYABLE  = ("banana", "trail mix", "MRE", "tronya", "chocolate bar", "dead skunk", "dead monkey",\
			  "dead tribble", "wheat", "seeds")
good_fried_foods = ()
gross_fried_foods = ()
for food in foods:
	if food not in UNFRYABLE:
		foood = food[:]
		if "dead" in food:
			food = "fried" + food[4:]
		else:
			food = "fried " + food
		if foood in good_foods:
			good_fried_foods += (food,)
		else:
			gross_fried_foods += (food,)
			
GOOD_FOODS = good_foods + good_fried_foods
GROSS_FOODS = gross_foods + gross_fried_foods
FRIED_FOODS = good_fried_foods + gross_fried_foods
FOODS = GOOD_FOODS + GROSS_FOODS


# Tools and weapons
UTENSILS = ("knife", "frying pan")
CUTTERS = ("knife", "axe")

MAKESHIFT = ("snake",) + UTENSILS
LONG_WEAPONS = ("axe", "shovel", "sword")
BLADED_WEAPONS = ("axe", "knife", "sword")
GUNS = ("shotgun", "pistol", "rifle")
WEAPONS = MAKESHIFT + LONG_WEAPONS + GUNS
REAL_WEAPONS = GUNS + BLADED_WEAPONS

hostile = ("snake", "rat", "gila monster", "monkey", "skunk")
DANGEROUS = ("yeti", "bear", "boar", "sasquatch", "cougar", "panther", "raptor", "konquiture")
for animal in DANGEROUS:
	animal = "wounded " + animal
	hostile += (animal,)
HOSTILE = hostile
PEACEFUL = ("tribble", "bug", "frog", "rabbit", "deer")
MEAN_ANIMALS = HOSTILE + DANGEROUS
ANIMALS = MEAN_ANIMALS + PEACEFUL
VENEMOUS = ("konquiture", "gila monster", "monkey", "snake", "bug")

GOODIES = ("first aid kit", "frying pan")
WOOD = ("tree", "palm tree", "Christmas tree", "pine tree", "log")
FLAMMABLE = ("torch", "clothing", "towel", "candle")
LIGHTS = ("flashlight", "lit candle", "lit torch", "lit clothing")
FIRESTARTERS = ("lighter", "lit candle", "lit torch", "match", "matches")
ARMOR = ["helmet", "chain mail", "chestplate", "shield", "sword"]

STUFF = WEAPONS + ANIMALS + GOODIES + WOOD + FLAMMABLE
bonus = random.choice(STUFF)

UNTAKEABLES = ("fire", "water") + DANGEROUS'''

SYMBOLS = "~!@#$%^&*()_+=-[];',./<>?:{}|\\\n "
TRUEFALSE = (True, False)

# Factors
COMBAT_DAMAGE_FACTOR = 38			# default 27
DAMAGE_REDUCTION_FACTOR = 2			# default 2
HOSTILE_CREATURE_DAMAGE = 25		# default 25
HUNGER_INCREASE_FACTOR = 5			# default 5
STARVATION_DEDUCTION = 8			# default 8
HEALTH_BONUS_FACTOR = 5				# default 5
FEELING_BETTER_FACTOR = 4			# default 4
FIRE_SPREADING_CHANCE = 14			# default 16
FRIED_FOOD_BONUS = 5				# default 5
