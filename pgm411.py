#411. Program to prompt and accept a number. If the number is even then draw a
#white square else if the number is odd then draw a black square.

#Import the module(s)
import turtle as bot

#Define variables
step = 100
angle = 90

#Get the input from the user
print("Enter a number : ")
n = int(input())

#Calculate the remainder
remainder = n % 2

#If even number
if remainder == 0:
    bot.pensize(10)
    bot.fillcolor('white')
    bot.begin_fill()
    bot.forward(step)
    bot.left(angle)
    bot.forward(step)
    bot.left(angle)
    bot.forward(step)
    bot.left(angle)
    bot.forward(step)
    bot.left(angle)
    bot.end_fill()
elif remainder == 1:
    bot.pensize(10)
    bot.fillcolor('black')
    bot.begin_fill()
    bot.forward(step)
    bot.left(angle)
    bot.forward(step)
    bot.left(angle)
    bot.forward(step)
    bot.left(angle)
    bot.forward(step)
    bot.left(angle)
    bot.end_fill()
