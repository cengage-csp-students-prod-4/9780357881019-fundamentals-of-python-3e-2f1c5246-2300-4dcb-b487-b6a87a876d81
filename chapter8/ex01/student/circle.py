"""
Program: circle.py
Michael Guillen

Defines a function that draws a circle with a turtle,
given the circle's center point and radius.
"""
import math
from turtle import Turtle

def drawCircle(t, x, y, radius):
    """Draws a circle with center (x, y) and the given radius."""
    distance = 2.0 * math.pi * radius / 120.0
    t.up()
    t.goto(x + radius, y)
    t.setheading(90)
    t.down()
    for count in range(120):
        t.left(3)
        t.forward(distance)

def main():
    t = Turtle()
    drawCircle(t, 0, 0, 100)

if __name__ == "__main__":
    main()
