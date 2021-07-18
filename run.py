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

# Function to start the game and set the scenario


def start_game(player_name):
    """
    start game, set scenario and get child name
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


welcome()


# Fisrt option

# Second option

# Third option

# Fourth option

# End game

# Play game
