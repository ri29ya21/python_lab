#Program 11: Interactive Turtle Pattern Generator and Fractal Renderer

import turtle
import math

screen = turtle.Screen()
screen.title("Turtle Pattern Generator")
screen.bgcolor("black")
screen.setup(width=800, height=700)

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.color("cyan")


def draw_spiral(length, angle, steps):
    for _ in range(steps):
        pen.forward(length)
        pen.right(angle)
        length += 2


def draw_polygon(sides, length):
    if sides < 3:
        print("A polygon needs at least 3 sides.")
        return

    angle = 360 / sides
    for _ in range(sides):
        pen.forward(length)
        pen.right(angle)


def koch_curve(length, depth):
    if depth == 0:
        pen.forward(length)
    else:
        length /= 3
        koch_curve(length, depth - 1)
        pen.left(60)
        koch_curve(length, depth - 1)
        pen.right(120)
        koch_curve(length, depth - 1)
        pen.left(60)
        koch_curve(length, depth - 1)


def koch_snowflake(length, depth):
    pen.penup()
    pen.goto(-length / 2, length / 3)
    pen.pendown()
    for _ in range(3):
        koch_curve(length, depth)
        pen.right(120)


def draw_spiral_pattern():
    colors = ["red", "orange", "yellow", "green",
              "cyan", "blue", "magenta"]
    for i in range(120):
        pen.color(colors[i % len(colors)])
        pen.forward(i * 2)
        pen.right(91)


print("Turtle Pattern Generator")
print("1. Draw Polygon")
print("2. Draw Spiral")
print("3. Draw Koch Snowflake")

choice = input("Enter your choice (1-3): ")

pen.penup()
pen.goto(0, 0)
pen.pendown()

if choice == "1":
    sides = int(input("Enter number of sides: "))
    length = int(input("Enter side length: "))
    draw_polygon(sides, length)

elif choice == "2":
    draw_spiral_pattern()

elif choice == "3":
    length = int(input("Enter snowflake size: "))
    depth = int(input("Enter recursion depth (0-4 recommended): "))
    if length > 0 and 0 <= depth <= 5:
        koch_snowflake(length, depth)
    else:
        print("Enter a positive size and depth from 0 to 5.")

else:
    print("Invalid choice.")

turtle.done()