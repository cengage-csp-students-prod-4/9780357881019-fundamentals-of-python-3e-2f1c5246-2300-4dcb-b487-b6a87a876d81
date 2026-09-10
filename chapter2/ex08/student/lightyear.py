"""
Program: Lightyear Calculator
9-10-2026
Michael Guillen

ask user for number of years, 'years' as an int
seconds = years * 31,536,000
lightSpeed = 3*10**8

meters = lightSpeed * seconds

print('Light travels', meters, 'meters in', years, 'years.)
"""

years = int(input('Enter the number of years: '))
seconds = years * 31536000
lightSpeed = 3*10**8

meters = lightSpeed * seconds

print('Light travels', meters, 'meters in', years, 'years.')