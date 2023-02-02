import re

pattern = r'\d+'
input_string = input()
while input_string:
    number = re.findall(pattern, input_string)
    if number:
        print(' '.join(number), end=' ')
    input_string = input()
