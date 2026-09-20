count = 1
total = 0
while count <= 10:
    score = int(input("Enter test score number " + str(count) + ": "))
    print('current score:', score, '|current total:', total)
    total += score
    count += 1
average = round(total / count, 1)
print("The average test score is", average)