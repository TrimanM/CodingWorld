#402. Program to find the greatest of two numbers.

#Input
print("Enter the first number")
a = int(input())

print("Enter the second number")
b =  int(input())

#Check if a is greater
if a > b:
    print(a, "is greater than" ,b)

#Check if b is greater
if b > a:
    print(b, "is greater then" ,a)

#Check if both values are the same
if a == b:
    print("both numbers are the same")
