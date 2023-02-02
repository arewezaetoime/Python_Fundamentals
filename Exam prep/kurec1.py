days_adventure = int(input())
count_of_players = int(input())
group_energy = float(input())

water_for_a_day = float(input())
food_for_a_day = float(input())
total_water = (days_adventure * count_of_players) * water_for_a_day
total_food = (days_adventure * count_of_players) * food_for_a_day
for day in range(1, days_adventure + 1):
    energy_loss = float(input())
    group_energy -= energy_loss
    if group_energy <= 0:
        print(f"You will run out of energy. You will be left with\
 {total_food:.2f} food and {total_water:.2f} water.")
        break
    if day % 2 == 0:
        group_energy += (group_energy * 0.05)
        total_water -= (total_water * 0.3)
    if day % 3 == 0:
        total_food -= (total_food / count_of_players)
        group_energy += (group_energy * 0.10)

if group_energy > 0:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
