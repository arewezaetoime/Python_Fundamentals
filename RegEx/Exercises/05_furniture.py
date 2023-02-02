import re
# pattern = r'\>>([A-za-z]+)<<([0-9]+\.?[0-9]{2})*\!([0-9])\b'
rege = re.compile(r'>>([A-za-z]+)<<(\d+\.?\d*)!(\d+)\b')
current_furniture = input()
total_sum = 0
items = []
while current_furniture != 'Purchase':
    match = re.search(rege, current_furniture)
    if match:
        current_item, price, quantity = match.groups()
        items.append(current_item)
        total_sum += float(price) * int(quantity)
    current_furniture = input()

print('Bought furniture:')
for item in items:
    print(''.join(item))
print(f'Total money spend: {total_sum:.2f}')