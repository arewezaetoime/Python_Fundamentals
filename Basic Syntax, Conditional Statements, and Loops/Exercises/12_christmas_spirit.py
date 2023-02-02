quantity = int(input())
days = int(input())
# scores and costs
total_cost = 0
points_christmas_spirit = 0
# items
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
days_counter = 0
while days_counter < days:
    days_counter += 1
    if days_counter % 11 == 0:
        quantity += 2
    if days_counter % 2 == 0:
        total_cost += ornament_set * quantity
        points_christmas_spirit += 5
    if days_counter % 3 == 0:
        total_cost += (tree_skirt + tree_garland) * quantity
        points_christmas_spirit += 13
    if days_counter % 5 == 0:
        total_cost += tree_lights * quantity
        points_christmas_spirit += 17
        if days_counter % 3 == 0:
            points_christmas_spirit += 30
    if days_counter % 10 == 0:
        points_christmas_spirit -= 20
        total_cost += (tree_skirt + tree_garland + tree_lights)
if days % 10 == 0:
    points_christmas_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {points_christmas_spirit}")