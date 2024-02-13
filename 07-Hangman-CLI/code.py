# Exercise Name:
# 	07-Hangman-CLI
# Description:
# 	Create a hangman CLI game
# Rough game logic:
# 	1. Pick a random word. (Initially just use a hardcoded word like 'watermelon'. Random selection can be done later.)
# 	2. Initialize Guess Count to 6
# 	3. Show one underscore for each character in the word. For example, in case of 'watermelon', show 10 underscores like: _ _ _ _ _ _ _ _ _ _ 
# 	4. Prompt user to input their guess
# 		- Show a sorted list of already guessed characters
# 		- Guess should be ONE character from the alphabet
# 		- Guessed character should be new and not have been previously guessed
# 	5. Check if that character exists in the selected word
# 		a. If the character exists, reveal the character in its position. 
# 		   For example, in case of 'watermelon' and user guessed 'e', show: _ _ _ e _ _ e _ _ _
# 		b. If the character does not exist in the selected word, show warning and decrement Guess Count by one
# 	6. If the Guess Count
# 		a. is greater than zero, loop and take another input
# 		b. becomes zero before guessing all the characters in the word, Game Over.
# For improvement:
# 	https://random-word-api.herokuapp.com/word

import requests
import json
response_API = requests.get('https://random-word-api.herokuapp.com/word')
print(response_API.status_code)

data = response_API.text
data = data[2:-2]

print(data)

print("You have a total of {0} guesses".format(len(data)))
str=''
score = len(data)
word = score*'_'
print(score)

while(score>0):
    print("remaining guesses: {}".format(score))
    print("word is ",word)
    guess = input("Enter the guess ")
    if guess in data:
        lst = [i for i, char in enumerate(data) if char == guess]
        for index in lst:
            word = word[:index] + guess + word[index+1:]
        
        print("word is ",word)
        print("You guessed correctly")

        if(word == data):
            break
    else:
        print("You guessed incorrectly")
        score-=1;

print("final guess is",word)
print("final data is",data)

if(word == data):
    print("Your won the game")

else:
    print("Your lost the game")


