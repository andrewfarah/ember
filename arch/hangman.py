

import random

def game():
	word_bank = ['andrew', 'dori', 'dave', 'dad', 'indy', 'mom']

# print(rand_num)
	game_word = word_bank[random.randint(0, len(word_bank)-1)]
	print(game_word)
	guess_list = []
	correct_guesses = []
	result_list = []
	game_word_letters = list(game_word)
	result_list = [len(game_word_letters) * '_ ']
	print(' '.join(result_list))

	while True:
		
	# draw spaces
	# take guess
	# draw guessed letters and strikes
	# print out win/lose
		try:
			player_guess = input("Hangman. Guess a letter: ")
		except ValueError:
			print("Sorry, text only.")
		result_list = ['' or '_' if char != player_guess else player_guess for char in game_word_letters]
		print(' '.join(result_list))


		

		guess_list.append(player_guess)
		
	
game()