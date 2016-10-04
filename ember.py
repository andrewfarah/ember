# import twilio
from twilio.rest import TwilioRestClient

account_sid = "ACc16b75896fa3e50970c248c2571fadd2" # Your Account SID from www.twilio.com/console
auth_token  = "9e88494a995b3c1d2e3550b92e0bd4f4"  # Your Auth Token from www.twilio.com/console
client = TwilioRestClient(account_sid, auth_token)

# data stores
contacts_list2 = {('Louderback', 75), ('Triest', 82), ('Black', 90), ('Indy', 7), ('Dori', 30), ('Mom', 6)}
contacts_list = ['Louderback', 'Triest', 'Black', 'Andrew', 'Dori', 'Mom', 'Indy']
days_until_list = ['10', '12', '34', '25', '75', '4', '1']
command_list = ['› help = Show command list', '› show = Show all contacts', '› edit = Edit a contact', '› q = Quit Ember']

# functions for showing contacts list
def show(count):
	print("\nCurrent contacts:")
	print(contacts_list2)
	# print(sorted_contacts_list = sorted(contacts_list2, key=lambda item: item[2]))
	# for contact in sorted_contacts_list:
	# 	print(contact)
	# 	message = client.messages.create(body=contact,
	#     to="+17038872869",    # Replace with your phone number
	#     from_="+12403485098") # Replace with your Twilio number
	# 	print(message.sid)

def show_next():
	count = 1
	days_until_list.sort()
	print(days_until_list)

def notify_text(text):
	print("\n>>>>>>>>>>>>>>>>>>>>> " + text + " <<<<<<<<<<<<<<<<<<<<<")

def edit_name(current_contact):
	while True:
		show(1)
		# edit the contact
		try:
			contact_list_index = int(input("\nType the record number of the contact you'd like to update: \n› "))
		except ValueError:
			notify_text('Sorry, numbers only!')
		else:
			print("\nEditing: " + contacts_list[contact_list_index - 1])
			updated_contact = contacts_list[contact_list_index - 1]
			try:
				updated_days = int(input("\nRemind you in how many days? {}."
										 	"\nType '-1' if no change? \n› ".format(updated_contact)))
			except ValueError:
				notify_text("Numbers only please.")
			if updated_days == -1:
				print("Okay, {}'s' reminder will remain as {}".format(updated_contact, days_until_list[contact_list_index-1]))
				start()
			else:
				days_until_list[contact_list_index - 1] = updated_days
				print("Success! I'll remind you to contact {} in {} days.".format(updated_contact, updated_days))
				start()

def add_days(current_contact):
	while True:
		count = 1
		try:
			days = int(input("\nHow many days from now would you like to be reminded to contact {}? \n› ".format(current_contact)))
		except ValueError:
			notify_text("Numbers only please.")
		else:			
			days_until_list.append(days)
			print("Success! I'll remind you to contact {} in {} days.".format(current_contact, days))
			start()

def help():
	print("\nWelcome to Ember. Commands:")
	for command in command_list:
		print(command)

def add(contact):
	contacts_list.append(contact)
	print("Success! {} has been added. You have {} contacts.".format(contact, len(contacts_list)))
	add_days(contact)
	

# start app
help()

def start():
	while True:
		current_contact = input("\nAdd a new contact: \n› ")
		# enter the word DONE - in all caps - to qui the program
		if current_contact == 'q':
			break
		
		# show me all contacts
		elif current_contact == 'show':
			show(1)
			continue

		# edit contacts
		elif current_contact == 'edit':
			edit_name(current_contact)

		elif current_contact == 'next':
			show_next()

		# help
		elif current_contact == 'help':
			help()
			continue
		add(current_contact)

	# Put new people into the list, one at a time

start()

# NOTES
# find the index of an object in a list -- print(days_until_list.index('34'))


# AN ATTEMPT AT GLOBAL NAVIGATION
# def check_input(input_word):
# 	while True:
# 		if input_word == 'q':
# 			break
		
# 		# show me all contacts
# 		elif input_word == 'show':
# 			show(1)
# 			continue

# 		# edit contacts
# 		elif input_word == 'edit':
# 			edit_name(current_contact)

# 		# help
# 		elif input_word == 'help':
# 			help()
# 			continue
# 	start()
