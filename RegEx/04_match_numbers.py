import re
some_nums = input()
pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

result = re.finditer(pattern, some_nums)

for number in result:
    print(number.group(), end=' ')