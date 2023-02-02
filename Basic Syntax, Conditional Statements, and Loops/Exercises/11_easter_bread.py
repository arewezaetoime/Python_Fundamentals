budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25
price_one_bread = eggs_price + flour_price + (milk_price / 4)
coloured_eggs = 0
bread_count = 0
money_remained = budget
while money_remained >= price_one_bread:
    money_remained -= price_one_bread
    bread_count += 1
    coloured_eggs += 3
    if bread_count % 3 == 0:
        coloured_eggs -= (bread_count - 2)
print(f"You made {bread_count} loaves of Easter bread! Now you have {coloured_eggs} eggs and "
      f"{money_remained:.2f}BGN left.")

