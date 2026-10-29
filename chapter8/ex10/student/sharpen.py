"""
Program: sharpen.py
Author: Michael Guillen

Sharpens the edges in a color image.
"""

from images import Image

def sharpen(image, degree, threshold):
   """Returns a copy of the image with its edges darkened by degree."""
   def average(triple):
      """Returns the average of an RGB triple."""
      (r, g, b) = triple
      return (r + g + b) // 3
   new = image.clone()
   for y in range(image.getHeight() - 1):
      for x in range(1, image.getWidth()):
         oldPixel = image.getPixel(x, y)
         leftPixel = image.getPixel(x - 1, y)
         bottomPixel = image.getPixel(x, y + 1)
         oldLum = average(oldPixel)
         leftLum = average(leftPixel)
         bottomLum = average(bottomPixel)
         if abs(oldLum - leftLum) > threshold or \
            abs(oldLum - bottomLum) > threshold:
            (r, g, b) = oldPixel
            r = max(0, r - degree)
            g = max(0, g - degree)
            b = max(0, b - degree)
            new.setPixel(x, y, (r, g, b))
   return new

def main():
   filename = input("Enter the image file name: ")
   image = Image(filename)
   print("Close the image window to continue.")
   image.draw()
   sharpImage = sharpen(image, 50, 10)
   print("Close the image window to quit.")
   sharpImage.draw()

if __name__ == "__main__":
   main()
