products_dict = {}
products_input = input().split(': ')

while len(products_input) > 1:
    keys = products_input[0]
    value = products_input[1]
    if keys not in products_dict.keys():
        products_dict[keys] = 0

    products_dict[keys] += int(value)
    products_input = input().split(': ')

print("Products in stock:")
for key, value in products_dict.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products_dict.keys())}")
print(f"Total Quantity: {sum(products_dict.values())}")
