number_snowballs = int(input())
highest_value = 0
current_weight = 0
current_time = 0
current_quality = 0
for ball in range(number_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    score = (weight / time) ** quality
    if score > highest_value:
        highest_value = score
        current_weight = weight
        current_time = time
        current_quality = quality
print(f"{current_weight} : {current_time} = {int(highest_value)} ({current_quality})")