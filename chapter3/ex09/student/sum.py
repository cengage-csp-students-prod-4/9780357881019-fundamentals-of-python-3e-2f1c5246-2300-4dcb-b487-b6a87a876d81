# Write your program here

totSum = float()
numCount = 0

while True:
    numInput = input("Enter a number or press Enter to quit: ")
    if numInput == "" or numInput is None:
        break
    totSum += float(numInput)
    numCount += 1

print("The sum is", totSum)
print("The average is", totSum / numCount)
