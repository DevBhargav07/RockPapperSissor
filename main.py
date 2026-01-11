#still we didn't finished the count of times next time the user is trying to use the rockpapper sissors only 2 tries are coming.
import random, pyfiglet


userCount = 0; programCount = 0; tied = 0
rps = ["Rock", "Papper", "Sissors"]
emojis_prg = {1: "\U0001f600", 2:"\U0001F606", 3: "\U0001F923", "claps": "\U0001F44F"}
computer_messages = {1: 'Let"s play again i"ll win this time.',2 : "Yeah... Yeah.....You Won.You know what time it is payback time.", 3: f"Suck...! Oops You lost..{emojis_prg[3]}"}

def do_play():
	random.shuffle(rps)
	return rps[0]

def refresh_count():
	global userCount, programCount, tied
	userCount,programCount, tied = 0, 0, 0

def take_input(userName):
	try:
		while True:
			if not userName: userName="User"
			userInput = input(f"Hi {userName}, Take One in Rock, Papper & Sissors: ").strip()
			formattedInput = userInput.capitalize()
			if formattedInput not in rps: 
				print(f'Please choose in {rps}')
			else:
				return formattedInput
	except KeyboardInterrupt:
		print(f'Pleaseeee come back!!!')
		return None

def print_success(userName):
	success_msg = pyfiglet.figlet_format("Congracts!! {}".format(userName), font="slant")
	print(success_msg)

userName = input("Hi! May i know your name: ")

try:
	while True:
		userInput = take_input(userName)
		if not userInput: break
		ProgrammGuess = do_play()
		if ProgrammGuess== userInput:
			tied += 1
			print(f"You both choose the {ProgrammGuess}, It's a tie")
		elif (ProgrammGuess == "Rock" and userInput == "Papper") or \
			(ProgrammGuess == "Papper" and userInput == "Sissors") or \
			(ProgrammGuess == "Sissors" and userInput == "Rock") :
			userCount += 1
			print(f'Computer choose: {ProgrammGuess}, You won {emojis_prg["claps"]}')
			print()
			print(f'Computer: {computer_messages[programCount]}')
		else:
			programCount += 1
			print(f'Computer: {emojis_prg[programCount]} Sorry! You lost ')
		if userCount + programCount+tied == 3:
			print(f'Evaluating results')
			print('.....................')
			if userCount > programCount and userCount > tied:
				print(f'{userName} Won')
				print_success(userName)
				break
			else:
				print(f'Sorry! {userName} You lost:')
				try_again = input('Want to try again?:')
				if try_again in ["yes", "YES", "Yes", "y","Y"]:
					refresh_count()
					print(f'usercount: {userCount}, programcount: {programCount}, tied count: {tied}')
					continue
				else:
					print(f'Please come again to play! {emojis_prg[1]}')
					break
		take_input(userName)
except KeyboardInterrupt:
	print(f'Pleaseeee come back!!!')

except Exception as e:
	print(f'Error Occured: {e}')