# Import
import time


def welcome():
    """
    Welcome and get player data
    """
    print('Hello there!')
    time.sleep(1)

    player_name = input('What is your name?\n').capitalize()
    time.sleep(2)
    print(f"Welcome to the children's reading camp {player_name}")
    time.sleep(2)
    print("Happy to have you here. So, let's start the game\n")
    time.sleep(1)
    start_game(player_name)

# Function to start the game


def start_game(player_name):
    """
    start game, set scenario, get child name and type of books
    """
    print("Your child has to give a presentation on an interesting book "
          "in front of parents, teachers and the whole class.\n")
    time.sleep(0.5)
    print("The book should be appropriate and comprehensible.\n")
    time.sleep(2)
    child_name = input("What is your child's name?\n").capitalize()
    time.sleep(1)
    print('Perfect!\n')
    time.sleep(1.5)
    print(f"You should make a choice for {child_name}, be careful, "
          "make the right choice!\n")
    time.sleep(2)
    print(f"{player_name}, there are 4 types of books.\n")
    print('Which type of book will you choose? (a, r, c or h)')

    # Take the type of books
    choice = input().lower()
    if 'a' in choice:
        # if the player typed a, he will redirect to adventure_book()
        adventure_book(player_name, child_name)
    elif 'r' in choice:
        # if the player typed r, he will redirect to romantic_book()
        romantic_book(player_name, child_name)
    elif 'c' in choice:
        # if the player typed c, he will redirect to comedy_book()
        comedy_book(player_name, child_name)
    elif 'h' in choice:
        # if the player typed h, he will redirect to history_book()
        history_book(player_name, child_name)
    else:
        # else call game_over() function
        game_over('Invalid choice')

# Adventure book function


def adventure_book(player_name, child_name):
    """
    Description of situation
    """
    print('Yay!! You have chosen the Adventure Book\n')
    time.sleep(1)
    print("Let's bring some adventure into this presentation")
    time.sleep(2)
    print(f'There are 2 choices for Adventure Books {player_name}')
    time.sleep(2)
    print('Choice 1: The Shadow of Glass\n')
    time.sleep(1)
    print('or\n')
    time.sleep(1)
    print('Choice 2: The Ship of Shadow\n')
    time.sleep(1.5)
    print(f'What would you choose {player_name}? (1 or 2)')
    time.sleep(2)

    # Take the choice
    choice = int(input())

    if choice == 1:
        # Bad Choice
        print("Bad choice!!!")
        print(f"{child_name} cannot make a presentation on this book, "
              "it might scare the other children\n")
        game_over(f"{player_name}, you should make another choice "
                  "so that {child_name} can make the best presentation to "
                  "everyone\n")
    elif choice == 2:
        # Good Choice
        print(f"Good choice {player_name}!!!")
        print("This adventure book is perfect for a presentation")
    else:
        game_over('Invalid Choice')

# Romantic book function


def romantic_book(player_name, child_name):
    """
    Description of situation
    """
    print('Perfect!! You have chosen the Romantic Book\n')
    time.sleep(1)
    print("Let's bring some love into this presentation")
    time.sleep(2)
    print(f'There are 2 choices for Romantic Books {player_name}\n')
    time.sleep(2)
    print('Choice 1: Mama, Do you love me?\n')
    time.sleep(1)
    print('or\n')
    time.sleep(1)
    print('Choice 2: Fifty Shades of Grey\n')
    time.sleep(1.5)
    print(f'What would you choose {player_name}? (1 or 2)')
    time.sleep(2)

    # Take the choice
    choice = int(input())

    if choice == 1:
        # Good Choice
        print(f"Good choice {player_name}!!!")
        print("This romantic book is THE BOOK")
    elif choice == 2:
        # Bad Choice
        print("Bad choice!!!")
        print(f"{child_name} cannot make a presentation on this book, "
              "it is not suitable for children\n")
        game_over(f"{player_name}, you should make another choice "
                  "so that {child_name} can make the best presentation to "
                  "everyone\n")  
    else:
        game_over('Invalid Choice')

# Comedy book function


def comedy_book(player_name, child_name):
    """
    Description of situation
    """
    print('HA HA!! You have chosen the Comedy Book\n')
    time.sleep(1)
    print("Let's bring some fun into this presentation")
    time.sleep(2)
    print(f'There are 2 choices for Comedy Books {player_name}')
    time.sleep(2)
    print('Choice 1: Double Trouble\n')
    time.sleep(1)
    print('or\n')
    time.sleep(1)
    print('Choice 2: Coco Banjo\n')
    time.sleep(1.5)
    print(f'What would you choose {player_name}? (1 or 2)')
    time.sleep(2)

    # Take the choice
    choice = int(input())

    if choice == 1:
        # Bad Choice
        print("Bad choice!!!")
        print(f"{child_name} cannot make a presentation on this book, "
              "it is absolutely not suitable\n")
        game_over(f"{player_name}, you should make another choice "
                  "so that {child_name} can make the best presentation to "
                  "everyone\n")
    elif choice == 2:
        # Good Choice
        print(f"Good choice {player_name}!!!")
        print(f"{child_name} will make everyone laugh with this book"
              "This is the perfect comedy book for a presentation")
    else:
        game_over('Invalid Choice')


welcome()
