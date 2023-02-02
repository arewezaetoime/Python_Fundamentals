import re
pattern = r'^%([A-Z][a-z]+)%[^\|\$\%\.]*?<(\w+)>[^\|\$\%\.]*?\|([\d]+)\|[^\|\$\%\.]*?([\d]+([\.\d]*)?)\$$'
total_income = 0
input_line = input()
while input_line != 'end of shift':
    match = re.search(pattern, input_line)
    if match:
        total_price = int(match.group(3)) * float(match.group(4))
        total_income += total_price

        print(f'{match.group(1)}: {match.group(2)} - {total_price:.2f}')

    input_line = input()
print(f'Total income: {total_income:.2f}')