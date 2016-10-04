# import random

# start = 5
# def even_odd(num):
# 	# If % 2 is 0, the number is even.
# 	# Since 0 is falsey, we have to invert it with not.
# 	return not num % 2

# while start > 0:
# 	rand_num = random.randint(1, 99)
# 	if rand_num % 2 == 0:
#  		print("{} is even".format(rand_num))
# 	else:
# 		print("{} is odd".format(rand_num))
# 	start -= 1

# contacts_list = ['Louderback', 'Triest', 'Black', 'Andrew', 'Dori', 'Mom', 'Indy']
# days_until_list = ['10', '12', '34', '25', '75', '4', '1']
# command_list = ['› help = Show command list', '› show = Show all contacts', '› edit = Edit a contact', '› q = Quit Ember']

# contacts_list = [('Louderback', 1, 75), ('Triest', 2, 82), ('Black', 3, 90), ('Indy', 4, 7), ('Dori', 5, 30), ('Mom', 6, 6)]
# for name, record, days in contacts_list:
# 	print(str(record) + '. ' + name + ' -- ' + str(days) + ' days')



# p._fields

# for x, y, days in contacts_list:
# 	print(str(days) + ' days')


# # regular unsorted dictionary
# >>> d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# >>> # dictionary sorted by key
# >>> OrderedDict(sorted(d.items(), key=lambda t: t[0]))
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

# >>> # dictionary sorted by value
# >>> OrderedDict(sorted(d.items(), key=lambda t: t[1]))
# OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])

number = int(input("go › "))

if number is False:
	print("nice")

else:
	print("Nope")