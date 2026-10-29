"""
Program: colorfilter.py
Author: Michael Guillen

Lightens, darkens, and color filters an image.
"""

from images import Image

def colorFilter(image, rgb):
   """Adjusts each pixel's RGB values by the amounts in the rgb tuple."""
   def limit(value):
      """Keeps a color value between 0 and 255."""
      return max(0, min(255, value))
   (redAmount, greenAmount, blueAmount) = rgb
   for y in range(image.getHeight()):
      for x in range(image.getWidth()):
         (r, g, b) = image.getPixel(x, y)
         r = limit(r + redAmount)
         g = limit(g + greenAmount)
         b = limit(b + blueAmount)
         image.setPixel(x, y, (r, g, b))

def lighten(image, amount):
   """Lightens the image by moving each pixel toward white."""
   colorFilter(image, (amount, amount, amount))

def darken(image, amount):
   """Darkens the image by moving each pixel toward black."""
   colorFilter(image, (-amount, -amount, -amount))

def main():
   filename = input("Enter the image file name: ")
   image = Image(filename)
   print("Close the image window to continue.")
   image.draw()
   lightImage = image.clone()
   lighten(lightImage, 64)
   print("Lightened. Close the image window to continue.")
   lightImage.draw()
   darkImage = image.clone()
   darken(darkImage, 64)
   print("Darkened. Close the image window to continue.")
   darkImage.draw()
   redImage = image.clone()
   colorFilter(redImage, (50, 0, 0))
   print("Red filter. Close the image window to quit.")
   redImage.draw()

if __name__ == "__main__":
   main()
