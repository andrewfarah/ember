# Handy functions:
# .upper() - uppercases a string
# .lower() - lowercases a string
# .title() - titlecases a string
# There is no function to reverse a string.
# Maybe you can do it with a slice? 

def stringcases(a_str):
	result = a_str.upper(), a_str.lower(), a_str.title(), a_str[::-1]
	print(result)
	return(result)

word = 'woop'
stringcases(word)