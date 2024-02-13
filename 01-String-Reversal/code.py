# Exercise Name:
# 	01-String-Reversal
# Description:
# 	Reverse each word of a string.
# Given: 
# 	sentence = "Python is Awesome"
# Return: 
# 	"nohtyP si emosewA"

str = "Python is Awesome"
revString=""
split_string = str.split()

for word in split_string:
    revString += word[::-1]+" "

print(revString)
