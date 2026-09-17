"""
Program: Population Calculator
9-17-2026
Michael Guillen

ask user for 'orgnsmNum', int
ask user for 'growthRt', check if real number and > 1
ask user for 'hourRt', int
ask user for 'totHours', int
assign 'totOrgnsm' to 'orgnsmNum'

cycle through a loop 'totHours/hourRt' times
    multiply 'totOrgnsm' by 'growthRt', assign to 'totOrgnsm'

print('The total population is', 'totOrgnsm')
"""

orgnsmNum = int(input('Enter the initial number of organisms: '))
growthRt = float(input('Enter the rate of growth [a real number > 1]: '))
if growthRt <= 1:
    import sys
    sys.exit("""
    ----------------------------------------------------------------------------
    Invalid growth rate. Please try again and input a real number greater than 1
    ----------------------------------------------------------------------------
    """)
hourRt = int(input('Enter the number of hours to achieve the rate of growth: '))
totHours = int(input('Enter the total hours of growth: '))
totOrgnsm = orgnsmNum

for x in range(int(totHours/hourRt)):
    totOrgnsm = totOrgnsm * growthRt

print('The total population is', int(totOrgnsm))