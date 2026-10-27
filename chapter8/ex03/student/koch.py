"""
Program: koch.py
Author: Michael Guillen

This program prompts the user for the level of
a Koch snowflake and draws a snowflake of that level.
"""

from turtle import Turtle, tracer, update

def drawFractalLine(t, distance, angle, level):
   """Draws a fractal line of the given distance, angle, and level."""
   if level == 0:
      t.setheading(angle)
      t.forward(distance)
   else:
      drawFractalLine(t, distance / 3, angle, level - 1)
      drawFractalLine(t, distance / 3, angle + 60, level - 1)
      drawFractalLine(t, distance / 3, angle - 60, level - 1)
      drawFractalLine(t, distance / 3, angle, level - 1)

def main():
   level = int(input("Enter the level (0 or greater): "))
   t = Turtle()
   if level > 4:
      tracer(False)
   t.speed(0)
   t.hideturtle()
   t.up()
   t.goto(-100, 60)
   t.down()
   distance = 200
   drawFractalLine(t, distance, 0, level)
   drawFractalLine(t, distance, -120, level)
   drawFractalLine(t, distance, 120, level)
   if level > 4:
      update()
   input("Press Enter to quit: ")

if __name__ == "__main__":
   main()
