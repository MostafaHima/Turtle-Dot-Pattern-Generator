import turtle
from turtle import Turtle, Screen
import random


# Function to generate a random color
def generate_random_color():
    colors = []
    for c in range(3):
        color_value = random.randint(0, 255)  # Random value for each color component (R, G, B)
        colors.append(color_value)
    return tuple(colors)


# Set up the screen and turtle
turtle_screen = Screen()
turtle_screen.setup(800, 700)
turtle_screen.colormode(255)  # Enable RGB color mode

t = Turtle()
t.hideturtle()
t.shape("turtle")
t.speed(0)
t.penup()  # To avoid drawing unnecessary lines
t.goto(-390, -330)  # Starting position of the turtle

# Loop to draw the dots in rows
work = 0
while work <= 33:
    work += 1
    for i in range(38):  # Loop to create 38 dots in one row
        t.penup()
        t.forward(20)  # Move forward by 20 units
        t.pendown()  # Start drawing
        t.dot(14, generate_random_color())  # Draw a dot with random color

    t.penup()  # Lift pen to move to the next row
    t.goto(-390, t.ycor() + 20)  # Move the turtle to the start of the next row
    t.setheading(360)  # Ensure the turtle is facing right before starting the next row

turtle_screen.mainloop()







