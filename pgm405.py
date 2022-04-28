'''
405. Program to prompt and accept a number from 1 to 7 and print the day of week

If input is 1 then output is Monday
If input is 2 then output is Tuesday
If input is 7 then output is Sunday
If input is greater than 7 or less than 1 then output is INVALID INPUT
'''

#Input
print("Choose a number from 1-7 : ")
n = int(input())

#Check which day of the week it is
if n == 1:
    print("It is Monday")

if n == 2:
    print("It is Tuesday")

if n == 3:
    print("It is Wednesday")

if n == 4:
    print("It is Thursday")

if n == 5:
    print("It is Friday")

if n == 6:
    print("It is Saturday")

if n == 7:
    print("It is Sunday")

#INVALID INPUTS
if n < 1 or n > 7:
    print("INVALID INPUT")
