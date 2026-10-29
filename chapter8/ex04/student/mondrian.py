"""
Program: mondrian.py
Author: Michael Guillen

This program prompts the user for a level and draws
a Mondrian-style pattern of that level.
"""

import random
from turtle import Turtle, tracer, update, window_width, window_height

def randomColor():
   """Returns a random color."""
   return (random.randint(0, 255),
           random.randint(0, 255),
           random.randint(0, 255))

def drawRectangle(t, x, y, width, height):
   """Draws a filled rectangle in a random color."""
   color = randomColor()
   t.pencolor(color)
   t.fillcolor(color)
   t.up()
   t.goto(x, y)
   t.setheading(0)
   t.down()
   t.begin_fill()
   for count in range(2):
      t.forward(width)
      t.right(90)
      t.forward(height)
      t.right(90)
   t.end_fill()

def mondrian(t, x, y, width, height, level, vertical):
   """Draws the pattern of the given level."""
   if level == 0:
      return
   elif vertical:
      third = width / 3
      drawRectangle(t, x + third, y, width - third, height)
      mondrian(t, x, y, third, height, level - 1, True)
      mondrian(t, x + third, y, width - third, height, level - 1, False)
   else:
      third = height / 3
      drawRectangle(t, x, y - third, width, height - third)
      mondrian(t, x, y, width, third, level - 1, False)
      mondrian(t, x, y - third, width, height - third, level - 1, True)

def main():
   level = int(input("Enter the level (0 or greater): "))
   t = Turtle()
   if level > 6:
      tracer(False)
   t.speed(0)
   t.hideturtle()
   width = window_width()
   height = window_height()
   drawRectangle(t, -width / 2, height / 2, width, height)
   mondrian(t, -width / 2, height / 2, width, height, level, False)
   if level > 6:
      update()
   input("Press Enter to quit: ")

if __name__ == "__main__":
   main()
