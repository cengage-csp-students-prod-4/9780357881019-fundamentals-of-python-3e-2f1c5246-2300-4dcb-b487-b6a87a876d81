"""
Program: Five Star Retro Video Cost Calculator
9-10-2026
Michael Guillen

get variable 'newVidsCost' from user as a float and times by 3
get variable 'oldVidsCost' from user as a float and times by 2

totCost = newVids + oldVids

print('The total cost is $', totCost)
"""

newVidsCost = float(input('Number of new videos: ')) *3
print(newVidsCost)
oldVidsCost = float(input('Number of oldies: ')) * 2
print(oldVidsCost)

totCost = newVidsCost + oldVidsCost

print('The total cost is $' + str(totCost))