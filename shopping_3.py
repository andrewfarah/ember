contacts = []

def show_help():
	print("\nSeparate each item with a comma, please. ")
	print("Type DONE to quit. SHOW to see the current list, and HELP to get this message.")
	
def show_contacts():
	count = 1
	for contact in contacts:
		print("{}: {}".format(count, contact))
		count += 1
		 
