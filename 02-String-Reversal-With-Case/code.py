# Exercise Name:
# 	02-String-Reversal-With-Case
# Description:
# 	Reverse each word of a string without changing upper-case positions.
# Given: 
# 	sentence = "Python is Awesome"
# Return: 
# 	"Nohtyp si Emosewa"

str = "Python is Awesome"
revString=""
split_string = str.split()

for word in split_string:   
    revString += word[::-1].capitalize()+" "

print(revString)
