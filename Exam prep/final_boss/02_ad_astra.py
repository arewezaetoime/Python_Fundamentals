import re
products = input()
pattern = r'(#|\|)(?P<product>[A-Za-z\s?]+)\1(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})\1(?P<cal>\d[0-9]+)\1'
matches = re.findall(pattern, products)
total_calories = 0
# print(matches)
if matches:
    for i in matches:
        total_calories += int(i[3])
average = total_calories // 2_000
print(f"You have food to last you for: {average} days!")
if matches:
    for current_product in matches:
        print(f"Item: {current_product[1]}, Best before: {current_product[2]}, Nutrition: {current_product[3]}")