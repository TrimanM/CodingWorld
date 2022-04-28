#305. Program to prompt and accept three numbers from user and find the product.

#Initialisation
print("Enter the first number : ")
first_number = input()
a = int(first_number)

print("Enter the second number : ")
second_number = input()
b = int(second_number)

print("Enter the third number : ")
third_number = input()
c = int(third_number)

#Computation
product = a * b * c

#Display
print("The product of", a, "and", b, "and", c, "is =", product)
