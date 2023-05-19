import re

def remove_numbers_except_5(string):
    pattern = r"[^5\s]"
    result = re.sub(pattern, "", string)
    return result

# Example usage
text = "A string with numbers 1, 2, 3, and 5. Keep 5!"
filtered_text = remove_numbers_except_5(text)
print(filtered_text)
