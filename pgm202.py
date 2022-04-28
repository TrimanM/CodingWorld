#202. Program to draw a blue rectangle with red border

import turtle as bot

#Define variables
step = 100
length = step * 2
angle = 90

#Setup the bot
bot.pensize(10)
bot.pencolor('red')
bot.fillcolor('blue')

#Draw a blue rectangle with red border
bot.begin_fill()

bot.forward(step)
bot.right(angle)

bot.forward(length)
bot.right(angle)

bot.forward(step)
bot.right(angle)

bot.forward(length)
bot.right(angle)

bot.end_fill()
