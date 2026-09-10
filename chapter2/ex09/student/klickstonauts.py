"""
Program: Kilometers to Nautical Miles Converter
9-10-2026
Michael Guillen

ask user for number of kilometers, 'kiloM', as a float
totalMins = 90*60
nautMiles = totalMins*1
totNauts = kiloM*1/10000*nautMiles

print('The number of nautical miles is', totNauts)
"""

kiloM = float(input('Enter the number of kilometers: '))
totalMins = 90*60
nautMiles = totalMins*1
totNauts = kiloM*1/10000*nautMiles

print('The number of nautical miles is', totNauts)