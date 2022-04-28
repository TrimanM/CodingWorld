'''
#409. Program to prompt and accept a number in the range of 1 to 12 and display
month of the year.
If the input is 1 then the output is January
If the input is 2 then the output is February
If the input is 12 then the output is December
If the input is less than 1 or greater than 12 then the output is INVALID INPUT.
'''

#Input
print("Enter a number in the range of 1-7 : ")
n = int(input())

#Check the month
if n == 1:
    print("The month is January")
elif n == 2:
    print("The month is February")
elif n == 3:
    print("The month is March")
elif n == 4:
    print("The month is April")
elif n == 5:
    print("The month is May")
elif n == 6:
    print("The month is June")
elif n == 7:
    print("The month is July")
elif n == 8:
    print("The month is August")
elif n == 9:
    print("The month is September")
elif n == 10:
    print("The month is October")
elif n == 11:
    print("The month is November")
elif n == 12:
    print("The month is December")
else:
    print("INVALID INPUT")
