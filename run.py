# Import the modules
import time
from pyfiglet import figlet_format
from termcolor import colored

# Import a styling logo name from Ascii Art Generator

print(' ▄▄▄▄    ▒█████   ▒█████   ██ ▄█▀     ▄████  ▄▄▄       ███▄ ▄███▓▓███')
print('▓█████▄ ▒██▒  ██▒▒██▒  ██▒ ██▄█▒     ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█  ')
print('▒██▒ ▄██▒██░  ██▒▒██░  ██▒▓███▄░    ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███')
print('▒██░█▀  ▒██   ██░▒██   ██░▓██ █▄    ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ')
print('░▓█  ▀█▓░ ████▓▒░░ ████▓▒░▒██▒ █▄   ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒███')
print('░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒    ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░')

while True:
    # BOOK GAME OPENS IN 5s
    print(colored('\nThe BOOK GAME starts in 5s...', attrs=['bold']))
    opening_time = 5
    while opening_time > 0:
        m, s = divmod(opening_time, 5)
        time_left = str(m).zfill(2) + ':' + str(s).zfill(2)
        print(time_left + '\r', end='')
        time.sleep(1)
        opening_time -= 1
    break


class Data:
    """
    Data Class
    Get player data
    use of these data throughout the book game
    """
    def __init__(self):
        self.player_name = ''
        self.child_name = ''
        self.book_choice = ''
        self.book_decision = ''

    # Set player name
    def setPlayerName(self, player_name):
        self.player_name = player_name

    # Set child name
    def setChildName(self, child_name):
        self.child_name = child_name

    # Set book choice
    def setBookChoice(self, book_choice):
        self.book_choice = book_choice

    # Set book decision
    def setBookDecision(self, book_decision):
        self.book_decision = book_decision


current_user = Data()


def welcome():
    """
    Welcome and get player name
    """
    time.sleep(2)
    # Style the welcome message
    welcome_art = figlet_format(f"Welcome {current_user.player_name}",
                                font='slant')
    colored_art = colored(welcome_art, 'cyan', attrs=['bold'])
    print(colored_art)
    time.sleep(2)
    print("Happy to have you here. So, let's start\n")
    time.sleep(1)

# Take the input from user and call welcome function to run


current_user.setPlayerName(input(colored("What is your name?\n",
                           'cyan', attrs=['bold'])).capitalize())

welcome()

# Function to start the game


def start_game():
    """
    Start game, set scenario, get child name and type of books
    """
    time.sleep(1)
    print('\nPerfect!')
    time.sleep(2)
    print(f"{current_user.child_name} has to give a presentation on "
          "an interesting book in front of parents, "
          "teachers and the whole class.")
    time.sleep(0.5)
    print("The book should be appropriate and understandable "
          "so that every child can understand, learn, enjoy, "
          "and above all not be bored..\n")
    time.sleep(1.5)
    print(f"You should make a choice for {current_user.child_name}, be careful"
          ", make the right choice!\n")
    time.sleep(2)
    print(f"{current_user.player_name}, there are 4 types of books.\n")
    time.sleep(1)
    # Style types of books
    print(("  "), (colored("ADVENTURE", "green", attrs=["reverse", "bold"])),
                  (colored("ROMANTIC", "red", attrs=["reverse", "bold"])),
                  (colored("COMEDY", "yellow", attrs=["reverse", "bold"])),
                  (colored("HISTORY", "cyan", attrs=["reverse", "bold"])))
    time.sleep(1.5)

# Take the input from user and call the start game function to run


current_user.setChildName(input(colored("What is your child's name?\n",
                          'cyan', attrs=['bold'])).capitalize())
start_game()


def book_choice():
    """
    Helper Function about user' book choice
    A while loop to check user' input
    try and except for ValueError
    """
    book_choice_options = ['a', 'adventure', 'r', 'romantic', 'c', 'comedy',
                           'h', 'history']
    user_choice = ''
    while user_choice not in book_choice_options:
        print(colored('\nWhich type of book will you choose?'
                      '(a, r, c or h)', 'cyan', attrs=['bold']))
        user_choice = input().lower()
        current_user.setBookChoice(user_choice)
        break
    try:
        # If user choice exists and if it's not in book choice options
        if current_user.book_choice and current_user.book_choice not in\
                book_choice_options:
            raise ValueError(
                f"You provide wrong data {current_user.book_choice}"
            )
    except ValueError as e:
        print(colored(f'Invalid : {e}, please try again',
                      'red', attrs=['bold']))
        book_choice()
    # Make user choice more flexible
    if current_user.book_choice == book_choice_options[0] or \
       current_user.book_choice == book_choice_options[1]:
        # if the player typed a, he will redirect to adventure_book()
        book_chosen('Adventure', 'The Shadow of Glass', 'The Ship of Shadows')
    elif current_user.book_choice == book_choice_options[2] or \
            current_user.book_choice == book_choice_options[3]:
        # if the player typed r, he will redirect to romantic_book()
        book_chosen('Romantic', 'Fifty Shades of Grey', 'Mama, '
                    'Do You love me?')
    elif current_user.book_choice == book_choice_options[4] or \
            current_user.book_choice == book_choice_options[5]:
        # if the player typed c, he will redirect to comedy_book()
        book_chosen('Comedy', 'Double Trouble', 'Coco Banjo')
    elif current_user.book_choice == book_choice_options[6] or \
            current_user.book_choice == book_choice_options[7]:
        # if the player typed h, he will redirect to history_book()
        book_chosen('History', 'Treasure Island', 'Who was Anne Franck?')


