# Write your program here

import math
import random

smaller = int(input('Enter the smaller number: '))
larger = int(input('Enter the larger number: '))
compGuess = random.randint(smaller, larger)
totNums = (larger - smaller) + 1
guessAmnt = int(math.log(totNums, 2)) + 1
count = 0
print(guessAmnt)

print('Guess #', str(count+1) + ': Your number is', compGuess)

for count in range(1, guessAmnt+1):
    if smaller > larger or count == guessAmnt:
        print("I'm out of guesses, and you cheated!")
        break
    userGuess = input('Enter =, <, or >: ')
    if userGuess == '<' and smaller < larger and smaller != larger:
        smaller = compGuess+1
        print(smaller, larger)
        compGuess = random.randint(smaller, larger)
        print('Guess #', str(count+1) + ': Your number is', compGuess)
    elif userGuess == '>' and smaller < larger and smaller != larger:
        larger = compGuess-1
        print(smaller, larger)
        compGuess = random.randint(smaller, larger)
        print('Guess #', str(count+1) + ': Your number is', compGuess)
    elif userGuess == '=' and smaller < larger and smaller != larger:
        print("Hooray, I've got it in", count, "tries!")
        break
    else:
        print('Error!')
        break