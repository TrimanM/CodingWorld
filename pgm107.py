# 107. Program to draw a rectangle using variables lenght, breadth and angle

import turtle as bot

#Define Variables
length = 200
breadth = 100
angle = 90

# Setup the bot
bot.pencolor('red')
bot.pensize(10)

# Draw a square
bot.forward(length)
bot.left(angle)

bot.forward(breadth)
bot.left(angle)

bot.forward(length)
bot.left(angle)

bot.forward(breadth)
bot.left(angle)
