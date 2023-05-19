import re


def validate_cell_phone_number(number):
    pattern = r'^\+27\d{2}-\d{3}-\d{4}$'
    if re.match(pattern, number):
        return True
    else:
        return False


# Example usage
user_input = input("Enter a cell phone number (e.g., +2778-123-4567): ")

if validate_cell_phone_number(user_input):
    print("The number is in the correct format.")
else:
    print("Error: The number is in an incorrect format.")
