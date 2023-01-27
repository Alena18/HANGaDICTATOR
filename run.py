import random
import time

# invitation to a game
print("\nWelcome to HANGaDICTATOR game by coffeebeanstudio1809@gmail.com")


# Enter player name
def getName():
    name = input("Enter your name: ")
    return name


def nameText():
    while (True):
        textName = getName()
        if textName.isalpha() and len(textName.strip()) > 1:
            break
        # If name contains not a letter
        else:
            print(f"{textName} is not valid. Pease try aglain.")
    print("Hello, " + textName.capitalize() + "! Best of Luck!")


nameText()


# Restart game
def onceagain():
    global play
    play = input("\nPlay again? Y = yes, N = no \n")
    while play not in ["Y", "y", "N", "n"]:
        play = input("Please enter 'Y' for 'yes', 'N' for 'no' \n")
    if play in ["Y", "y"]:
        main()
    elif play in ["N", "n"]:
        print("Thank you! Hope you enjoyed the game.")
        exit()


# Game start
time.sleep(1)
print("The game is about to start!\nEnjoy!")
time.sleep(1)


# Game
# Define variable
def main():
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
            print("Try a letter\n ")
            continue
        if guess in word:
            # If the letter guessed
            for index in range(len(word)):
                if word[index] == guess:
                    guessed = guessed[:index]+guess+guessed[index+1:]
            # If word guessed
            if guessed == word:
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
            print("Wrong guess.\n")
            print("The attempt(s) left: ", total_guess)
    # If all attempts are failed
    else:
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
