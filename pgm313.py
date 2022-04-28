# 313. Program to prompt and accept radius of a circle and calculate its area and circumference.

#Initialisation
print("Enter the radius :")
radius = float(input())

#Computation
area = 3.14 * (radius * radius)
circumference = 3.14 * (radius * 2)

#Display
print("Area of circle is =", area, "and circumference of circle is =", circumference)