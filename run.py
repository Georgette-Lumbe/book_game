# Import the modules
import time
from pyfiglet import figlet_format
from termcolor import colored


while True:
    # BOOK GAME OPENS IN 5s
    print(colored('The BOOK GAME starts in 5s...', 'cyan'))
    opening_time = 5
    while opening_time > 0:
        m, s = divmod(opening_time, 5)
        time_left = str(m).zfill(2) + ':' + str(s).zfill(2)
        print(time_left + '\r', end='')
        time.sleep(1)
        opening_time -= 1
    break


class Data:

    def getData(self, player_name, child_name):
        Data.player_name = player_name
        Data.child_name = child_name


def welcome():
    """
    Welcome and get player data
    """
    time.sleep(2)
    # Style the welcome message
    welcome_art = figlet_format(f"Welcome {player_name}", font='slant')
    colored_art = colored(welcome_art, 'cyan', attrs=['bold'])
    print(colored_art)
    time.sleep(2)
    print("Happy to have you here. So, let's start\n")
    time.sleep(1)


player_name = input(colored("What is your name?\n",
                    'cyan', attrs=['bold'])).capitalize()
welcome()

# Function to start the game


def start_game():
    """
    start game, set scenario, get child name and type of books
    """
    time.sleep(1)
    print('\nPerfect!')
    time.sleep(2)
    print(f"{child_name} has to give a presentation on an interesting book "
          "in front of parents, teachers and the whole class.")
    time.sleep(0.5)
    print("The book should be appropriate and comprehensible.\n")
    time.sleep(1.5)
    print(f"You should make a choice for {child_name}, be careful, "
          "make the right choice!\n")
    time.sleep(2)
    print(f"{player_name}, there are 4 types of books.\n")
    time.sleep(1)
    # Style types of books
    print(("  "), (colored("ADVENTURE", "green", attrs=["reverse", "bold"])),
                  (colored("ROMANTIC", "red", attrs=["reverse", "bold"])),
                  (colored("COMEDY", "yellow", attrs=["reverse", "bold"])),
                  (colored("HISTORY", "cyan", attrs=["reverse", "bold"])))
    time.sleep(1.5)


child_name = input(colored("What is your child's name?\n",
                   'cyan', attrs=['bold'])).capitalize()


def book_choice():
    """
    Helper Function about user' book choice
    A while loop to check user' input
    try and except for ValueError
    """
    book_choice_options = ['a', 'r', 'c', 'h']
    user_choice = ''
    while user_choice not in book_choice_options:
        print(colored('\nWhich type of book will you choose?'
                      '(a, r, c or h)', 'cyan', attrs=['bold']))
        user_choice = input('Enter a letter: ')
        break
    try:
        if user_choice not in book_choice_options:
            raise ValueError(
                f"You provide wrong data {user_choice}"
            )
    except ValueError as e:
        print(colored(f'Invalid : {e}, please try again',
                      'red', attrs=['bold']))
        book_choice()

    if user_choice == book_choice_options[0]:
        # if the player typed a, he will redirect to adventure_book()
        adventure_book()
    elif user_choice == book_choice_options[1]:
        # if the player typed r, he will redirect to romantic_book()
        romantic_book()
    elif user_choice == book_choice_options[2]:
        # if the player typed c, he will redirect to comedy_book()
        comedy_book()
    elif user_choice == book_choice_options[3]:
        # if the player typed h, he will redirect to history_book()
        history_book()


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
        print(colored(f'\nWhat would you choose {player_name} (1 or 2)?',
                      'cyan', attrs=['bold']))
        user_integer = input('Enter a number: ')
        time.sleep(1.5)
        break
    try:
        if user_integer not in user_integer_options:
            raise ValueError(
                f"You provide wrong data {user_integer}"
            )
    except ValueError as e:
        print(colored(f'Invalid : {e}, please try again',
                      'red', attrs=['bold']))
        # Call again validate_integer if user enter wrong data
        validate_integer()

    if user_integer == user_integer_options[0]:
        # Call game over function when it is Bad Choice
        time.sleep(2)
        game_over()
    elif user_integer == user_integer_options[1]:
        # Good Choice
        # Style the output
        good_choice_art = figlet_format("GOOD CHOICE", font='slant')
        colored_choice = colored(good_choice_art, 'green', attrs=['bold'])
        print(colored_choice)
        time.sleep(1.5)
        print(f"GUESS WHAT? {child_name} will be among the best")
        print("This book is perfect for a presentation\n")
        time.sleep(1)
        print(f"{child_name} will surely love it too and make one of the best "
              "presentations at school.\n")
        time.sleep(1.5)


