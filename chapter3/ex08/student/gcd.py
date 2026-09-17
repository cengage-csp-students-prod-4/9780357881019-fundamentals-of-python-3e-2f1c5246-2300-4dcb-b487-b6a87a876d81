""""
Program: GCD Finder
9-17-2026
Michael Guillen

ask user for 'smallNum', int
ask user for 'largeNum', int

use a while loop checking if 'smallNum' == 0
    get 'remainder' by doing 'largeNum'/'smallNum'
    'largeNum' = 'smallNum'
    'smallNum' = 'remainder'

print('largeNum')
"""

smallNum = int(input('Enter the smaller number: '))
largeNum = int(input('Enter the larger number: '))
remainder = int()

while remainder > 0 or remainder != 0:
    remainder = largeNum/smallNum
    largeNum = smallNum
    smallNum = remainder

print('The greatest common divisor is', smallNum)