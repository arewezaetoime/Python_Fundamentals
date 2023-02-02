def left_side(lst, point, command):
    entry_index = lst[point]
    left_damage = []
    for left in lst[point - 1:: -1]:
        if command == 'cheap':
            if left < entry_index:
                left_damage.append(left)
        elif command == 'expensive':
            if left >= entry_index:
                left_damage.append(left)
    return sum(left_damage)


def right_side(lst, point, command):
    entry_index = lst[point]
    right_damage = []
    for right in lst[point + 1:]:
        if command == 'cheap':
            if right < entry_index:
                right_damage.append(right)
        elif command == 'expensive':
            if right >= entry_index:
                right_damage.append(right)
    return sum(right_damage)


price_ratings = list(map(int, input().split(', ')))
entry_point = int(input())
type_of_elements = input()
total_lst = [left_side(price_ratings, entry_point, type_of_elements),
             right_side(price_ratings, entry_point, type_of_elements)]

position = ''
if total_lst[0] == total_lst[1]:
    position = 'Left'
    print(f"{position} - {max(total_lst)}")
elif total_lst[0] > total_lst[1]:
    position = 'Left'
    print(f"{position} - {max(total_lst)}")
elif total_lst[0] < total_lst[1]:
    position = 'Right'
    print(f"{position} - {max(total_lst)}")

# for left in price_ratings[entry_point - 1:: -1]:
#     if type_of_elements == 'cheap':
#         if left < entry_index:
#             left_damage.append(left)
#     elif type_of_elements == 'expensive':
#         if left >= entry_index:
#             left_damage.append(left)
#
# for right in price_ratings[entry_point + 1:]:
#     if type_of_elements == 'cheap':
#         if right < entry_index:
#             right_damage.append(right)
#     elif type_of_elements == 'expensive':
#         if right > entry_index:
#             right_damage.append(right)
