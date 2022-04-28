#203. Program to draw a red square, blue rectangle, green triangle and
# orange circle

import turtle as bot

#Define variables
step = 100
angle = 90
tri_angle = 120

#Setup the bot for *square*
bot.pensize(10)
bot.pencolor('black')
bot.fillcolor('red')

#Code for *square*
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


#Setup the bot for *rectangle*
bot.pensize = 10
bot.pencolor('black')
bot.fillcolor('blue')
bot.penup()
bot.forward(step * 2)
bot.pendown()

#Code for *rectangle*
bot.begin_fill()

bot.forward(step)
bot.left(angle)

bot.forward(step * 2)
bot.left(angle)

bot.forward(step)
bot.left(angle)

bot.forward(step * 2)
bot.left(angle)

bot.end_fill()

#Setup the bot for *triangle*
bot.pensize = 10
bot.pencolor('black')
bot.fillcolor('green')
bot.penup()
bot.forward(step * 2)
bot.pendown()

#Code for *triangle*
bot.begin_fill()

bot.forward(step)
bot.left(tri_angle)

bot.forward(step)
bot.left(tri_angle)

bot.forward(step)
bot.left(tri_angle)

bot.end_fill()

#Setup the bot for *circle*
bot.pensize = 10
bot.pencolor('black')
bot.fillcolor('orange')
bot.penup()
bot.forward(step * 2)
bot.pendown()

#Code for *circle*
bot.begin_fill()

bot.circle(step)

bot.end_fill()
