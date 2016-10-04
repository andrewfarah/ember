# E.g. word_count("I am that I am") gets back a dictionary like:
# {'i': 2, 'am': 2, 'that': 1}
# Lowercase the string to make it easier.
# Using .split() on the sentence will give you a list of words.

# In a for loop of that list, you'll have a word that you can
# check for inclusion in the dict (with "if word in dict"-style syntax).
# Or add it to the dict with something like word_dict[word] = 1.



def word_count(a_sen):
	a_sen.lower()
	word_list = a_sen.lower().split(' ')
	count = 0
	a_dict = dict((k,count) for k in word_list)
	# print(word_list)
	for k in word_list:
		if k in a_dict:
			a_dict[k] = a_dict[k] + 1 
	# print(a_dict)
	return(a_dict)

word_count("I opened a store named I and I would really like to name it me")