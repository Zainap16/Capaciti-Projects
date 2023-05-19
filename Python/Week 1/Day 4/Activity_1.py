import math

# standard size (500 ml)
# user only enters the number of litres of water they have
# calculates how many bottles they can fill.
# decimal shoyld be omitted
user_num_litres = float(input('Enter number of litres: '))


def calculate():

    litres = (user_num_litres * 1000)
    litres = math.trunc(litres / 500)
    return litres


print(f'{user_num_litres}L will fill {calculate()} bottles')
