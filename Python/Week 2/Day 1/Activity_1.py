count = 1
for i in range(1, 40):
    if i == 1:
        print(count, count + 1, count+2)
    else:
        print('\n')
        print(count, count + 1, count+2)
    count += 3
