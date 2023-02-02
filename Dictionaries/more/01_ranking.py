def print_results():
    print(f"Best candidate is {max(best_candidate)} with total {max(best_candidate.values())} points.\nRanking:")
    for user in sorted(contestants_dict.keys()):
        print(user)
        for contest in sorted(contestants_dict[user].items(), key=lambda item: item[1], reverse=True):
            print(f'#  {contest[0]} -> {contest[1]}')


def get_contests():
    # With this func we get the contest's data.
    contest_input = input()
    while contest_input != 'end of contests':
        contest_input = contest_input.split(':')
        if len(contest_input) == 2:
            contests_dict[contest_input[0]] = contest_input[1]
        contest_input = input()


def validate_entry(c_contest, c_pass, c_point, c_user):
    # Contest validation func
    if c_contest in contests_dict.keys():
        if c_pass == contests_dict[c_contest]:
            if c_point in range(0, 10_001):
                list_with_symbols = [':', '=', '>']
                flag = True
                for sym in list_with_symbols:
                    if sym in c_contest or sym in c_pass or sym in c_user:
                        flag = False
                        break
                if flag:
                    return True
    return False


def add_contestant(c_username, c_points, c_contest):
    # This is our ADD func.
    if c_username not in contestants_dict.keys():
        contestants_dict[c_username] = {}
        contestants_dict[c_username][c_contest] = c_points
    if c_contest in contestants_dict[c_username]:
        if contestants_dict[c_username][c_contest] < c_points:
            contestants_dict[c_username][c_contest] = c_points
    else:
        contestants_dict[c_username][c_contest] = c_points


def get_contestants():
    # With this func we get the data for the contestants.
    contestant_input = input()
    while contestant_input != 'end of submissions':
        contestant_input = contestant_input.split('=>')
        if len(contestant_input) == 4:  # Checking if we have all needed data/values.
            contest, password, username, points = str(contestant_input[0]), str(contestant_input[1]), \
                                                  str(contestant_input[2]), int(contestant_input[3])
            # Here we check if the contest is present in the contests list and whether the password is correct.
            if validate_entry(contest, password, points, username):
                # If so, we call the ADD func.
                add_contestant(username, points, contest)
        contestant_input = input()


contestants_dict = {}
contests_dict = {}
get_contests()
get_contestants()

best_candidate = {}
for current_user in contestants_dict.keys():
    best_candidate[current_user] = sum(contestants_dict[current_user].values())

print_results()
