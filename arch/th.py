import random

def nchoices(a_iter, a_int):
	count = 0
	ressult_list = []
	while a_int > count:
		ressult_list.append(random.choice(a_iter))	
		count += 1
	return(ressult_list)


my_list = [1, 2, 3, 4, 5, 67, 8]
nchoices(my_list, 3)