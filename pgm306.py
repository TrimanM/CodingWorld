#306. Program prompt and accept two numbers from user and find the quotient and
#remainder

#Initialisation
print("Enter the first number : ")
a = int(input())

print("Enter the second number : ")
b = int(input())

#Computation
quotient = a / b
remainder = a % b

#Display
print("The quotient of", a, "and", b, "is =", quotient, "and the remainder is", remainder)
