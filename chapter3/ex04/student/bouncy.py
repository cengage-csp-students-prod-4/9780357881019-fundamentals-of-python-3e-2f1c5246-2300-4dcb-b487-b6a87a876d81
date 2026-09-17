# Write your program here

dropHeight = float(input('Enter the height from which the ball is dropped: '))
bnceIndx = float(input('Enter the bounciness index of the ball: '))
numOfBncs = int(input('Enter the number of times the ball is allowed to continue bouncing: '))
totDist = dropHeight
curDist = dropHeight*bnceIndx
print(totDist, curDist)

for x in range(1, numOfBncs+1):
    if x == 1: # checking if its the first bounce
        totDist = totDist + curDist
    else:
        prevDist = curDist
        curDist = curDist*bnceIndx
        totDist = totDist + prevDist + curDist

print(totDist)