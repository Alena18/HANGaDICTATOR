import random
import time
# invitation to a game
print("\nWelcome to HANGaDICTATOR game by coffeebeanstudio1809@gmail.com")
name = input("Enter your name:")
print("Hello, " + name + "! Best of Luck!")
time.sleep(3)
print("The game is about to start!\nEnjoy!")
time.sleep(3)
# game
# define variable
def main():
    global count
    global display
    global word
    global guessed
    global length
    global play
    words = ["freedom", "rights", "humanity", "democracy", "tolerance", 
    "liberty", "equality", "justice", "honesty", "integrity", "fairness", 
    "probity", "uprightness", "rectitude", "sincerity", "commonwealth", 
    "emancipation","suffrage","election", "minority"]
    word = random.choice(words)
    length = len(word)
    count = 0
    display = "_"*length
    guessed = []
    play = ""
    
# Restart game

def onceagain ():
    global play
    play = input("Play again? Y = yes, N = no \n")
    while play not in ["Y", "y", "N", "n"]:
        play = input("Play again? Y = yes, N = no \n")
    if play ==  "y":
        main()
    elif play == "n":
        print("Thank you! See you again.")
        exit()    

# Play game
def hang():
     guess = input("Enter the HANGaDICTATOR word:" + display + "\n" )
     guess = guess.strip()
     if len(guess.strip()) == 0 or len(guess.strip()) > 1 or not guess.isalpha():
            print("Try a letter\n ")
            hang()
     elif guess in word:
          guessed.extend([guess])
          index = word.lower(guess)
          word = word[:index] + "_" + word[index + 1:]
          print(display + "\n")
     elif guess in guessed:
          print("Try another letter.\n")
     else:
          count +=1
          if count == 1:
             time.sleep(1)
             print("    _________\n"
                   "   |      \n"
                   "   |      \n"
                   "   |      \n"
                   "   |      \n"
                   "   |      \n"
                   "   |      \n"
                   "   |      \n"
                   "   |      \n"
                   "   |      \n"
                   "   |      \n"
                   "   |      \n"
                   "   |      \n"
                   "   |      \n"
                   "   |      \n"    
                   "___|___   \n"          
                 )
main()

hang()





