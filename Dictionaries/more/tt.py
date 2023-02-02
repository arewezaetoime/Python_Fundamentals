pool = {'Peter': {'Adc': 400}, 'Frank': {'Mid': 200, 'Support': 250, 'Tank': 250}}

sums_dict = {key: sum(value.values()) for key, value in sorted(pool.items())}
# Let the fuckin sorting begin:
for player, total_skills in sorted(sums_dict.items(), key=lambda item: (-item[1], item[0])):
    print(f"{player}: {total_skills} skill")
    for position, skill in sorted(pool[player].items(), key=lambda item: (-item[1], item[0])):
        print(f"- {position} <::> {skill}")
        # Az sam Ahil ot Troya az sam Hector az sam Lil WAyne az sam mnogo horaaaaaaaa

# sorted_by_value = {k: v for k, v in sorted(pool.items(), key=lambda v: v, reverse=True)}
# print(sorted_by_value)
# for k, v in pool.items():
#     print(k)
#     print(v)
# sorted_positions = {k: v for k, v in sorted(pool.items(), key=lambda v: v[1])}
# print(sorted_positions)

# new_dict = {'a': 3, 'b': 4, 'c': 5}
# sort_by_key = {k: v for k, v in sorted(new_dict.items(), key=lambda k: k, reverse=False)}
# print(sort_by_key)
# sort_by_value = {k: v for k, v in sorted(new_dict.items(), key=lambda v: v, reverse=True)}
# print(sort_by_value)


# # initializing dictionary
# test_dict = {'Gfg': [6, 7, 4], 'is': [4, 3, 2], 'best': [7, 6, 5]}
#
# # printing original dictionary
# print("The original dictionary is : " + str(test_dict))
#
# # summing all the values using sum()
# temp1 = {key: sum(int(idx) for idx in val)
#          for key, val in test_dict.items()}
# print(temp1)
#
# # using sorted to perform sorting as required
# temp2 = sorted(temp1.items(), key=lambda ele: temp1[ele[0]])
#
# # rearrange into dictionary
# res = {key: val for key, val in temp2}
#
# # printing result
# print("The sorted dictionary : " + str(res))