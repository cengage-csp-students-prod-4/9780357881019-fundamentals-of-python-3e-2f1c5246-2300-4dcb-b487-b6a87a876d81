"""
Program: Right Triangle Checker
9-16-2026
Michael Guillen

ask user for 'sideOne', as an int
ask user for 'sideTwo', as an int
ask user for 'sideThree', as an int

check which side is bigger and assign it to variable 'c'
assign other two sides to variables 'a' and 'b'
check if a^2+b^2=c^2, if yes print 'the triangle is a right triangle'
if not then print 'triangle is not a right triangle
"""

sideOne = int(input('Enter the first side: '))
sideTwo = int(input('Enter the second side: '))
sideThree = int(input('Enter the third side: '))

if sideThree > sideTwo and sideOne:
    a = sideOne
    b = sideTwo
    c = sideThree
else: 
    if sideTwo > sideOne and sideThree:
        a = sideOne
        b = sideThree
        c  = sideTwo
    else:
        if sideOne > sideTwo and sideThree:
            a = sideTwo
            b = sideThree
            c = sideOne
        else:
            if sideOne == sideTwo and sideThree:
                print('The triangle is an equalateral triangle')
                import sys
                sys.exit()

if a**2 + b**2 == c**2: # type: ignore
    print('The triangle is a right triangle')
else:
    print('The triangle is not a right triangle')