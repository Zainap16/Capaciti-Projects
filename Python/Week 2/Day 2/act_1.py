def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def determine_coldest_day(temp_day1, temp_day2):
    if temp_day1 < temp_day2:
        return "The first day was the coldest."
    elif temp_day1 > temp_day2:
        return "The second day was the coldest."
    else:
        return "The temperatures were the same on both days."


temp_day1 = float(
    input("Enter the maximum temperature (in °F) for the first day: "))
temp_day2 = float(
    input("Enter the maximum temperature (in °F) for the second day: "))

temp_day1_celsius = fahrenheit_to_celsius(temp_day1)
temp_day2_celsius = fahrenheit_to_celsius(temp_day2)

print("Temperatures in °C:")
print("Day 1:", temp_day1_celsius)
print("Day 2:", temp_day2_celsius)

coldest_day_message = determine_coldest_day(
    temp_day1_celsius, temp_day2_celsius)
print(coldest_day_message)
