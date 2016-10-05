# Finds if a dictionary had items that are in a list.

my_dict = {'apples': 1, 'bananas': 2, 'coconuts': 3}
my_list = ['apples', 'coconuts', 'grapes', 'strawberries']

# You can check for dictionary membership using the
# "key in dict" syntax from lists.

count = 0
result = 0
for i in my_dict:
	print(i)
	if i == my_list[count]:
		print(i + ' is in both!')
		result += 1
	else:
		continue
	count += 1
return(result)
