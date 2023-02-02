contests = {}
candidates = {}

command_input = input()
while command_input != 'end of contests':
    contest, password = command_input.split(':')
    contests[contest] = password
    command_input = input()

candidates_input = input()
while candidates_input != 'end of submissions':
    current_contest, password, username, points = candidates_input.split('=>')
    if current_contest in contests.keys():
        if password == contests[current_contest]:
            if username not in candidates.keys():
                candidates[username] = {int(points): current_contest}

            if current_contest not in candidates[username].values():
                upd_contest = {int(points): current_contest}
                candidates[username].update(upd_contest)
            elif current_contest in candidates[username].values():
                for key, value in candidates[username].items():
                    if key < int(points):
                        key = int(points)

    candidates_input = input()
sum_lst = []
for key, value in candidates.items():
    current_sum = sum(value.keys())
    total = current_sum, key
    sum_lst.append(total)

print(f"Best candidate is {max(sum_lst)[1]} with total {max(sum_lst)[0]} points.")
print('Ranking:')
for current_candidate in sorted(candidates):
    print(current_candidate)
    for key, value in sorted(candidates[current_candidate].items(), reverse=True):
        print(f'#  {value} -> {key}')
