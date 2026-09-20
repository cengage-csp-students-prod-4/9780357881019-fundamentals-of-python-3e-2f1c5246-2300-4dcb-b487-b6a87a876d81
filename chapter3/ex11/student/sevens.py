"""
Program: Dice Game Calculator
9-20-2026
Michael Guillen

ask user for 'money', float
loop until money is less than or equal to 1
    roll 2 random numbers between 1 and 6
    add 4 to money if the sum of the two numbers is 7, otherwise subtract 1 from money
print the number of rolls it took to go broke and the max amount of money they couldve gotten
"""

import random

money = float(input("How many dollars do you have? "))
maxMoney = 0
rolls = 0

while True:
    rolls += 1
    if money <= 1:
        print("You are broke after", rolls, "rolls.")
        break

    diceRollA = random.randint(1, 6)
    diceRollB = random.randint(1, 6)

    if diceRollA + diceRollB == 7:
        money += 4
    else:
        money -= 1
    if money > maxMoney:
        maxMoney = money

print('You should have quit after 6 rolls when you had $', maxMoney, sep="")