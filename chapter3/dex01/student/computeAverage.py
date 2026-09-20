count = 1
total = 0
while count <= 10:
    if count == 1:
        score = int(input("Enter test score number " + str(count) + ": "))
        total = score
    score = int(input("Enter test score number " + str(count) + ": "))
    print('current score:', score, '|current total:', total)
    total += score
    count += 1
average = round(total / count, 1)
print("The average test score is", average)