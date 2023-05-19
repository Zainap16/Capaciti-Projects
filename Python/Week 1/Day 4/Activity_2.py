# user to input the millilitres of water that were released to the oceans/rivers.
# generate a report showing how many litres of water were released
# how many left and the percentage of the litres left.

user_millitres = 70000000
amount_of_water_released = user_millitres / 1000
amount_of_water_left = 1000000 - amount_of_water_released
percentage = (amount_of_water_left / 1000000) * 100

print(
    f'Amount of water released {amount_of_water_released}L\n Amount of water left {amount_of_water_left}L\n Percentage: {percentage}L')
