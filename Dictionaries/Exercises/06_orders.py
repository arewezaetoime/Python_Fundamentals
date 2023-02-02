our_dict = {}

orders_input = input().split()

while len(orders_input) > 1:
    name = orders_input[0]
    price = float(orders_input[1])
    quantity = int(orders_input[2])
    if name not in our_dict.keys():
        our_dict[name] = []
        our_dict[name].append(price)
        our_dict[name].append(quantity)
    else:
        our_dict[name][0] = price
        our_dict[name][1] += quantity

    orders_input = input().split()

for name, info in our_dict.items():
    price = info[0]
    quantity = info[1]
    print(f"{name} -> {price * quantity:.2f}")
