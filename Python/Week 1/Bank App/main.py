
user_option = input(
    'Do you wish to do a widthdraw or deposit \n press w-withdrawl and or d-deposit: ').lower()

if user_option == 'd':
    total = 0

    with open('transaction.txt', 'a') as deposit:
        user_deposit = input('enter the deposit amount: R ')
        deposit.write(user_deposit + '\n')

    with open('transaction.txt', 'r') as readfile:
        content = readfile.readlines()
        for lines in (content):
            total += float(lines)

    with open('totalbalance.txt', 'w') as readfile:
        print(str(total))

elif user_option == 'w':
    total2 = 0
    with open('transaction.txt', 'a') as withdrawls:
        user_withdrawls = input('enter the withdrawls amount: R ')
        withdrawls.write('-'+user_withdrawls + '\n')

    with open('transaction.txt', 'r') as withdrawls_read:
        content2 = withdrawls_read.readlines()
        for lines2 in content2:
            total2 += float(lines2)
        print(total2)

else:
    print('not valid')

# add values tg via txt
# total = 0

# with open('transaction.txt', 'a') as deposit:
#     user_deposit = input('enter the deposit amount: R ')
#     deposit.write(user_deposit + '\n')

# with open('transaction.txt', 'r') as readfile:
#     content = readfile.readlines()
#     for lines in (content):
#         total += float(lines)

# with open('totalbalance.txt', 'w') as readfile:
#     print(str(total))

# subtracts values===withdrawls
# total2 = 0
# with open('transaction.txt', 'a') as withdrawls:
#     user_withdrawls = input('enter the withdrawls amount: R ')
#     withdrawls.write('-'+user_withdrawls + '\n')

# with open('transaction.txt', 'r') as withdrawls_read:
#     content2 = withdrawls_read.readlines()
#     for lines2 in content2:
#         total2 += float(lines2)
#     print(total2)
