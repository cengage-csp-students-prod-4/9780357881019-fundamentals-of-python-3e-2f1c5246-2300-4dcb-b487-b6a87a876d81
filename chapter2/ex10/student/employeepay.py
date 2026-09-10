"""
Program: Employees Total Weekly Pay Calculator
9-10-2026
Michael Guillen

ask user for the wage, 'wage', as a float
ask user for the regular hours, 'regHours', as an int
ask user for the overtime hours, 'otHours', as an int
otPay = otHours*(1.5*wage)
regPay = regHours*wage

totalPay = '$' + str(otPay + regPay)

print('The total weekly pay is', totalPay)
"""

wage = float(input('Enter the wage: '))
regHours = int(input('Enter the regular hours: '))
otHours = int(input('Enter the overtime hours: '))
otPay = otHours*(1.5*wage)
regPay = regHours*wage

totalPay = otPay + regPay

print('The total weekly pay is $' + str(totalPay))