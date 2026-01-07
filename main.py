#today we are going to see whether we can complete all tasks for 
#making a user to play rock paper scissor
import random, pyfiglet, turtle
from turtle import color


userCount = 0; programCount = 0; tied = 0
rps = ["Rock", "Papper", "Sissors"]
emojis_prg = {1: "\U0001f600", 2:"\U0001F606", 3: "\U0001F923"}
# turtle.bgcolor("black")
# turtle.speed(0)
# colors = ["red", "yellow", "blue", "pink", "orange", "cyan", "magenta", "gold"]

# s = turtle.Screen()
# t = turtle.Turtle()

# s.setup(width = 1.0, height = 1.0)

#remove close,minimaze,maximaze buttons:
# canvas = s.getcanvas()
# root = canvas.winfo_toplevel()
# root.overrideredirect(1)

def do_play():
	random.shuffle(rps)
	return rps[0]

def refresh_count():
	global userCount, programCount, tied
	userCount,programCount, tied = 0,0,0

def take_input(userName):
	while True:
		userInput = input(f"Hi, {userName}, Take One in Rock, Papper & Sissors:") if userName else input("Hi User , Take One in Rock, Papper & Sissors:") 
		if userInput not in rps: 
			print(f'Please choose in {rps}')
		elif userInput:
			return userInput

def print_success(userName):
	success_msg = pyfiglet.figlet_format("Congracts!! {}".format(userName), font="slant")
	print(success_msg)

# def move():
#     turtle.penup()
#     x = random.randint(-660, 430)
#     y = random.randint(-300, 130)
#     turtle.goto(x, y)
#     turtle.pendown()

# def move_to(x,y):
#     t.penup()
#     t.goto(x,y)
#     t.pendown()

# def draw_rectangle(a,b):
#     t.forward(a)
#     t.left(90)
#     t.forward(b)
#     t.left(90)
#     t.forward(a)
#     t.left(90)
#     t.forward(b)
#     t.end_fill()
#     t.speed(100)

# def happy():
#     t.color("red")
#     move_to(-500,200)
#     draw_rectangle(10,100)
#     move_to(-490,250)
#     t.left(90)
#     draw_rectangle(80,10)
#     move_to(-410,200)
#     t.left(90)
#     draw_rectangle(10,100)
#     move_to(-380,200)
#     t.left(60)
#     t.color("yellow")
#     draw_rectangle(10,122)
#     move_to(-275,198)
#     t.left(145)
#     draw_rectangle(10,110)
#     move_to(-350,230)
#     t.left(335)
#     draw_rectangle(10,63)
#     move_to(-240,198)
#     t.left(270)
#     t.color("green")
#     draw_rectangle(100,10)
#     move_to(-240,288)
#     draw_rectangle(50,10)
#     move_to(-190,288)
#     draw_rectangle(40,10)
#     move_to(-190,248)
#     draw_rectangle(50,10)
#     move_to(-160,198)
#     t.color("violet")
#     draw_rectangle(100,10)
#     move_to(-160,288)
#     draw_rectangle(50,10)
#     move_to(-110,288)
#     draw_rectangle(40,10)
#     move_to(-110,248)
#     draw_rectangle(50,10)
#     move_to(-80,198)
#     t.left(320)
#     t.color("orange")
#     draw_rectangle(120,10)
#     move_to(-100,295)
#     draw_rectangle(68,10)
#     move_to(-500,80)
#     t.left(40)
#     t.color("red")
#     draw_rectangle(100,10)
#     t.left(180)
#     move_to(-490,70)
#     draw_rectangle(50,10)
#     t.left(90)
#     t.fd(50)
#     t.right(90)
#     draw_rectangle(80,10)
#     t.left(90)
#     t.fd(80)
#     t.left(270)
#     draw_rectangle(50,10)
#     move_to(-400,80)
#     t.left(180)
#     t.color("pink")
#     draw_rectangle(100,10)
#     move_to(-220,70)
#     t.left(60)
#     t.color("brown")
#     draw_rectangle(100,10)
#     t.left(300)
#     move_to(-370,70)
#     t.right(152)
#     draw_rectangle(100,10)
#     t.left(152)
#     move_to(-290,10)
#     t.right(45)
#     draw_rectangle(40,10)
#     t.right(3)
#     draw_rectangle(40,10)
#     move_to(-200,-15)
#     t.left(200)
#     t.color("green")
#     draw_rectangle(10,110)
#     move_to(-95,-20)
#     t.left(145)
#     draw_rectangle(10,114)
#     move_to(-175,25)
#     t.left(333)
#     draw_rectangle(10,63)
#     move_to(-70,79)
#     t.left(90)
#     t.color("blue")
#     draw_rectangle(101,10)
#     move_to(-60,-22)
#     t.left(180)
#     draw_rectangle(80,10)
#     move_to(50,-22)
#     t.left(180)
#     t.color("Green")
#     draw_rectangle(100,10)
#     move_to(300,150)
#     t.color("red")



userName = input("Hi! May i know your name?")




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
			print(f'Computer:Yes, You won. Let"s play again i ll win this time.')
		elif ProgrammGuess == "Sissors" and userInput == "Rock":
			userCount += 1
			print(f'Computer:Yes, You won. You know what time it is payback time.')
		else:
			programCount += 1
			print(f'Computer: {emojis_prg[programCount]} Sorry! You lost ')
		if userCount + programCount+tied == 3:
			if userCount > programCount and userCount > tied:
				print(f'{userName} Won')
				# happy() #eventthough user won we are not asking him that he wanted to play again so need to add it
				print_success(userName)
				break
			else:
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
	print('')