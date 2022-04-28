#404. Program to check if a number is positive or negative

#Input
print("Enter the number : ")
n = int(input())

#Check if n is a positive number
if n > 0:
    print(n, "is a positive number")

#Check if it a negative number
if n < 0:
    print(n, "is a negative number")

#Check if n is neither positive nor negative
if n == 0:
    print(n, "is neither positive nor negative")
