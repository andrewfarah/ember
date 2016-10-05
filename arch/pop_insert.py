the_list = ["a", 2, 3, 1, False, [1, 2, 3]]

# Your code goes below here
the_list.insert(0, the_list.pop(3))

indices = 1, 4, 5
for i in sorted(indices, reverse=True):
	del the_list[i]

print(the_list)
the_list.extend(range(4,21))
print(the_list)