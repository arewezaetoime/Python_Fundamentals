single_string = input()
digits = ''
letters = ''
other = ''
for char in single_string:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    elif char.isascii():
        other += char
print(digits)
print(letters)
print(other)