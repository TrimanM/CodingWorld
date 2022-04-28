#106. Program to draw a square using variables

import turtle as bot

#Define Variables
side = 200
angle = 90

# Setup the bot
bot.pencolor('red')
bot.pensize(10)

# Draw a square
bot.forward(side)
bot.left(angle)

bot.forward(side)
bot.left(angle)

bot.forward(side)
bot.left(angle)

bot.forward(side)
bot.left(angle)
