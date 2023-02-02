lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
# broken equipment counters
broken_helmets = lost_fights // 2
broken_swords = lost_fights // 3
broken_shields = lost_fights // 6
broken_armors = broken_shields // 2

total_price = (
    (broken_helmets * helmet_price) +
    (broken_armors * armor_price) +
    (broken_shields * shield_price) +
    (broken_swords * sword_price)
)
print(f"Gladiator expenses: {total_price:.2f} aureus")