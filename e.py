# IMPORTS
from twilio.rest import TwilioRestClient
import datetime

# CREDS
account_sid = "ACc16b75896fa3e50970c248c2571fadd2" # Your Account SID from www.twilio.com/console
auth_token  = "9e88494a995b3c1d2e3550b92e0bd4f4"  # Your Auth Token from www.twilio.com/console
client = TwilioRestClient(account_sid, auth_token)

# LIST OF NAMES
con_list = [('Louderback', datetime.date(2016, 11, 1)), ('Triest', datetime.date(2016, 10, 15))]
			# ('Black', datetime.date(2016, 10, 20)), ('Indy', datetime.date(2016, 12, 25)),
			# ('Dori', datetime.date(2016, 10, 1)), ('Mom', datetime.date(2017, 1, 18))]

today = datetime.date.today() # gets today in M / D / Y format
sorted_cons = sorted(con_list, key=lambda n: n[1]) # sorts list by date (nearest first)
# con_dict = dict(con_list)

# ISSUE 'SHOW' COMMAND FROM A TEXT
def next(name):
	if name == 'next':
		for con, days in sorted_cons:
			print(days, con)
			break
			if days	== '%c':
				print('Time to reach out to:', con)
				# message = client.messages.create(body="You need to reach out to: " + str(con),
				# to="+17038872869",    # Replace with your phone number
				# from_="+12403485098") # Replace with your Twilio number
				break
		start()

def show():
	for con, days in sorted_cons:
		if (days - today).days < 1:
			print('Call {} today'.format(con))
		else:
			print('Call {} in {} days '.format(con, (days - today).days))

def edit(name):
	name = name.capitalize()
	print(name)
	editing = [i for i, v in enumerate(con_list) if v[0] == name]
	print(editing)
	new_days = int(input("\nHow many days?\n› "))
	del con_list[name]
	con_list.update(name, datetime.timedelta(new_days + today))
	print(con_list)
	
def add(name):
	name = name.capitalize()
	reminder = input('\nRemind you about {} in how many days?: \n› '.format(name))
	con_list.append((name, (today + datetime.timedelta(days=int(reminder)))))
	print(con_list)
	return(con_list)

def start():
	while True:
		command = input("\nCommand: \n› ")
		if command == 'next': # run NEXT function
			next(command)
			continue

		if command == 'show': # run SHOW function
			show()
			continue
		
		if command == 'edit':
			show()
			name = input("\nWhich contact? \n› ").lower()			
			edit(name)
			continue

		if command == 'q':
			break

		else:
			confirm = input('\nAre you sure you want to add {}? y/n \n› '.format(command)).lower()
			if confirm == 'y':
				add(command)
			else:
				break


start()