# Adventure book function


def adventure_book():
    """
    Description of situation
    """
    print('\nYay!! You have chosen the Adventure Book')
    time.sleep(1)
    print("Let's bring some adventure into this presentation\n")
    time.sleep(2)
    print(f'There are 2 choices for Adventure Books {player_name}')
    time.sleep(2)
    print('Choice 1: The Shadow of Glass\n')
    time.sleep(1)
    print('or\n')
    time.sleep(1)
    print('Choice 2: The Ship of Shadows\n')
    time.sleep(1.5)
    # If user enter wrong data
    validate_integer()

    time.sleep(1)

    print(colored('Do you need a summary of this book? (yes or no)',
                  'cyan', attrs=['bold']))
    time.sleep(1)
    """
    Conditional statement to relate more about the book choosen or not
    """
    choice = input()
    if 'yes' in choice:
        print("This book is about Aleja who is a dreamer who longs for "
              "a life of magic and adventure. So when a mysterious ship "
              "arrives in her Spanish harbour city, crewed by a band of "
              "ruthless women, Aleja knows it's sailed right out of a "
              "legend. ... But life aboard the Ship of Shadows is more  "
              "than even she bargained for.")
        time.sleep(2)
        make_another_choice()
    elif 'no' in choice:
        print("It's perfect, you can find out for yourself by reading it")
        time.sleep(1.5)
        make_another_choice()
    else:
        print('OOPS, Invalid Choice')
        time.sleep(1.5)
        make_another_choice()


# Romantic book function


def romantic_book():
    """
    Description of situation with differents choices
    """
    print('\nPerfect!! You have chosen the Romantic Book')
    time.sleep(1)
    print("Let's bring some love into this presentation\n")
    time.sleep(2)
    print(f'There are 2 choices for Romantic Books {player_name}\n')
    time.sleep(2)
    print('Choice 1: Fifty Shades of Grey\n')
    time.sleep(1)
    print('or\n')
    time.sleep(1)
    print('Choice 2: Mama, Do you love me?\n')
    time.sleep(1.5)
    # If user enter wrong data
    validate_integer()
    time.sleep(1)
    print(colored('Do you need a summary of this book? (yes or no)',
                  'cyan', attrs=['bold']))
    time.sleep(1)
    # Take the input
    choice = input()
    """
    Conditional statement to relate more about the book choosen or not
    """
    if 'yes' in choice:
        print('Mama, Do you love me? is a Charming tale of affection, '
              'adventure, and wonder in which a young Inuit girl disobeys '
              'wanders away from home and learns valuable lessons..')
        time.sleep(2)
        make_another_choice()
    elif 'no' in choice:
        print("It's perfect, you can find out for yourself by reading it")
        time.sleep(1.5)
        make_another_choice()
    else:
        print('OOPS, Invalid Choice')

        time.sleep(1.5)
        make_another_choice()


# Comedy book function


