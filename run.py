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
    print(f"Welcome to BOOK CHOICE GAME {player_name}")
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
        print('OOPS, Invalid')
        print(f'Please {player_name}, make another choice\n')
        start_game(player_name)

# Adventure book function


def adventure_book(player_name, child_name):
    """
    Description of situation
    """
    print('Yay!! You have chosen the Adventure Book')
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
    print(f'What would you choose {player_name}? (1 or 2)\n')
    time.sleep(2)

    # Take the choice
    choice = int(input())

    if choice == 1:
        # Bad Choice
        print("Bad choice!!!")
        print(f"{child_name} cannot make a presentation on this book, "
              "it might scare the other children")
        game_over(player_name, child_name)
    elif choice == 2:
        # Good Choice
        print(f"Good choice {player_name}!!!\n")
        time.sleep(1)
        print("This adventure book is perfect for a presentation\n")
        time.sleep(1)
        print('Do you want to know more about this book? (yes or no)\n')
        time.sleep(1)
        choice = input()
        if 'yes' in choice:
            print("This book is about Aleja who is a dreamer who longs for a" 
                  " life of magic and adventure. So when a mysterious ship "
                  "arrives in her Spanish harbour city, crewed by a band of "
                  "ruthless women, Aleja knows it's sailed right out of a "
                  "legend. ... But life aboard the Ship of Shadows is more  "
                  "than even she bargained for.")
        elif 'no' in choice:
            print("It's perfect, you can find out for yourself by reading it")
        else:
            print('OOPS, Invalid choice')

        time.sleep(1.5)
        make_another_choice(player_name, child_name)

    else:
        print('OOPS, Invalid\n')
        print(f'Please {player_name}, make another choice\n')
        adventure_book(player_name, child_name)
        time.sleep(2)

# Romantic book function


def romantic_book(player_name, child_name):
    """
    Description of situation
    """
    print('Perfect!! You have chosen the Romantic Book')
    time.sleep(1)
    print("Let's bring some love into this presentation\n")
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
        time.sleep(1)
        print("This romantic book is THE BOOK\n")
        time.sleep(1)
        print('Do you need a summary of this book? (yes or no)\n')
        time.sleep(1)
        choice = input()
        if 'yes' in choice:
            print('Mama, Do you love me? is a Charming tale of affection, '
                  'adventure, and wonder in which a young Inuit girl disobeys '
                  'wanders away from home and learns valuable lessons..')
        elif 'no' in choice:
            print("It's perfect, you can find out for yourself by reading it")
        else:
            print('OOPS, Invalid choice')

        time.sleep(1.5)
        make_another_choice(player_name, child_name)

    elif choice == 2:
        # Bad Choice
        print("Bad choice!!!")
        print(f"{child_name} cannot make a presentation on this book, "
              "it is not suitable for children\n")
        time.sleep(2)
        game_over(player_name, child_name)  
    else:
        print('OOPS, Invalid\n')
        print(f'Please {player_name}, make another choice\n')
        romantic_book(player_name, child_name)
        time.sleep(2)

# Comedy book function


def comedy_book(player_name, child_name):
    """
    Description of situation
    """
    print('HA HA!! You have chosen the Comedy Book')
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
    print(f'What would you choose {player_name}? (1 or 2)')
    time.sleep(2)

    # Take the choice
    choice = int(input())

    if choice == 1:
        # Bad Choice
        print("Bad choice!!!")
        print(f"{child_name} cannot make a presentation on this book, "
              "it is absolutely not suitable\n")
        game_over(player_name, child_name)
    elif choice == 2:
        # Good Choice
        print(f"Good choice {player_name}!!!")
        time.sleep(1)
        print(f"{child_name} will make everyone laugh with this book. "
              "This is the perfect comedy book for a presentation\n")
        time.sleep(1)
        print('Do you need a summary of this book? (yes or no)\n')
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
        elif 'no' in choice:
            print("It's perfect, you can find out for yourself by reading it")
        else:
            print('OOPS, Invalid choice')
        time.sleep(2)
        make_another_choice(player_name, child_name)

    else:
        print('OOPS, Invalid\n')
        print(f'Please {player_name}, make another choice\n')
        comedy_book(player_name, child_name)
        time.sleep(2)

# History book function


def history_book(player_name, child_name):
    """
    Description of situation
    """
    print('That is great!! You have chosen the History Book\n')
    time.sleep(2)
    print(f'There are 2 choices for History Book {player_name}\n')
    time.sleep(2)
    print('Choice 1: Who was Anne Franck?\n')
    time.sleep(1)
    print('or\n')
    time.sleep(1)
    print('Choice 2: Treasure Island\n')
    time.sleep(1.5)
    print(f'What would you choose {player_name}? (1 or 2)')
    time.sleep(2)

    # Take the choice
    choice = int(input())

    if choice == 1:
        # Good Choice
        print(f"Good choice {player_name}!!!")
        time.sleep(1)
        print("Every child should have this book\n")
        time.sleep(1)
        print('Do you need a summary of this book? (yes or no)\n')
        time.sleep(1)
        choice = input()
        if 'yes' in choice:
            print("Anne Frank was a teenage Jewish girl who kept a diary "
                  "while her family was in hiding from the Nazis during "
                  "World War II. For two years, she and seven others "
                  "lived in a 'Secret Annex' lived in a 'Secret Annex'")
            time.sleep(1)
            print("Anne died in the Bergen-Belsen camp in 1945.")
        elif 'no' in choice:
            print("It's perfect, you can find out for yourself by reading it")
        else:
            print('OOPS, Invalid choice')

        time.sleep(2)
        make_another_choice(player_name, child_name)

    elif choice == 2:
        # Bad Choice
        print("Bad choice!!!\n")
        time.sleep(1)
        print(f"{child_name} cannot make a presentation on this book, "
              "it is not suitable for children\n")
        time.sleep(2)
        game_over(player_name, child_name)
    else:
        print('OOPS, Invalid\n')
        print(f'Please {player_name}, make another choice\n')
        history_book(player_name, child_name)
        time.sleep(2)

# Function to play again


def make_another_choice(player_name, child_name):
    time.sleep(3)
    print('')
    print(f'DO YOU WANT TO MAKE ANOTHER CHOICE {player_name}? (yes or no)\n')

    choice = input().lower()
    if 'yes' in choice:
        # if the player choose 'yes', start the book game from beginning
        start_game(player_name)
    elif 'no' in choice:
        print('')
        time.sleep(1)
        print("Hope you liked the BOOK you chose for your child\n")
        print(f"{child_name} will surely love it too and make one of the best "
              "presentations at school\n")
        time.sleep(2)
        print(f"GUESS WHAT? {child_name} will be among the best\n")
        time.sleep(1.5)
        print('IF YOU CHANGE YOUR MIND\n')
        print('CLICK THE GREEN BUTTON\n')
        print('     ')
    else:
        print('OOPS, Invalid')
        print(f'Please {player_name}, make another choice\n')
        time.sleep(2)
        make_another_choice(player_name, child_name)

# game_over function


def game_over(player_name, child_name):
    print('GAME OVER')
    time.sleep(1)
    print(f"{player_name}, you should make another choice "
          f"so that {child_name} can make the best presentation to "
          "everyone\n")
    time.sleep(2)

    make_another_choice(player_name, child_name)


welcome()
