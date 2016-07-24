# Simple Adventure Game
# 
#
# A simple adventure game using object-oriented programming. The player can collect
# items and travel between various connected locations

import time, random
import adventurer, items, location


def get_keys(dictionary):
	'''Sometimes it can be hard to refer to the right item or location.
	This function is intended to print out the name and key key for each entry
	in player.inventory, player.location.stuff, or player.location.adjacent.
	
	Returns a string of the name-key pairs for the dictionary of objects. 
	'''
	
	namekeys = ""
	for entry in dictionary:
		namekeys += entry.name + '\t' + entry.key + '\n'
	return namekeys




if __name__ == "__main__":
	print "Main"
