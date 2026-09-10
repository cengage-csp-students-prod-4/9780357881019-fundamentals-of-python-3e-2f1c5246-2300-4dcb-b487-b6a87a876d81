"""
Program: Radius of Sphere Converter
9-10-2026
Michael Guillen

import math
pi = math.pi

Ask user for the radius 'rad' convert to float

diam = 2*rad
circum = 2*pi*rad
surfArea = 4*pi*rad**2
vol = 4/3*pi*rad**3

print('Diameter:', diam, '\nCircumference:', circum, '\nSurface area:', surfArea, '\nVolume:', vol)
"""

import math
pi = math.pi

rad = float(input("Enter the sphere's radius: "))

diam = 2*rad
circum = 2*pi*rad
surfArea = 4*pi*rad**2
vol = 4/3*pi*rad**3

print('Diameter:', diam, '\nCircumference:', circum, '\nSurface area:', surfArea, '\nVolume:', vol)