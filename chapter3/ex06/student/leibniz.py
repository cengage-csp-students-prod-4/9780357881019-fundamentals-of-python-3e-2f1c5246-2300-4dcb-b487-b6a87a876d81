"""
Program: Pi Estimator 
9-17-2026
Michael Guillen

ask user for 'iterations', int

cycle through 'iterations'
    alternate between adding and subracting with a difference of 2 in the denominator
        assign to piApprox

print(piApprox)
"""

iterations = int(input('Enter the number of iterations: '))
denominator = 3
piApprox = 1
operator = 'minus'

for x in range(1, iterations):
    if operator == 'minus':
        piApprox = float(piApprox - 1/denominator)
        operator = 'plus'
    elif operator == 'plus':
        piApprox = float(piApprox + 1/denominator)
        operator = 'minus'
    denominator += 2

print('The approximation of pi is', piApprox*4)