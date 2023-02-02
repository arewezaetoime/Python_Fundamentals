names_list = input().split(', ')
sorted_lst = sorted(names_list, key=lambda x: (-len(x), x))
print(sorted_lst)