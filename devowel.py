# take a list of vowels
# take a list of words
# remove vowels
# return word list de-vowel-ed
# capitalize the first letter of each word


vowel_list = ['a', 'e', 'i', 'o', 'u']
word_list = ['andrew', 'dori', 'margaret', 'joseph', 'michal', 'dovid austin']
count = 0

for word in word_list:
	char_word = list(word)	
	while count < len(vowel_list):
		try:
			if vowel_list[count] in char_word:
				char_word.remove(vowel_list[count])
			else:
				count += 1
		except ValueError:
			continue
	result = ''.join(char_word)
	print(result.capitalize())
	count = 0