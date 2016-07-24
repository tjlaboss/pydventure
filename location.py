# Module for Pydventure containing the classes Location and

import random

class Location(object):
	'''A place that the Adventurer can go to and pick up items from.
	
	Parameters:
		name:			string; long name of the location
		key:			string; short, unique name of the location
		stuff:			dictionary of Item objects (things present at the location)
		adjacent:		dictionary of Location objects that the player can reach from self
		description:	string; fun, descriptive text about the location
		marker:			string of 1 character; marker on the level's map
		is_dark:  		Boolean; whether it's possible to see here without a light
		buried:			dictionary of Item objects buried in the ground
	
	'''
	def __init__(self, name, key, stuff, adj, description, num, buried, is_dark):
		'''You must specify all these values upon instantiating the object.'''
		self.name = name
		self.key = key
		self.stuff = stuff
		self.adjacent = adjacent
		self.description = description
		self.num = num
		self.buried = buried
		self.is_dark = is_dark
		self.required = None
		
		
	def __str__(self):
		return self.name	
	
	def report(self):
		rep = self.name.capitalize()
		rep += '\n' + self.description
		if self.stuff:
			rep += "\nYou can see "
			for thing in self.stuff:
				rep += str(thing) + ', '
		else:
			rep += "\nThere are no useful objects "
		rep += "lying around."
		rep += "\nYou can access the following locations: "
		count = 0
		for place in self.adjacent:
			if count != len(self.adjacent) - 1:
				rep += str(place) + ', '#.name + ', '
				if count > 4:
					rep += '\n'
			else:
				p = place
			count += 1
		rep += "and " + p + '.'
		return rep







