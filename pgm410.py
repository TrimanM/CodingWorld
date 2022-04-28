'''
#410. Program to prompt to prompt and accept a number in the range of 1 to 10 and
display the shapes based on the input.
If the input is 1 then draw a square
If the input is 2 then draw a rectangle
If the input is 3 then draw a triangle
If the input is 4 then draw a circle
If the input is 5 then draw a pentagon
If the input is 6 then draw a hexagon
If the input is 7 then draw a heptagon
If the input is 8 then draw a octagon
If the input is 9 then draw a nonagon
If the input is 10 then draw a decagon
'''

#Import Modules
import turtle as bot

#Define Variables
step = 100
square_rect_angle = 90
tri_angle = 360/3
pent_angle = 360/5
hex_angle = 360/6
hept_angle = 360/7
oct_angle = 360/8
non_angle = 360/9
dec_angle = 360/10

#Setup the bot
bot.pensize(10)

#Get the input
print("Enter a number in the range of 1-10")
n = int(input())

#Draw the shapes based on the input
if n == 1:
    bot.forward(step)
    bot.left(square_rect_angle)

    bot.forward(step)
    bot.left(square_rect_angle)

    bot.forward(step)
    bot.left(square_rect_angle)

    bot.forward(step)
    bot.left(square_rect_angle)
elif n == 2:
    bot.forward(step)
    bot.left(square_rect_angle)

    bot.forward(step * 2)
    bot.left(square_rect_angle)

    bot.forward(step)
    bot.left(square_rect_angle)

    bot.forward(step * 2)
    bot.left(square_rect_angle)
elif n == 3:
    bot.forward(step)
    bot.left(tri_angle)

    bot.forward(step)
    bot.left(tri_angle)

    bot.forward(step)
    bot.left(tri_angle)
elif n == 4:
    bot.circle(step)
elif n == 5:
    bot.forward(step)
    bot.left(pent_angle)

    bot.forward(step)
    bot.left(pent_angle)

    bot.forward(step)
    bot.left(pent_angle)

    bot.forward(step)
    bot.left(pent_angle)

    bot.forward(step)
    bot.left(pent_angle)
elif n == 6:
    bot.forward(step)
    bot.left(hex_angle)

    bot.forward(step)
    bot.left(hex_angle)

    bot.forward(step)
    bot.left(hex_angle)

    bot.forward(step)
    bot.left(hex_angle)

    bot.forward(step)
    bot.left(hex_angle)

    bot.forward(step)
    bot.left(hex_angle)
elif n == 7:
    bot.forward(step)
    bot.left(hept_angle)

    bot.forward(step)
    bot.left(hept_angle)

    bot.forward(step)
    bot.left(hept_angle)

    bot.forward(step)
    bot.left(hept_angle)

    bot.forward(step)
    bot.left(hept_angle)

    bot.forward(step)
    bot.left(hept_angle)

    bot.forward(step)
    bot.left(hept_angle)
elif n == 8:
    bot.forward(step)
    bot.left(oct_angle)

    bot.forward(step)
    bot.left(oct_angle)

    bot.forward(step)
    bot.left(oct_angle)

    bot.forward(step)
    bot.left(oct_angle)

    bot.forward(step)
    bot.left(oct_angle)

    bot.forward(step)
    bot.left(oct_angle)

    bot.forward(step)
    bot.left(oct_angle)

    bot.forward(step)
    bot.left(oct_angle)
elif n == 9:
    bot.forward(step)
    bot.left(non_angle)

    bot.forward(step)
    bot.left(non_angle)

    bot.forward(step)
    bot.left(non_angle)

    bot.forward(step)
    bot.left(non_angle)

    bot.forward(step)
    bot.left(non_angle)

    bot.forward(step)
    bot.left(non_angle)

    bot.forward(step)
    bot.left(non_angle)

    bot.forward(step)
    bot.left(non_angle)

    bot.forward(step)
    bot.left(non_angle)
elif n == 10:
    bot.forward(step)
    bot.left(dec_angle)

    bot.forward(step)
    bot.left(dec_angle)

    bot.forward(step)
    bot.left(dec_angle)

    bot.forward(step)
    bot.left(dec_angle)

    bot.forward(step)
    bot.left(dec_angle)

    bot.forward(step)
    bot.left(dec_angle)

    bot.forward(step)
    bot.left(dec_angle)

    bot.forward(step)
    bot.left(dec_angle)

    bot.forward(step)
    bot.left(dec_angle)

    bot.forward(step)
    bot.left(dec_angle)
else:
    print("INVALID INPUT")
