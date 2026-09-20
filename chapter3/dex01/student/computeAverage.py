count = 1
total = 0
while count <= 10:
    score = int(input("Enter test score number " + str(count) + ": "))
    if count == 1:
        total = score
    else:
        total += score

    count += 1
print('count:', count-1)
print('total:', total)
average = round(total / (count-1), 1)
print("The average test score is", average)