import re

# Example 1: Matching and extracting information

# Define a pattern for matching email addresses
email_pattern = r'([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)'

# Input string
text = 'Contact us at support@example.com or info@example.com'

# Find all email addresses in the input string
matches = re.findall(email_pattern, text)

# Print the extracted email addresses
for match in matches:
    print(f'Email: {match[0]} Domain: {match[1]} Extension: {match[2]}')

# Example 2: Pattern substitution

# Define a pattern for matching phone numbers in the format (XXX) XXX-XXXX
phone_pattern = r'\((\d{3})\) (\d{3})-(\d{4})'

# Input string
text = 'Contact us at (555) 123-4567 or (888) 987-6543'

# Replace phone numbers with a generic string
replaced_text = re.sub(phone_pattern, '[PHONE NUMBER]', text)

# Print the modified text
print(replaced_text)
