from colorama import Back, Fore, Style
import pathlib
import random

words = pathlib.Path("word_list.txt").read_text(encoding="utf-8").strip().split('\n')#select words from this text to randomly check
check = pathlib.Path("wordle.txt").read_text(encoding="utf-8").strip().split('\n')#Guess should be made from this list of words only

rand = random.choice(words)

def color_background(word, target_letter, background_color):
    colored_word = ""
    for char in word:
        if char.lower() == target_letter.lower():
            colored_word += f"{Back.__dict__[background_color]}{Fore.WHITE}{char}{Style.RESET_ALL}"
        else:
            colored_word += char
    print(colored_word)

print(words)
# Example usage
word = rand
print("randomly chosen word is",word)
chance = 6

while(chance!=0):
    print("###### YOU GOT {0} CHANCES LEFT #######".format(chance))
    guess = input("Enter the 5 letter GUESS: ")
    chance-=1
    if(len(guess)!=5):
        print("Please guess a 5 letter word")
    elif(word not in check):
        print("Enter a valid word from wordle.txt")
    elif(guess == word):
        print("Guessed the correct word")
        break
    else:
        for letter in guess:
            if(word.find(letter)!=-1):
                if(guess.find(letter)==word.find(letter)):
                    color_background(guess,letter,'GREEN')
                else:
                    color_background(guess,letter,'RED')
            elif(letter not in word):
                print("Letter {0} not found in word".format(letter))
