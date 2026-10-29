"""
Program: posterize.py
Author: Michael Guillen

This program prompts the user for an image file name and an RGB
color, and converts the image to two colors: the given color
and white.
"""

from images import Image

def posterize(image, color):
   """Converts the argument image to two colors: the given
   RGB color and white."""
   whitePixel = (255, 255, 255)
   for y in range(image.getHeight()):
      for x in range(image.getWidth()):
         (r, g, b) = image.getPixel(x, y)
         average = (r + g + b) // 3
         if average < 128:
            image.setPixel(x, y, color)
         else:
            image.setPixel(x, y, whitePixel)

def main():
   filename = input("Enter the image file name: ")
   red = int(input("Enter an integer [0..255] for red: "))
   green = int(input("Enter an integer [0..255] for green: "))
   blue = int(input("Enter an integer [0..255] for blue: "))
   image = Image(filename)
   posterize(image, (red, green, blue))
   image.draw()

if __name__ == "__main__":
   main()
