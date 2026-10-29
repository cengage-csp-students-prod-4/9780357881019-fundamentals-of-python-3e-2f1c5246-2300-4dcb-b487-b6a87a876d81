"""
Program: grayscale.py
Author: Michael Guillen

Converts an image to grayscale by averaging and by luminance.
"""

from images import Image

def grayscale1(image):
   """Converts the image to grayscale using luminance."""
   for y in range(image.getHeight()):
      for x in range(image.getWidth()):
         (r, g, b) = image.getPixel(x, y)
         r = int(r * 0.299)
         g = int(g * 0.587)
         b = int(b * 0.114)
         lum = r + g + b
         image.setPixel(x, y, (lum, lum, lum))

def grayscale2(image):
   """Converts the image to grayscale by averaging RGB values."""
   for y in range(image.getHeight()):
      for x in range(image.getWidth()):
         (r, g, b) = image.getPixel(x, y)
         average = (r + g + b) // 3
         image.setPixel(x, y, (average, average, average))

def main():
   filename = input("Enter the image file name: ")
   image = Image(filename)
   copy = image.clone()
   grayscale2(image)
   print("Averaging version. Close the image window to continue.")
   image.draw()
   grayscale1(copy)
   print("Luminance version. Close the image window to quit.")
   copy.draw()

if __name__ == "__main__":
   main()
