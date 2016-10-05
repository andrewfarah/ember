# Create a function named combo() that takes two iterables and returns a 
# list of tuples. Each tuple should hold the first item in each list, then 
# the second set, then the third, and so on. Assume the iterables will be the same length.

# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]
# If you use .append(), you'll want to pass it a tuple of new values.

# combo([1, 2, 3], 'abc')

# def combo(item_a, item_b):
# 	result = []
# 	new_tuple = ()
# 	num = 0
# 	new_list = list(item_b[0])

# 	for i in item_a:
# 		try:
# 			new_tuple = i, new_list[num]
# 			result.append(new_tuple)
# 			num += 1
# 		except:
# 			continue

# 	# print(new_list)
# 	print(result)
# 	return(result)
# combo([1, 2, 3], ['abc'])


def combo(x, y):
  myList = list()
  for z in range(len(x)):
    myList.append((x[z], y[z]))
  return myList

combo([1, 2, 3], 'abc')


# def combo(item_a, item_b):
# 	result = []
# 	new_tuple = ()
# 	for i, b in item_a, item_b:
# 		new_tuple = i, b
# 		result.append(new_tuple)
# 	print(result)
# combo([1, 2, 3], ['abc'])