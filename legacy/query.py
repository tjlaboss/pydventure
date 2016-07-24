# Questions
# Demonstrates module creation

class Player(object):
	'''A player for a game.'''
	def __init__(self, name, score = 0):
		self.name = name
		self.score = score

	def __str__(self):
		rep = self.name + ':\t\t' + str(self.score)
		return rep

def ask_yes_or_no(question):
	'''Ask a yes or no question.'''
	response = None
	POS_CHOICES = ('y', "yes", "yeah", "sure", "of course", "la", "true", 't')
	NEG_CHOICES = ('n', "no", "nope", "never", "no way", "wah", "false", 'f')
	CHOICES = POS_CHOICES + NEG_CHOICES

	while response not in CHOICES:
		response = raw_input(question).lower().strip()
	if response in NEG_CHOICES:
		response = False
	else:
		response = True
	return response

def ask_for_a_number(question, low, high):
	'''Ask for a number within a given range.'''
	response = None
	while response not in range(low, high):
		try:
			response = int(raw_input(question))
		except(ValueError):
			pass
	return response



# main
if __name__ == "__main__":
	print "You ran this module directly (and did not import it)."
	raw_input("\n\nPress the enter key to exit. ")