""" "
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

smallNum = int(input("Enter the smaller number: "))
largeNum = int(input("Enter the larger number: "))
remainder = int()
count = 1

while True:
    if smallNum == 0:
        break
    print("Step " + str(count) + ":", largeNum, "/", smallNum, "=", largeNum / smallNum)
    remainder = largeNum - (int(largeNum/smallNum) * smallNum)
    print("Large Number =", smallNum)
    largeNum = smallNum
    print("Small Number =", remainder)
    smallNum = remainder
    count += 1

print("The greatest common divisor is", largeNum)
