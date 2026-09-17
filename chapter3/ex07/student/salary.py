"""
Program: Salary Scheduler
9-17-2026
Michael Guillen

ask user for 'strtSal', float
ask user for 'annPrcnt', float, divide by 100
ask user for 'years', int

cycle through a loop 'years' times
    add the amount of money in the last year times 'annPrcnt' to the ammount of money in the last year
    print(x, 'totSal')
"""

startSal = float(input('Enter the starting salary: $'))
annPrcnt = float(input('Enter the annual % increase: '))/100
years = int(input('Enter the number of years: '))
totSal = startSal
outputList = []

for x in range(1, years+1):
    rowString = f"{x}  {totSal:0.2f}"
    outputList.append(rowString)
    totSal = float(totSal + totSal*annPrcnt)

print(outputList)