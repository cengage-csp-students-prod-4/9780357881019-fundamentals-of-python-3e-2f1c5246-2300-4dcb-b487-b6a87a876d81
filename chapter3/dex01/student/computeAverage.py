count = 1
total = 0
while count <= 10:
    print('count:', count)
    score = int(input("Enter test score number " + str(count) + ": "))
    total += score
    count += 1
average = round(total / count, 1)
print("The average test score is", average)