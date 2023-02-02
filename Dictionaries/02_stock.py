products = input().split(' ')
searched_prods = input().split(' ')
stocks = {}
for keys in range(0, len(products), 2):
    key = products[keys]
    value = products[keys + 1]
    stocks[key] = int(value)

for search in searched_prods:
    if search in stocks.keys():
        print(f"We have {stocks[search]} of {search} left")
    else:
        print(f"Sorry, we don't have {search}")