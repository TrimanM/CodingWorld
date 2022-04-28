#401. Program to check if a number is even or odd.

#Input
print("Enter a number : ")
n = int(input())

#Calculate the remainder
remainder = n % 2

#Check if n is an even number
if remainder == 0:
    print(n, "is an even number")

#Check if n is an odd number
if remainder == 1:
    print(n, "is an odd number")
