"""
Program: Momentum Calculator
9-10-2026
Michael Guillen

set 'objMass' to users input as a float
set 'objVelo' to users input as a float

objMomen = objMass*objVelo
objKenEn = 1/2*objMomen**2

print("The object's momentum is", objMomen)
"""

objMass = float(input("Enter the object's mass: "))
objVelo = float(input("Enter the object's velocity: "))

objMomen = objMass*objVelo
objKenEn = 1/2*objMass*objVelo**2

print("The object's momentum is", objMomen, "\nThe object's kinetic energy is", objKenEn)