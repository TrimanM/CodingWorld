#201. Program to draw a red square with black border

import turtle as bot

#Define variables
step = 100
angle = 90

#Setup the bot
bot.pensize(10)
bot.pencolor('black')
bot.fillcolor('red')

#Draw red square with black border
bot.begin_fill()

bot.forward(step)
bot.right(angle)

bot.forward(step)
bot.right(angle)

bot.forward(step)
bot.right(angle)

bot.forward(step)
bot.right(angle)

bot.end_fill()
