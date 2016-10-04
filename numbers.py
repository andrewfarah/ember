import random

def game():
	# gen a random number btw 1 and 10
	secret_num = random.randint(1, 10)
	guesses_left = 5

	while True:
		# non-integar catch
		try:
			# get a num from a player
			guess = int(input("Guess a number between 1 and 10:  "))
		except ValueError:
			print("Sorry. Integers only, please.")
		else:
			# compare num to random number
			if guesses_left == 0:
				print("Game Over! You have {} guesses left".format(guesses_left))

				# let people play again
				start_over = str(input("Would you like to try again? Y or N? ")).lower()

				if start_over == "n":
					print("Game over!")
					break
				elif start_over == "y":
					print("Let's do this. You've got 5 more guesses!")
					guesses_left += 5

			elif guess != secret_num:
				print("Try again. You have {} guesses left".format(guesses_left))
				guesses_left -= 1

				# print "too low" or too high for bad guesses
				if guess < secret_num:
					print("Higher..")
				else:
					print("Lower..")
				
				continue
			elif guess == secret_num:
				print("Yes! {} is correct!".format(guess))
				start_over = str(input("Would you like to play again? Y or N? ")).lower()

				if start_over == "n":
					print("Game over!")
					break
				elif start_over == "y":
					print("Let's do this. You've got 5 more guesses!")
					guesses_left = 5

game()