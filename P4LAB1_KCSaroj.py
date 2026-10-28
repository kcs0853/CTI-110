# Saroj KC
# 27 October 2026
# P4LAB1_KCSaroj
# Use turtle and loops to draw a square and a triangle

# Pseudocode:
# 1. Import the turtle module.
# 2. Create a screen and change the background color.
# 3. Create a turtle and change its color.
# 4. Move the turtle to the starting position.
# 5. Use a FOR loop to draw a square (house body).
# 6. Move the turtle to the top of the square.
# 7. Use a WHILE loop to draw a triangle (house roof).
# 8. Keep the graphics window open until closed.

import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create turtle
house = turtle.Turtle()
house.color("green")
house.pensize(3)

# Move turtle to starting position
house.penup()
house.goto(-50, -50)
house.pendown()

# Draw square using a for loop
for side in range(4):
    house.forward(100)
    house.left(90)

# Move to top-left corner of square
house.goto(-50, 50)

# Draw triangle using a while loop
count = 0
while count < 3:
    house.forward(100)
    house.left(120)
    count += 1

# Keep window open
turtle.done()