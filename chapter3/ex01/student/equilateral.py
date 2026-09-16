"""
Program: Equalateral Checker
9-16-2026
Michael Guillen

ask user for 'sideOne', as an int
ask user for 'sideTwo', as an int
ask user for 'sideThree', as an int

if sideOne == sideTwo and sideOne == sideThree and sideTwo == sideThree then
    print('The triangle is equalateral')
else
    print('The triangle is not equalateral')
"""

sideOne = int(input('Enter the first side: '))
sideTwo = int(input('Enter the second side: '))
sideThree = int(input('Enter the third side: '))

if sideOne == sideTwo and sideOne == sideThree and sideTwo == sideThree:
    print('The triangle is equalateral')
else:
    print('The triangle is not equalateral')