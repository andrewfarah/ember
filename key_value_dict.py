# Create a function named word_count() that takes a string. 
# Return a dictionary with each word in the string as the key and 
# the number of times it appears as the value.

# E.g. word_count("I am that I am") gets back a dictionary like:
# {'i': 2, 'am': 2, 'that': 1}
# Lowercase the string to make it easier.

# Using .split() on the sentence will give you a list of words.

# In a for loop of that list, you'll have a word that you can
# check for inclusion in the dict (with "if word in dict"-style syntax).
# Or add it to the dict with something like word_dict[word] = 1.

word = 'I am that I am'

def word_count(a_str):
	word_list = word.lower().split(' ')
	word_dict = {}
	
	for w in word_list:
		if w in word_dict:
			word_dict[w] += 1
		else:
			word_dict[w] = 1
	print(word_dict)
	return(word_dict)

word_count(word)