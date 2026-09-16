# Write your program here

import math
import random

smaller = int(input('Enter the smaller number: '))
larger = int(input('Enter the larger number: '))
compGuess = random.randint(smaller, larger)
totNums = (larger - smaller) + 1
guessAmnt = int(math.log(totNums, 2)) + 1
print('smaller:', smaller, 
      'larger:', larger, 
      'compGuess:', compGuess, 
      'totNums:', totNums,
      'guessAmnt:', guessAmnt,
      sep='\n')

print('Your number is', compGuess)

for count in range(1, guessAmnt+1):
    if smaller > larger:
        print('You cheated! Give better hints')
        break
    elif count == guessAmnt:
        print("I'm out of guesses, I lose!")
        break
    
    userGuess = input('Enter =, <, or >: ')
    if userGuess == '<':
        smaller = compGuess+1
        print(smaller, larger)
        compGuess = random.randint(smaller, larger)
        print('Your number is', compGuess)
    elif userGuess == '>':
        larger = compGuess-1
        print(smaller, larger)
        compGuess = random.randint(smaller, larger)
        print('Your number is', compGuess)
    elif userGuess == '=':
        print("Hooray, I've got it in", count, "tries!")
        break