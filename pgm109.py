# Date - 18/4/22 - Version 0.1
#109. Homework Program to draw the following shapes one after the other
# with different colors. All shapes in one program (Use suitable variables)
# Square
# Rectangle
# Triangle
# Circle
# Pentagon
# Hexagon
# Heptagon
# Octagon
# Nonagon
# Decagon

import turtle as bot

# Define the variables
length = 100
breadth = 50
square_rect_angle = 90
tri_angle = 360/3
pent_angle = 360/5
hexa_angle = 360/6
hept_angle = 360/7
oct_angle = 360/8
non_angle = 360/9
dec_angle = 360/10

# Setup the bot for *square*
bot.pencolor('blue')
bot.pensize(10)

# Code for *square*
bot.forward(length)
bot.left(square_rect_angle)

bot.forward(length)
bot.left(square_rect_angle)

bot.forward(length)
bot.left(square_rect_angle)

bot.forward(length)
bot.left(square_rect_angle)

# Setup the bot for *rectangle*
bot.pencolor('red')
bot.penup()
bot.forward(200)
bot.pendown()

# Code for *rectangle*
bot.forward(length)
bot.left(square_rect_angle)

bot.forward(breadth)
bot.left(square_rect_angle)

bot.forward(length)
bot.left(square_rect_angle)

bot.forward(breadth)
bot.left(square_rect_angle)

# Setup the bot for *triangle*
bot.pencolor('green')
bot.penup()
bot.forward(200)
bot.pendown()

# Code for *triangle*
bot.forward(length)
bot.left(tri_angle)

bot.forward(length)
bot.left(tri_angle)

bot.forward(length)
bot.left(tri_angle)

# Setup for *circle*
bot.pencolor('cyan')
bot.penup()
bot.forward(200)
bot.pendown()

# Code for *circle*
bot.circle(50)

# Setup for *pentagon*
bot.pencolor('pink')
bot.penup()
bot.forward(125)
bot.pendown()

# Code for *pentagon*
bot.forward(length)
bot.left(pent_angle)

bot.forward(length)
bot.left(pent_angle)

bot.forward(length)
bot.left(pent_angle)

bot.forward(length)
bot.left(pent_angle)

bot.forward(length)
bot.left(pent_angle)

# Setup for *hexagon*
bot.pencolor('yellow')
bot.penup()
bot.right(90)
bot.forward(300)
bot.left(90)
bot.pendown()

# Code for *hexagon*
bot.forward(length)
bot.left(hexa_angle)

bot.forward(length)
bot.left(hexa_angle)

bot.forward(length)
bot.left(hexa_angle)

bot.forward(length)
bot.left(hexa_angle)

bot.forward(length)
bot.left(hexa_angle)

bot.forward(length)
bot.left(hexa_angle)

# Setup for *heptagon*
bot.pencolor('orange')
bot.penup()
bot.forward(-300)
bot.pendown()

# Code for *heptagon*
bot.forward(length)
bot.left(hept_angle)

bot.forward(length)
bot.left(hept_angle)

bot.forward(length)
bot.left(hept_angle)

bot.forward(length)
bot.left(hept_angle)

bot.forward(length)
bot.left(hept_angle)

bot.forward(length)
bot.left(hept_angle)

bot.forward(length)
bot.left(hept_angle)

# Setup for *oactagon*
bot.pencolor('brown')
bot.penup()
bot.forward(-300)
bot.pendown()

# Code for *octagon*
bot.forward(length)
bot.left(oct_angle)

bot.forward(length)
bot.left(oct_angle)

bot.forward(length)
bot.left(oct_angle)

bot.forward(length)
bot.left(oct_angle)

bot.forward(length)
bot.left(oct_angle)

bot.forward(length)
bot.left(oct_angle)

bot.forward(length)
bot.left(oct_angle)

bot.forward(length)
bot.left(oct_angle)

# Setup for *nonagon*
bot.pencolor('purple')
bot.penup()
bot.forward(-300)
bot.pendown()

# Code for *nonagon*
bot.forward(length)
bot.left(non_angle)

bot.forward(length)
bot.left(non_angle)

bot.forward(length)
bot.left(non_angle)

bot.forward(length)
bot.left(non_angle)

bot.forward(length)
bot.left(non_angle)

bot.forward(length)
bot.left(non_angle)

bot.forward(length)
bot.left(non_angle)

bot.forward(length)
bot.left(non_angle)

bot.forward(length)
bot.left(non_angle)

# Setup for *decagon*
bot.pencolor('black')
bot.penup()
bot.forward(-350)
bot.pendown()

# Code for *decagon*
bot.forward(length)
bot.left(dec_angle)

bot.forward(length)
bot.left(dec_angle)

bot.forward(length)
bot.left(dec_angle)

bot.forward(length)
bot.left(dec_angle)

bot.forward(length)
bot.left(dec_angle)

bot.forward(length)
bot.left(dec_angle)

bot.forward(length)
bot.left(dec_angle)

bot.forward(length)
bot.left(dec_angle)

bot.forward(length)
bot.left(dec_angle)

bot.forward(length)
bot.left(dec_angle)
