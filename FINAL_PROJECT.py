'''
DO A MINI PROJECT with THE FOLLOWING FEATURES
'''

import math
import random
import turtle as bot
operation = 1

while operation != 0:
  # Step 1 - Display the title
  print("--------------------------------------------------")
  print("|               SIMPLE CALCULATOR                |")
  print("--------------------------------------------------")
  print("|                 1. Addition                    |")
  print("|                 2. Subtraction                 |")
  print("|                 3. Multiplication              |")
  print("|                 4. Division                    |")
  print("--------------------------------------------------")
  print("|     5. Area of Square                          |")
  print("|     6. Area of Rectangle                       |")
  print("|     7. Area of Triangle                        |")
  print("|     8. Area of Circle                          |")
  print("|     9. Volume of a sphere                      |")
  print("|    10. Surface Area of a Sphere.               |")
  print("--------------------------------------------------")
  print("|    11. Check if number is even or odd          |")
  print("|    12. Check if number is positive or negative |")
  print("|    13. Find greatest of two numbers            |")
  print("|    14. Find smallest of two numbers            |")
  print("|    15. Play Guess the number game              |")
  print("--------------------------------------------------")
  print("|    16. Draw a square                           |")
  print("|    17. Draw a rectangle                        |")
  print("|    18. Draw a triangle                         |")
  print("|    19. Draw a circle                           |")
  print("|    20. Draw a polygon                          |")
  print("--------------------------------------------------")
  print("|    21. Print numbers from 1 to n               |")
  print("|    22. Print even numbers from 1 to n          |")
  print("|    23. Print odd numbers from 1 to n           |")
  print("|    24. Print numbers from n to 1               |")
  print("--------------------------------------------------")
  print("|    25. Sum of numbers from 1 to n              |")
  print("|    26. Sum of even numbers from 1 to n         |")
  print("|    27. Sum of odd numbers from 1 to n          |")
  print("|    28. Product of numbers from 1 to n          |")
  print("--------------------------------------------------")
  print("|    29. Chessboard                              |")
  print("|    30. Ludoboard                               |")
  print("--------------------------------------------------")
  print("|                 0. EXIT                        |")
  print("--------------------------------------------------")

  # Step 2 - Prompt and accept the user's choice
  print("Enter which type of operation you would like to perform (1 - 10) : ")
  operation = int(input())
  
  # Step 3 - Process the choice
  if operation == 1:
    num_1 = int(input("Enter the first number : "))
    num_2 = int(input("Enter the second number : "))
    sum = num_1 + num_2
    print("The sum of", num_1, "and", num_2, "is", sum)
  
  elif operation == 2:
    num_1 = int(input("Enter the first number : "))
    num_2 = int(input("Enter the second number : "))
    difference = num_1 - num_2
    print("The difference between", num_1, "and", num_2, "is", difference)
  
  elif operation == 3:
    num_1 = int(input("Enter the first number : "))
    num_2 = int(input("Enter the second number : "))
    product = num_1 * num_2
    print("The product of", num_1, "and", num_2, "is", product)
  
  elif operation == 4:
    num_1 = int(input("Enter the first number : "))
    num_2 = int(input("Enter the second number : "))
    quotient = num_1 // num_2
    remainder = num_1 % num_2
    print("The quotient and remainder of", num_1, "and", num_2, "is =", quotient, "and", remainder, "respectivily")
  
  elif operation == 5:
    side = int(input("Enter the first number : "))
    area = side * side
    print("The area of the square with side", side, "is", area)
  
  elif operation == 6:
    length = int(input("Enter the first number : "))
    breadth = int(input("Enter the second number : "))
    area = length * breadth
    print("The area of the rectangle with side", length, "and", breadth, "is", area)
  
  elif operation == 7:
    base = int(input("Enter the first number : "))
    height = int(input("Enter the third number : "))
    area = (base * height) // 2
    print("The area of the triangle with side", length, "and", breadth, "is", area)
  
  elif operation == 8:
    radius = int(input("Enter the radius : "))
    area = math.pi * (radius * radius)
    print("The area of the circle with radius", radius, "is", area)

  elif operation == 9:
    # 4/3 (pie) r^3
    radius = int(input("Enter the radius : "))
    volume = (4/3) * math.pi * radius * radius * radius

  elif operation == 10:
    print("Enter the radius : ")
    radius = int(input())
    surface_area = 4 * 3.14 * radius * radius
    print("The surface area of the sphere is", surface_area)

  elif operation == 11:
    num = int(input("Enter a number : "))
    if num % 2 == 0:
      print("The number is even")
    else:
      print("The number is odd")

  elif operation == 12:
    num = int(input("Enter a number"))
    if num > 0:
      print("The number is positive")
    elif num < 0:
      print("The number is negative")
    else:
      print("The number is neither positive not regative")

  elif operation == 13:
    num_1 = int(input("Enter the first number"))
    num_2 = int(input("Enter the second number"))

    if num_1 > num_2:
      print("The first number is greater")
    elif num_1 < num_2:
      print("The second number is greater")
    else:
      print("Both the numbers are equal")

  elif operation == 14:
    num_1 = int(input("Enter the first number"))
    num_2 = int(input("Enter the second number"))

    if num_1 > num_2:
      print("The second number is smaller")
    elif num_1 < num_2:
      print("The first number is smaller")
    else:
      print("Both the numbers are equal")

  elif operation == 15:
    rand_num = random.randint(1, 10)
    guess = int(input("Guess a number from 1 to 10 : "))
    if guess == rand_num:
      print("YOU WIN!")
    else:
      print("YOU LOSE! The number was", rand_num)
      
  elif operation == 16:
    counter = 1
    step = 100
    angle = 90
    while counter <= 5:
      bot.forward(step)
      bot.right(angle)
      counter = counter + 1
  elif operation == 17:
    length = 100
    breadth = 50
    angle = 90
    counter = 1

    while counter <= 4:
      if counter % 2 == 1:
        bot.forward(length)
        bot.left(angle)
        counter = counter + 1
      if counter % 2 == 0:
        bot.forward(breadth)
        bot.left(angle)
        counter = counter + 1
  elif operation == 18:
    step = 100
    angle = 360 / 3
    counter = 1

    while counter <= 3:
      bot.forward(step)
      bot.left(angle)
      counter = counter + 1
  elif operation == 19:
    step = 50
    bot.circle(step)
  elif operation == 20:
    sides = int(input("Number of sides you woulf like yout polygon to have : "))
    counter = 1
    step = 50
    angle = 360 / sides

    while counter <= sides:
      bot.forward(step)
      bot.left(angle)
      counter = counter + 1
  elif operation == 21:
    n = int(input("Enter the number : "))
    counter = 1
    while counter <= n:
      print(counter)
      counter = counter + 1
  elif operation == 22:
    n = int(input("Enter the number : "))
    counter = 1
    while counter <= n:
      if counter % 2 == 0:
        print(counter)
      counter = counter + 1
      
  elif operation == 23:
    n = int(input("Enter the number : "))
    counter = 1
    while counter <= n:
      if counter % 2 == 1:
        print(counter)
      counter = counter + 1
  elif operation == 24:
    n = int(input("Enter the number : "))
    counter = 1
    while n >= counter:
      print(n)
      n = n - 1
  elif operation == 25:
    n = int(input("Enter the number : "))
    sum = 0
    counter = 1
    while counter <= n:
      sum = sum + counter
      counter = counter + 1
    print("The sum of all the numbers from 1 to", n, "is", sum)

  elif operation == 26:
    n = int(input("Enter the number : "))
    sum = 0
    counter = 1

    while counter <= n:
      if counter % 2 == 0:
        sum = sum + counter
      counter = counter + 1

    print("The sum of the even numbers from 1 to", n, "is", sum)

  elif operation == 27:
    n = int(input("Enter the number : "))
    sum = 0
    counter = 1

    while counter <= n:
      if counter % 2 == 1:
        sum = sum + counter
      counter = counter + 1
      
    print("The sum of the odd numbers from 1 to", n, "is", sum)
    
  elif operation == 28:
    n = int(input("Enter the number : "))
    product = 1
    counter = 1
    while counter <= n:
      product = product * counter
      counter = counter + 1
    print("The product of all the numbers from 1 to", n, "is", product)
  elif operation == 29:
    bot.speed = 100
    counter = 1
    step = 10
    angle = 90

    while counter <= 8:
      if counter % 2 != 0:
        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)
      if counter % 2 == 0:
        bot.begin_fill()
        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)
        bot.end_fill()

      bot.penup()
      bot.forward(step)
      bot.pendown()

      counter = counter + 1

    bot.penup()
    bot.backward(step * 8)
    bot.right(angle)
    bot.forward(step)
    bot.left(angle)
    bot.pendown()

    counter = 1
    while counter <= 8:
      if counter % 2 == 0:
        bot.forward(step)
        bot.right(angle)
        bot.forward(step)
        bot.right(angle)
  
        bot.forward(step)
        bot.right(angle)
  
        bot.forward(step)
        bot.right(angle)
  
      if counter % 2 != 0:
        bot.begin_fill()
        bot.forward(step)
        bot.right(angle)
  
        bot.forward(step)
        bot.right(angle)
  
        bot.forward(step)
        bot.right(angle)
  
        bot.forward(step)
        bot.right(angle)
        bot.end_fill()
  
      bot.penup()
      bot.forward(step)
      bot.pendown()
      
      counter = counter + 1

    bot.penup()
    bot.backward(step * 8)
    bot.right(angle)
    bot.forward(step)
    bot.left(angle)
    bot.pendown()

    counter = 1
    
    while counter <= 8:
      if counter % 2 != 0:
        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)
      if counter % 2 == 0:
        bot.begin_fill()
        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)
        bot.end_fill()

      bot.penup()
      bot.forward(step)
      bot.pendown()

      counter = counter + 1

    bot.penup()
    bot.backward(step * 8)
    bot.right(angle)
    bot.forward(step)
    bot.left(angle)
    bot.pendown()

    counter = 1

    while counter <= 8:
      if counter % 2 == 0:
        bot.forward(step)
        bot.right(angle)
        bot.forward(step)
        bot.right(angle)
  
        bot.forward(step)
        bot.right(angle)
  
        bot.forward(step)
        bot.right(angle)
  
      if counter % 2 != 0:
        bot.begin_fill()
        bot.forward(step)
        bot.right(angle)
  
        bot.forward(step)
        bot.right(angle)
  
        bot.forward(step)
        bot.right(angle)
  
        bot.forward(step)
        bot.right(angle)
        bot.end_fill()
  
      bot.penup()
      bot.forward(step)
      bot.pendown()
      
      counter = counter + 1

    bot.penup()
    bot.backward(step * 8)
    bot.right(angle)
    bot.forward(step)
    bot.left(angle)
    bot.pendown()

    counter = 1

    while counter <= 8:
      if counter % 2 != 0:
        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)
      if counter % 2 == 0:
        bot.begin_fill()
        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)

        bot.forward(step)
        bot.right(angle)
        bot.end_fill()

      bot.penup()
      bot.forward(step)
      bot.pendown()

      counter = counter + 1

    bot.penup()
    bot.backward(step * 8)
    bot.right(angle)
    bot.forward(step)
    bot.left(angle)
    bot.pendown()

    counter = 1
  elif operation == 30:
    # Still working on this using IDLE
    
    bot.speed(50)
    counter = 1
    step = 25
    angle = 90
    tri_angle = 360 / 3

    # Red big square
    bot.fillcolor('red')
    bot.begin_fill()
    while counter <= 4:
        bot.forward(step * 5)
        bot.left(angle)

        counter = counter + 1
    bot.end_fill()
    #---------------------------

    bot.penup()
    bot.forward(step * 5)

    bot.left(90)
    bot.forward(step * 4)
    bot.right(90)

    bot.pendown()

    counter = 1
    while counter <= 4:
        bot.forward(step)
        bot.left(angle)

        counter = counter + 1
    bot.penup()
    bot.forward(step)
    bot.pendown()

    counter = 1
    while counter <= 4:
        bot.forward(step)
        bot.left(angle)

        counter = counter + 1
    bot.penup()
    bot.forward(step)
    bot.pendown()

    counter = 1
    while counter <= 4:
        bot.forward(step)
        bot.left(angle)

        counter = counter + 1
    bot.penup()
    bot.forward(step)
    bot.pendown()


    # Green big square
    counter = 1
    bot.fillcolor('green')
    bot.begin_fill()
    while counter <= 4:
        bot.forward(step * 5)
        bot.left(angle)

        counter = counter + 1
    bot.end_fill()
    #-----------------------------

    bot.penup()
    bot.right(90)
    bot.forward(step * 8)
    bot.left(90)
    bot.pendown()

    # Yellow big square
    counter = 1
    bot.fillcolor('yellow')
    bot.begin_fill()
    while counter <= 4:
        bot.forward(step * 5)
        bot.left(angle)

        counter = counter + 1
    bot.end_fill()
    #----------------------------

    bot.penup()
    bot.left(180)
    bot.forward(step * 8)
    bot.left(180)
    bot.pendown()

    # Blue big square
    counter = 1
    bot.fillcolor('blue')
    bot.begin_fill()
    while counter <= 4:
        bot.forward(step * 5)
        bot.left(angle)

        counter = counter + 1
    bot.end_fill()
    #------------------------------

    bot.penup()
    bot.left(90)
    bot.forward(step * 9)
    bot.right(90)
    bot.forward(step)
    bot.pendown()

    #------------------------------
    # Red circles

    bot.circle(20)

    bot.penup()
    bot.forward(75)
    bot.pendown()

    bot.circle(20)

    bot.penup()
    bot.forward(20)
    bot.left(90)
    bot.forward(75)
    bot.pendown()

    bot.circle(20)

    bot.penup()
    bot.left(90)
    bot.forward(115)
    bot.left(90)
    bot.pendown()

    bot.circle(20)
    #------------------------
    # Green circles
    
  elif operation == 0:
    print("OK")

  
  else:
    print("INVALID CHOICE")

print("--------------------------------------------------")
print("|                T H A N K  Y O U                |")
print("--------------------------------------------------")
