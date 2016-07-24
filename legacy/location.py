# Location class module

import random

class Location(object):
	def __init__(self, name, ref, stuff, adj, description, num, buried, is_dark):
		'''You must specify all these values upon instantiating the object.'''
		self.name = name
		self.ref = ref
		self.stuff = stuff
		self.adj = adj
		self.description = description
		self.num = num
		self.buried = buried
		self.is_dark = is_dark
		self.required = None
	def __str__(self):
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
	
class Market(Location):
	'''A special class which you can use to buy and sell.'''
	def __init__(self, name, ref, stuff, adj, description, num, buried,
				 sale, accepted_currency, change_given, wanted, is_dark):
		super(Market, self).__init__(name, ref, stuff, adj, description, num, buried, is_dark)
		self.CURRENCY = accepted_currency
		self.CHANGE = change_given
		self.sale = sale	# stuff to sell
		self.WANTED = wanted# stuff to buy
	def accept_trade(self, player, money, item):
		if money.name in self.CURRENCY:
			player.inventory.remove(money)
			player.inventory.append(item)
			if item in self.sale:		#FIXME: this should always be here, but sometimes it seems not to be!
				self.sale.remove(item)
			print '"Pleasure doing business with you.',
			print 'You are the proud new owner of this', item.name + '".'
		else:
			print money.name.capitalize(), "isn't valid currency in this country."
	def accept_offer(self, player, item):
		if item in player.inventory:
			if item.name in self.WANTED:
				coin = random.choice(self.CHANGE)
				player.inventory.remove(item)
				player.inventory.append(coin)
				self.sale.append(item)
				print "You have sold your", item, "for one", str(coin) + '.'
				print 'Clerk: "...and a bargain."'
			else:
				print '"We have no use for', str(item) + ',', player.name + '".'
		else:
			print "You don't have", item.name + '.'
		
class Forbidden_Location(Location):
	'''A location you can't enter unless you have the "key".'''
	def __init__(self, name, ref, stuff, adj, description, num, buried, required, reason, is_dark):
		super(Forbidden_Location, self).__init__(name, ref, stuff, adj, description, num, buried,
												 is_dark)
		self.required = required
		self.reason = reason
		#self.ready = False	# Always starts out as False
	def check_permit(self, player):
		'''Don't let someone in.'''
		# See if conditions are met
		if len(self.required) > 1:
			count = 0
			for key in self.required:
				if key in player.inventory:
					count += 1
			if count == len(self.required):
				return True, ""
			else:
				return False, self.reason
		else:
			if self.required in player.inventory:
				return True, ""
			else:
				return False, self.reason
				
	
if __name__ == "__main__": print "This is a class for an adventure game location."