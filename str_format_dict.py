dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]
string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(a_list_dicts, a_str):
	count = 0
	temp_list = []
	for d in a_list_dicts:
		temp_dict = a_list_dicts[count]
		result = a_str.format(name = temp_dict['name'], food = temp_dict['food'])

		temp_list.append(result)
		print(temp_list)

		count += 1

	return(temp_list)

string_factory(dicts, string)

# Create a function named string_factory that accepts a list of dictionaries and a string. 

# Return a new list build by using .format() on the string, filled in by each 
# of the dictionaries in the list.


# def string_factory(a_list_dicts, a_str):


# string_factory()