def validate_integer():
    """
    Helper Function for user' validate data
    Use of While loop, try and except
    If the user enter an incorrect data,
    he will ask to re-enter data again
    """
    user_integer_options = ['1', '2']
    user_integer = ' '
    while user_integer not in user_integer_options:
        print(colored(f'What would you choose {current_user.player_name}'
                      '(1 or 2)?', 'cyan', attrs=['bold']))
        user_integer = input()
        current_user.setBookDecision(user_integer)
        time.sleep(1.5)
        break
    try:
        # If user integer is not in user integer options
        if current_user.book_decision not in user_integer_options:
            raise ValueError(
                f"You provide wrong data {current_user.book_decision}"
            )
    except ValueError as e:
        print(colored(f'Invalid : {e}, please try again',
                      'red', attrs=['bold']))
        # Call again validate_integer if user enter wrong data
        validate_integer()

    if current_user.book_decision == user_integer_options[0]:
        # Call game over function when it is Bad Choice
        time.sleep(2)
        game_over()
    elif current_user.book_decision == user_integer_options[1]:
        # Good Choice
        # Style the output
        good_choice_art = figlet_format("GOOD CHOICE", font='slant')
        colored_choice = colored(good_choice_art, 'green', attrs=['bold'])
        print(colored_choice)
        time.sleep(1.5)
        print(f"GUESS WHAT? {current_user.child_name} will be among the best")
        print("This book is perfect for a presentation\n")
        time.sleep(1)
        print(f"{current_user.child_name} will surely love it too and make one"
              " of the best presentations at school.\n")
        time.sleep(1.5)
        make_another_choice()


# Book chosen function


def book_chosen(book_type, choice_1, choice_2):
    """
    Adventure, romantic, comedy and history
    all book types in one function
    call and change data by arguments
    """
    print(f'\nThat is great!! You have chosen the {book_type} Book')
    time.sleep(1)
    print(f"Let's bring some {book_type} into this presentation\n")
    time.sleep(2)
    print(f'There are 2 choices for {book_type} {current_user.player_name}\n')
    time.sleep(2)
    print(f'Choice 1: {choice_1}\n')
    time.sleep(1.5)
    print(f'Choice 2: {choice_2}\n')
    time.sleep(1.5)
    # If user enters wrong data
    validate_integer()
    time.sleep(1)

# game_over function


def game_over():
    """
    If player chose wrong choice, game_over function is called
    """
    game_over_art = figlet_format("BAD CHOICE", font='slant')
    colored_ascii = colored(game_over_art, 'red', attrs=['bold'])
    print(colored_ascii)
    time.sleep(1)
    print("You should make another choice "
          f"so that {current_user.child_name} can make the best presentation "
          "to everyone")
    print(f"{current_user.child_name} cannot make a presentation on this book"
          ", it is absolutely not suitable\n")
    time.sleep(1.5)
    # Make another choice
    make_another_choice()

# Function to play again


def make_another_choice():
    """
    Give user the opportunity to make another choice
    A while loop to check user' input
    try and except for ValueError
    """
    time.sleep(3)
    another_choice_options = ['y', 'yes', 'n', 'no']
    user_answer = ''
    while user_answer not in another_choice_options:
        print(colored(f'DO YOU WANT TO MAKE ANOTHER CHOICE '
                      f'{current_user.player_name}? (yes or no)',
                      'cyan', attrs=['bold']))
        # Get the user's answer
        user_answer = input().lower()
        break
    try:
        # If user answer exists and if it's not in another choice options
        if user_answer and user_answer not in another_choice_options:
            raise ValueError(
                f'You provide wrong data {user_answer}'
            )
    except ValueError as e:
        print(colored(f'Invalid : {e}, please try again\n',
                      'red', attrs=['bold']))
        make_another_choice()
    # Make input more flexible
    if user_answer == another_choice_options[0] or \
       user_answer == another_choice_options[1]:
        # if the player choose 'yes', start the book game from book choice
        time.sleep(2)
        book_choice()
    elif user_answer == another_choice_options[2] or \
            user_answer == another_choice_options[3]:
        time.sleep(2)
        print(f"\nIt was a pleasure to have you with us "
              f"{current_user.player_name}")
        print('Hope that you enjoyed the game,'
              'You can come back whenever you want.\n')
        time.sleep(1)
        print(colored('IF YOU CHANGE YOUR MIND', 'green',
                      attrs=['bold']))
        # Reload the game
        print(colored('JUST CLICK THE GREEN BUTTON TO RESTART\n',
                      'green', attrs=['bold']))
        time.sleep(2)

        # Import a styling good bye message from Ascii Art Generator

        print('  ██████ ▓█████ ▓█████    ▓██   ██▓ ▒█████   █    ██ ')
        print('▒██    ▒ ▓█   ▀ ▓█   ▀     ▒██  ██▒▒██▒  ██▒ ██  ▓██▒')
        print('░ ▓██▄   ▒███   ▒███        ▒██ ██░▒██░  ██▒▓██  ▒██░')
        print('  ▒   ██▒▒▓█  ▄ ▒▓█  ▄      ░ ▐██▓░▒██   ██░▓▓█  ░██░')
        print('▒██████▒▒░▒████▒░▒████▒     ░ ██▒▓░░ ████▓▒░▒▒█████▓ ')
        print('▒ ▒▓▒ ▒ ░░░ ▒░ ░░░ ▒░ ░      ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ')
        print('░ ░▒  ░ ░ ░ ░  ░ ░ ░  ░    ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░ ')


# Call book choice functions so that the functions
# dependent on it can run normally


book_choice()
