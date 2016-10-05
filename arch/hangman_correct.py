import os
import random

# make a list of words

words = [
	'apple',
	'banana',
	'orange',
	'strawberry',
	'lime',
	'grapefruit',
	'coconut',
	'kumquat',
	'blueberry',
	'melon'
]

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def draw(bad_guesses, good_guesses, secret_word):
# draw spaces
	clear()

	for letter in bad_guesses:
		print(letter, end='')
		print('\n\n')

	for letter in secret_word:
		if letter in good_guesses:
			print(letter, end='')
		else:
			print('_', end='')

	print('')
	print('Strikes: {}/7'.format(len(bad_guesses)))
	print('')

def get_guess(bad_guesses, good_guesses):
	while True

		guess = input("Guess a letter: ").lower()
			
		if len(guess) != 1 and not guess.isalpha():
			print('You can only guess single letters!')
		elif guess in bad_guesses or guess in good_guesses:
			print('You\'ve already guessed \'{}\'').format(guess)
		else:
			return guess

def play(done):
	clear()
	secret_word = random.choice(words)
	bad_guesses = []
	good_guesses = []

	while True:
		draw(bad_guesses, good_guesses,  secret_word)
		guess = in secret_word

while True:
	start = input("Press enter/return to start, or Q to quit: ")
	if start.lower() == 'q':
		break

	# pick a random work
	secret_word = random.choice(words)
	bad_guesses = []
	good_guesses = []

	while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
		

		# take guess
		

	else:
		print('You didn\'t get it!')