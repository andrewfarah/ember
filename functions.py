def printer(count):
	print("Hi" * count)

printer(5)

# EXAMPLES
# squared(5) would return 25
# squared("2") would return 4
# squared("tim") would return "timtimtim

def squared(num):
    try:
        square = int(num) * int(num)
        return square
    except:
        result = num * len(num)
        return result

squared('andrews')