def comedy_book():
    """
    Description of situation
    """
    print('\nHA HA!! You have chosen the Comedy Book')
    time.sleep(1)
    print("Let's bring some fun into this presentation\n")
    time.sleep(2)
    print(f'There are 2 choices for Comedy Books {player_name}')
    time.sleep(2)
    print('Choice 1: Double Trouble\n')
    time.sleep(1)
    print('or\n')
    time.sleep(1)
    print('Choice 2: Coco Banjo\n')
    time.sleep(1.5)
    # If user enter wrong data
    validate_integer()
    time.sleep(1)
    print(colored('Do you need a summary of this book? (yes or no)',
                  'cyan', attrs=['bold']))
    time.sleep(1)
    choice = input()
    if 'yes' in choice:
        print("Coco Banjo to the rescue! Coco Banjo loves her life. "
              "She sleeps in a tiger onesie, wears her mum's diamonds "
              "just because she can, and has dolphins and penguins for "
              "friends.")
        time.sleep(1.5)
        print("Today Coco's planning a Yay Day of fun on her secret "
              "island home in the middle of Sydney Harbour. But "
              "wait . . . what's that Secret Signal? Oh no, Narianna "
              "(known as N) is being bullied!")
        time.sleep(1.5)
        print("Coco sets off for school to rescue her. But when cranky "
              "school principal Miss Trample sees Coco's school uniform "
              "(customised, thank you very much), Coco might be in even "
              "more trouble than her best friend.")
        time.sleep(1.5)
        print("How will she get out of this one?")
        time.sleep(2)
        make_another_choice()
    elif 'no' in choice:
        print("It's perfect, you can find out for yourself by reading it")
        time.sleep(1.5)
        make_another_choice()
    else:
        print('OOPS, Invalid Choice')
        time.sleep(2)
        make_another_choice()

# History book function


def history_book():
    """
    Description of situation
    """
    print('\nThat is great!! You have chosen the History Book')
    time.sleep(2)
    print(f'There are 2 choices for History Book {player_name}\n')
    time.sleep(2)
    print('Choice 1: Treasure Island\n')
    time.sleep(1)
    print('or\n')
    time.sleep(1)
    print('Choice 2: Who was Anne Franck?\n')
    time.sleep(1.5)
    # If user enter wrong data
    validate_integer()
    time.sleep(1)
    print(colored('Do you need a summary of this book? (yes or no)',
                  'cyan', attrs=['bold']))
    time.sleep(1)
    choice = input()
    if 'yes' in choice:
        print("Anne Frank was a teenage Jewish girl who kept a diary "
              "while her family was in hiding from the Nazis during "
              "World War II. For two years, she and seven others "
              "lived in a 'Secret Annex' lived in a 'Secret Annex'")
        time.sleep(1)
        print("Anne died in the Bergen-Belsen camp in 1945.")
        time.sleep(2)
        make_another_choice()
    elif 'no' in choice:
        print("It's perfect, you can find out for yourself by reading it")
        time.sleep(1)
        make_another_choice()
    else:
        print('OOPS, Invalid Choice')
        time.sleep(2)
        make_another_choice()


# Function to play again


def make_another_choice():
    """
    Give user the opportunity to make another choice
    """
    time.sleep(3)
    print('')
    print(colored(f'DO YOU WANT TO MAKE ANOTHER CHOICE {player_name}?'
                  '(yes or no)', 'cyan', attrs=['bold']))
    # Take the user input
    choice = input().lower()
    if 'yes' in choice:
        # if the player choose 'yes', start the book game from book choice
        book_choice()
    elif 'no' in choice:
        print('')
        time.sleep(1)
        print("It was a pleasure to have you with us")
        time.sleep(1)
        print('IF YOU CHANGE YOUR MIND')
        # Reload the game
        print('JUST CLICK THE GREEN BUTTON TO RESTART')
    else:
        print('OOPS, Invalid Data')
        print(f'Please {player_name}, make another choice\n')
        time.sleep(2)
        make_another_choice()

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
          f"so that {child_name} can make the best presentation to "
          "everyone")
    print(f"{child_name} cannot make a presentation on this book, "
          "it is absolutely not suitable\n")
    time.sleep(1.5)
    # Make another choice
    make_another_choice()

# Call functions


start_game()
book_choice()
c1 = Data()
c1.getData(player_name, child_name)
