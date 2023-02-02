employees = list(map(int, input().split(' ')))
happiness_factor = int(input())
happiness_lst = list(map(lambda x: x * happiness_factor, employees))
filtered = list(filter(lambda a: a >= sum(happiness_lst) / len(happiness_lst), happiness_lst))

if len(filtered) >= len(happiness_lst) // 2:
    print(f"Score: {len(filtered)}/{len(happiness_lst)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(happiness_lst)}. Employees are not happy!")