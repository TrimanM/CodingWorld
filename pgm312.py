# 312. Program to prompt and accept base and height of a triangle and calculate its area and perimeter.

#Initialisation
print("Enter the base :")
base = float(input())

print("Enter the height :")
height = float(input())

#Computation
area = (base * height) / 2
perimeter = base + (2 * height)

#Display
print(area, perimeter)