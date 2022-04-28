#407. Program to design the game 'GUESS THE LUCKY NUMBER'

import random as bot

#Generate a random lucky number
lucky_number = bot.randint(1, 1)

#Prompt and accept the user's guessed number
print("Guess a number in the range of 1 to 6")
guessed_number = int(input())

#Check if the user's guessed number is same as computer generated lucky number
if guessed_number == lucky_number:
    print("PRO GAMER!!!!! YOU WIN Rs. 2000000/-")
elif guessed_number != lucky_number:
    print("noob. YOU LOSE. The lucky number was", lucky_number)
