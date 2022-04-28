# 311. Program to prompt and accept length and breadth of a rectangle and calculate its area and perimeter

#Initialisation
print("Enter the length :")
length = float(input())

print("Enter the breadth :")
breadth = float(input())

#Computation
area = length * breadth
perimeter = 2 * (length + breadth)

#Display
print("Area of rectangle is :", area, "and perimeter of rectangle is :", perimeter)