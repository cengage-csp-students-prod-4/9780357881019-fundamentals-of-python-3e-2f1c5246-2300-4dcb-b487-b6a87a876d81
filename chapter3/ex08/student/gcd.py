""""
Program: GCD Finder
9-17-2026
Michael Guillen

ask user for 'smallNum', float
ask user for 'largeNum', float

use a while loop checking if 'smallNum' == 0
    get 'remainder' by doing 'largeNum'/'smallNum'
    'largeNum' = 'smallNum'
    'smallNum' = 'remainder'

print('largeNum')
"""

smallNum = float(input('Enter the smaller number: '))
largeNum = float(input('Enter the larger number: '))
remainder = float()

while remainder > 0 or remainder != 0:
    remainder = largeNum/smallNum
    largeNum = smallNum
    smallNum = remainder

print('The greatest common diviser is', smallNum)