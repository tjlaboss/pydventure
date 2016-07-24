# Adventure Interface
# Greets the player and selects a map--a sort of "front" for adventure.py


print '''\
\t\a\tWelcome to Python Adventure Game.
You are trapped on the island. The goal is to survive for as long as you can, and eventually escape.
Good luck--you're going to need it.\n\n'''

print "You have maps:"
print "-default"
print "-medieval"
adventure = raw_input("Select a map to play: ")
adventure.lower()

if adventure in ("medieval", "medeival", "medival"):
	import medieval as island
else:
	if adventure != "default":
		#print "Defaulting to Default Island."
		print "Defaulting to Medieval Map"
	#import default as islandFIXME: put it baaack
	import medieval as island

MAP = island.MAP

class Constructor(island.Adventure_Map):
	'''def __init__(self):'''
	'''super(Constructor, self).__init__()
		self.locations = ()
		self.create_locations()'''
	
#if __name__ == "__main__"