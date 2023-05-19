import math


user_option = input('''
    Choose either "investment" or "bond" from the menu below to proceed:

    investment      - to calculate the amount of interest you will earn on interest
    bond            - to calculate the amount you will have to pay on a home loan 
    
    ''').lower()

if user_option == 'investment':
    user_amount_deposit_p = float(
        input('Enter amount that you wish to deposit: R '))
    interest_rate = float(
        input('Enter interest rate: '))
    user_num_years_t = int(
        input('Enter number of years: '))
    user_investment_option = input(
        'Choose between "simple" or "compound": ').lower()
    if user_investment_option == 'simple':
        total = 0
        total = user_amount_deposit_p * \
            (1 + (interest_rate/100) * user_num_years_t)
        print('The simple interest amount is: R',  float(total))
    elif user_investment_option == 'compound':
        total = 0
        total = user_amount_deposit_p * \
            math.pow((1 + (interest_rate/100)), user_num_years_t)
        print('The compound interest amount is: R',  float(total))

if user_option == 'bond':
    value_of_the_house = float(input('Please enter the value of the house: R'))
    interest_rate = float(
        input('Enter interest rate: '))
    period = float(
        input('Enter number of months you plan to repay the bond: '))
    installments = 0
    installments = (value_of_the_house * (interest_rate / 1200)
                    ) / (1 - (math.pow((1 + (interest_rate / 1200)), -period)))
    print('Your monthly payments will be: R', float(installments))
