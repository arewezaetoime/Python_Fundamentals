our_dict = {}

while True:
    metal = input()
    if metal == 'stop':
        for metal, amount in our_dict.items():
            print(f"{metal} -> {amount}")
        break
    amount = int(input())
    if metal not in our_dict.keys():
        our_dict[metal] = 0
    our_dict[metal] += amount
