"""
Program: invert.py
Author: Michael Guillen

Inverts color, grayscale, and black and white images.
"""

from images import Image

def invert(image):
   """Resets each RGB component to 255 minus that component."""
   for y in range(image.getHeight()):
      for x in range(image.getWidth()):
         (r, g, b) = image.getPixel(x, y)
         image.setPixel(x, y, (255 - r, 255 - g, 255 - b))

def grayscale(image):
   """Converts the image to grayscale using luminance."""
   for y in range(image.getHeight()):
      for x in range(image.getWidth()):
         (r, g, b) = image.getPixel(x, y)
         r = int(r * 0.299)
         g = int(g * 0.587)
         b = int(b * 0.114)
         lum = r + g + b
         image.setPixel(x, y, (lum, lum, lum))

def blackAndWhite(image):
   """Converts the image to black and white."""
   blackPixel = (0, 0, 0)
   whitePixel = (255, 255, 255)
   for y in range(image.getHeight()):
      for x in range(image.getWidth()):
         (r, g, b) = image.getPixel(x, y)
         average = (r + g + b) // 3
         if average < 128:
            image.setPixel(x, y, blackPixel)
         else:
            image.setPixel(x, y, whitePixel)

def main():
   filename = input("Enter the image file name: ")
   image = Image(filename)
   gray = image.clone()
   grayscale(gray)
   blackWhite = image.clone()
   blackAndWhite(blackWhite)
   invert(image)
   print("Inverted color image. Close the image window to continue.")
   image.draw()
   invert(gray)
   print("Inverted grayscale image. Close the image window to continue.")
   gray.draw()
   invert(blackWhite)
   print("Inverted black and white image. Close the image window to quit.")
   blackWhite.draw()

if __name__ == "__main__":
   main()
