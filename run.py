import random
import time
import os


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


# invitation to a game
clear()
print("\nWelcome to HANGaDICTATOR game by coffeebeanstudio1809@gmail.com")


# Enter player name
def getName():
    """
    Get a user name.
    """
    name = input("Enter your name: ")
    return name


def nameText():
    """
    Validate user a correct name.
    """
    while (True):
        textName = getName()
        if textName.isalpha() and len(textName.strip()) > 1:
            break
        # If name contains not a letter
        else:
            clear()
            print(f"{textName} is not valid. Please try again.")
    clear()
    print("Hello, " + textName.capitalize() + "! Best of Luck!")


nameText()


# Restart game
def onceagain():
    """
    At end of the game ask if user can play again.
    """
    global play
    play = input("\nPlay again? Y = yes, N = no \n")
    while play not in ["Y", "y", "N", "n"]:
        clear()
        play = input("Please enter 'Y' for 'yes', 'N' for 'no' \n")
    if play in ["Y", "y"]:
        clear()
        main()
    elif play in ["N", "n"]:
        clear()
        print("Thank you! Hope you enjoyed the game.")
        exit()


# Game start
time.sleep(2)
print("The game is about to start!\nEnjoy!")
time.sleep(4)
clear()


# Game
# Define variable
def main():
    """
    Main functionality with randomised word.
    """
    words = [
        'commonwealth', 'democracy', 'election', 'emancipation',
        'equality', 'fairness', 'freedom', 'honesty', 'humanity',
        'integrity', 'justice', 'liberty', 'minority', 'probity',
        'rectitude', 'rights', 'sincerity', 'suffrage', 'tolerance',
        'uprightness']
    word = random.choice(words)
    word = word.upper()
    total_guess = 7
    guessed = "-"*len(word)
    print("\nThis is the word to guess to kill a dictator:\n")
    while total_guess != 0:
        print(guessed)
        guess = input("\nEnter the HANGaDICTATOR word letter: \n").upper()
        # Check if a letter that entered is a letter
        if len(guess.strip()) == 0 or len(guess.strip()) > 1 or not guess.isalpha():  # noqa
            clear()
            print("Try a letter\n ")
            continue
        if guess in word:
            # If the letter guessed
            for index in range(len(word)):
                if word[index] == guess:
                    guessed = guessed[:index]+guess+guessed[index+1:]
            # If word guessed
            if guessed == word:
                clear()
                print(f"Your guessed word: {word}. Well done!!!")
                time.sleep(1)
                print("The dictator is hanged!")
                time.sleep(1)
                print("    ______\n"
                      "   |      |\n"
                      "   |      |\n"
                      "   |      |\n"
                      "   |      O \n"
                      "   |     /|\\ \n"
                      "   |     / \\ \n"
                      "___|___\n")
                onceagain()
        # If enter a wrong letter
        else:
            total_guess -= 1
            clear()
            print("Wrong guess.\n")
            print("The attempt(s) left: ", total_guess)
    # If all attempts are failed
    else:
        clear()
        print("\nYou loose.\n")
        print("The correct word is ", word)
        print("The dictator is free :( ")
        time.sleep(1)
        print("     _____\n"
              "   ( O   o ) \n"
              "  /    0    \\ \n"
              " / / |   | \\ \\ \n"
              "(``)  | |  (``) \n"
              "      | | \n"
              "     /   \\ \n"
              "     |   | \n"
              "    _|   |_ \n")

        onceagain()


main()
