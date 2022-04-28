'''405. Program to prompt and accept a number from 1 to 7 and print the day of week
If input is 1 then output is Monday
If input is 2 then output is Tuesday
If input is 7 then output is Sunday
If input is greater than 7 or less than 1 then output is INVALID INPUT
'''

print("Enter a number from 1-7 : ")
n = int(input())

if n == 1:
    print("It is Monday")
elif n == 2:
    print("It is Tuesday")
elif n == 3:
    print("It is Wednesday")
elif n == 4:
    print("It is Thursday")
elif n == 5:
    print("It is Friday")
elif n == 6:
    print("It is Saturday")
elif n == 7:
    print("It is Sunday")
else:
    print("INVALID INPUT")
