#still we didn't finished the count of times next time the user is trying to use the rockpapper sissors only 2 tries are coming.
import random, pyfiglet, time


userCount = 0; programCount = 0; tied = 0
rps = ["Rock", "Papper", "Sissors"]
emojis_prg = {1: "\U0001f600", 2:"\U0001F606", 3: "\U0001F923"}

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
			userInput = input(f"Hi {userName}, Take One in Rock, Papper & Sissors: ") 
			userInput = userInput.strip(' ')
			if userInput not in rps: 
				print(f'Please choose in {rps}')
			elif userInput:
				return userInput
	
	except KeyboardInterrupt:
		print(f'Pleaseeee come back!!!')

def print_success(userName):
	success_msg = pyfiglet.figlet_format("Congracts!! {}".format(userName), font="slant")
	print(success_msg)

userName = input("Hi! May i know your name: ")
userInput = take_input(userName)

try:
	while userCount+programCount+tied <= 3:
		ProgrammGuess = do_play()
		if ProgrammGuess.lower() == userInput.lower():
			tied += 1
			print(f'You both choose the same!')
		elif ProgrammGuess == "Rock" and userInput == "Papper":
			userCount += 1
			print(f'Computer: Yeah i know its Best Of three right')
		elif ProgrammGuess == "Papper" and userInput == "Sissors":
			userCount += 1
			print(f'Computer:Yes, You won. Let"s play again i"ll win this time.')
		elif ProgrammGuess == "Sissors" and userInput == "Rock":
			userCount += 1
			print(f'Computer:Yes, You won. You know what time it is payback time.')
		else:
			programCount += 1
			print(f'Computer: {emojis_prg[programCount]} Sorry! You lost ')
		if userCount + programCount+tied == 3:
			print(f'Evaluating results')
			print('.....................')
			time.sleep(2)
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