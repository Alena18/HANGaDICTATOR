import random
import time
# invitation to a game
print("\nWelcome to HANGaDICTATOR game by coffeebeanstudio1809@gmail.com")
name = input("Enter your name:")
print("Hello" + name + "Best of Luck!")
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
    global play_game
    words = ["freedom", "rights", "humanity", "democracy", "tolerance", 
    "liberty", "equality", "justice", "honesty", "integrity", "fairness", 
    "probity", "uprightness", "rectitude", "sincerity", "commonwealth", 
    "emancipation","suffrage","election", "minority"]
    word = random.choice(words)
    length = len(word)
    count = 0
    display = "_"*length
    guessed = []
    play_game = ""





