#203. Program to draw a green triangle with blue border

import turtle as bot

#Define variables
step = 100
angle = 120

#Setup the bot
bot.pensize(10)
bot.pencolor('blue')
bot.fillcolor('green')

#Draw green triangle with blue border
bot.begin_fill()

bot.forward(step)
bot.left(angle)

bot.forward(step)
bot.left(angle)

bot.forward(step)
bot.left(angle)

bot.end_fill()
