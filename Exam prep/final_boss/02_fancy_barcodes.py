import re
n = int(input())
pattern = r'([@][#]+[A-Z][a-z0-9A-Z]{4,}[A-Z][@][#]+)'
for _ in range(n):
    current_string = input()
    match = re.match(pattern, current_string)
    if not match:
        print('Invalid barcode')
    else:
        digits = re.findall(r'\d', match.group())
        if not digits:
            print('Product group: 00')
        else:
            print(f"Product group: {''.join(digits)}")

