# Dictionary module for Python
# ...especially hangman.
# Chooses words from the dictionary and filters out unacceptable ones

import random, string

ALPHABET = string.ascii_lowercase
VOWELS = "aeiouy"
CONSANANTS = "bcdfghjklmnpqrstvwxyz"

def hangword(min_length):
    '''Opens the dictionary and chooses a word for hangman.'''
    try:
        dictionary_file = open("/usr/share/dict/american-english")    # Preferred dictionary
    except IOError:
        print "Error--American English dictionary not found, please specify custom dictionary."
        loc_dict = raw_input("Please enter location of the dictionary to use: ")
        try:
            dictionary_file = open(str(loc_dict))    # Load custom dictionary
        except IOError:
            raise StandardError("Error: No custom dictionary found; aborting attempt.")
    dictionary = dictionary_file.readlines()                # Loads words into a list
    dct = []
    for word in dictionary:
        # filters out stuff that won't work, like proper nouns and possessive cases
        word = word.replace('\n', '')    # get rid of newlines
        if len(word) > int(min_length) and word == word.lower():
            alphabetical = True		# so far
            for letter in word:
                if letter.lower() not in ALPHABET:
			alphabetical = False
            if alphabetical:	# if the word is composed only of the 26 letters
                dct.append(word)# then add it to the words you can use
    dictionary_file.close()
    word = random.choice(dct)            # choose a random word from the acceptable ones
    return word

def randname(length = 6, bypass = False):
    '''Generates random text from a modified alphabet. Quality of word not guaranteed.'''
    # Modified alphabet--more vowels, fewer difficult letters
    acceptable_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z', 'e', 'a', 'i', 'e', 'f', 't', 'o', 'c', 'h', 't', 'e', 'p', 'a']
    random.shuffle(acceptable_letters)
    word = ""
    for letter in range(int(length)):
        word += random.choice(acceptable_letters)
    if bypass:
        return acceptable_letters
    else:
        return word

def aN(word):
    '''Decides whether to use "a" or "an". Very useful.'''
    word.lower()
    # Exceptions to the rule
    con_exceptions = ("hour", "honest", "honor", "honorable", "honesty", "hourly")
    vow_exceptions = ("unit", "use", "urinal", "usable", "united", "union", "utopian")
    try:
        if word in con_exceptions:
            return 'an ' + word
        elif word in vow_exceptions:
            return "a " + word
        elif word[0] in "aeiou8":
            return ("an " + word)
        else:
            return 'a ' + word
    except(IndexError):
        return "nothing"

def sort(word):
	'''A useful function that sorts a given word. __builtin__.sort() only works with lists.'''
	the_word = []
	sorted = ""
	for letter in word:
		the_word.append(letter)
	the_word.sort()
	for letter in the_word:
		sorted += letter
	return sorted

def list_items(list, error_message = "Sorry; there are no valid items in that list."):
	'''Print all the items in a list, with spaces, commas, and 'and'.'''
	# A simple "x and y", no commas
	if len(list) == 2:
		print str(list[0]), "and", str(list[-1])
	# If there's more than one item in the list (and not only 2)
	elif len(list) > 1:
		count = 0
		for entry in list:
			count += 1
			if count < len(list):
				print str(entry) + ',',
			if count == len(list) - 1:
				#print str(entry), "and",
				print "and",
			if count == len(list):
				print str(entry), '\n'	#';'
	elif not list:
		print error_message
	else:
		print list[0]

def madlib_demo():
    '''Makes a simple madlib, for demonstration purposes.'''
    noun = raw_input("Give me a noun: ").lower()
    name = raw_input("Give me a name: ").title()
    verb = raw_input("Give me a verb in its present tense: ").lower()
    adj = raw_input("Give me an adjective: ").lower()
    na = aN(adj)
    print "One day,", na, noun, "was hard at work, when", name, "came along and decided to", verb + '.'


def test():
    lex = hangword(4)

    print "Testing hangman word generator..."
    print "Your random hangman word is", lex + '.'
    
    print "\nTesting random name generator..."
    name = randname(6)
    print "Your randomly generated product name is", name.title() + '!'
    mod_alpha = randname(bypass = True)
    print "The modified alphabet we are using is", mod_alpha
    
    print "\nTesting simple madlib..."
    madlib_demo()
    
if __name__ == "__main__": test()
