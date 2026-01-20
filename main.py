import random, pyfiglet

userCount = 0; programCount = 0; tied = 0
rps = ["Rock", "Papper", "Sissors"]
emojis_prg = {
    1: "\U0001f600", 
    2:"\U0001F606", 
    3: "\U0001F923", 
    "claps": "\U0001F44F"}
computer_messages = {
    1: 'Let"s play again i"ll win this time.',
    2: "Yeah... Yeah.....You Won. You know what time it is payback time.", 
    3: "Suck..! come back, let's play again"
}

def do_play():
    return random.choice(rps)

def refresh_count():
    global userCount, programCount, tied
    userCount, programCount, tied = 0, 0, 0

def take_input(userName):
    try:
        while True:
            name = userName if userName else "User"
            userInput = input(f"Hi {name}, Take One in Rock, Papper & Sissors: ").strip()
            formattedInput = userInput.capitalize()
            if formattedInput not in rps: 
                print(f'Please choose in {rps}')
            else:
                return formattedInput
    except KeyboardInterrupt:
        print(f'Pleaseeee come back!!!')
        return None

def print_success(userName):
    success_msg = pyfiglet.figlet_format("Congrats!! {}".format(userName), font="slant")
    print(success_msg)

userName = input("Hi! May i know your name: ")

try:
    while True:
        userInput = take_input(userName)
        if not userInput: 
            break
        ProgrammGuess = do_play()
        if ProgrammGuess == userInput:
            tied += 1
            print(f"You both chose {ProgrammGuess}, It's a tie")
        elif (ProgrammGuess == "Rock" and userInput == "Papper") or \
             (ProgrammGuess == "Papper" and userInput == "Sissors") or \
             (ProgrammGuess == "Sissors" and userInput == "Rock"):
            userCount += 1
            print(f'Computer chose: {ProgrammGuess}, You won {emojis_prg["claps"]}')
            msg_idx = userCount if userCount in computer_messages else 1
            print(f'Computer: {computer_messages[msg_idx]}')
        else:
            programCount += 1
            msg_idx = programCount if programCount in emojis_prg else 1
            print(f'Computer: {emojis_prg[msg_idx]} Sorry! You lost this round.')

        if (userCount + programCount + tied) == 3:
            print(f'\nEvaluating results.....................')
            if userCount > programCount:
                print(f'{userName} Won')
                print(f'{userName}: {userCount}    Computer: {programCount}')
                print_success(userName)
                break
            elif userCount == programCount:
                print(f"It's a tie, {userName}")
            else:
                print(f'Sorry! {userName} You lost:')
            try_again = input('Want to try again? (y/n): ').lower()
            if try_again in ["yes", "y", "YES", "Y"]:
                refresh_count()
                continue
            else:
                print(f'Please come again to play! {emojis_prg[1]}')
                break
        
except KeyboardInterrupt:
    print(f'\nPleaseeee come back!!!')
except Exception as e:
    print(f'Error Occured: {e}')