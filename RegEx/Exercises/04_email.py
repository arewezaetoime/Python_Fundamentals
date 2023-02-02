import re
emails = input()
pattern = r'\s(([a-z0-9]+[a-z0-9\.\,\-\_]+)*@[a-z\-]+(\.[a-z]+)+)\b'
valid_emails = re.findall(pattern, emails)
for match in valid_emails:
    print(match[0])