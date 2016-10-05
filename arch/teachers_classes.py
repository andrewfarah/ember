
# Create a function named most_classes that takes a dictionary of teachers. Each key is a 
# teacher's name and their value is a list of classes they've taught. most_classes should
# return the teacher with the most classes.


# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.

# Now, create a function named stats that takes the teacher dictionary. Return a list of 
# lists in the format [<teacher name>, <number of classes>]. For example, one item in the 
# list would be ['Dave McFarland', 1].

# Great work! Finally, write a function named courses that takes the teachers dictionary. 
# It should return a single list of all of the courses offered by all of the teachers.


class_dict = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
			 'Kenneth Love': ['Python Basics', 'Python Collections']}
	
def most_classes(a_dict):
	max_count = 0
	for key in a_dict:
		if len(a_dict[key]) > max_count:
			max_count = len(a_dict[key])
			name = key
	print(name)
	return(name)

def num_teachers(a_dict):
	num = 0
	for key in a_dict:
		num += 1
	print(num)
	return(num)

def stats(a_dict):
	num_classes = 0
	temp_list = []
	for key in a_dict:
		temp_list.append([key, len(a_dict[key])])
	print(temp_list)
	return(temp_list)

def courses(a_dict):
	result = []
	for value in a_dict.values():
		result.extend(value)
	print(result)

most_classes(class_dict)
num_teachers(class_dict)
stats(class_dict)
courses(class_dict)

