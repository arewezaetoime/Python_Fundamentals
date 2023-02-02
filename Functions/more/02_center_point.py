import math


def get_pairs(x1, y1, x2, y2):
    first_pair = (float(coordinates[0]) ** 2) + (float(coordinates[1]) ** 2)
    second_pair = (float(coordinates[2]) ** 2) + (float(coordinates[3]) ** 2)
    if first_pair < second_pair:
        return float(x1), float(y1)
    elif first_pair > second_pair:
        return float(x2), float(y2)
    else:
        return float(x1), float(y1)


coordinates = []
for _ in range(4):
    current_input = input()
    coordinates.append(current_input)

result = get_pairs(coordinates[0], coordinates[1], coordinates[2], coordinates[3])

print(f'({math.floor(result[0])}, {math.floor(result[1])})')


