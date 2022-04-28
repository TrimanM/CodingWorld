#403. Program to find the lowest of two numbers.

#Input
print("Enter the first number")
a = int(input())

print("Enter the second number")
b =  int(input())

#Check if a is lower
if a < b:
    print(a, "is lower than" ,b)

#Check if b is lower
if b < a:
    print(b, "is lower than" ,a)

#Check if both values are the same
if a == b:
    print("both numbers are the same")
