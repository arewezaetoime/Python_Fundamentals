def print_results():
    # Here we print the info for every course.
    for current_course in courses.keys():
        print(f'{current_course}: {len(courses[current_course])} participants')
        counter = 1
        for current_participant in sorted(courses[current_course].items(), key=lambda item: (-item[1], item[0])):
            print(f'{counter}. {current_participant[0]} <::> {current_participant[1]}')
            counter += 1
    total_points_dict = {}
    # With the loops below we get the sum of all the points for every user and fill the total point dict.
    for i_user in individual_stats.keys():
        total_points_dict[i_user] = 0
        for current_points in individual_stats[i_user].values():
            total_points_dict[i_user] += current_points
    # Here we start printing the ranking for the users in descending order.
    print('Individual standings:')
    i_counter = 1
    for user, point in sorted(total_points_dict.items(), key=lambda item: (-item[1], item[0])):
        print(f'{i_counter}. {user} -> {point}')
        i_counter += 1


def validation(v_name, v_course, v_score):
    flag_str = True
    flag_int = True
    if ' ' in v_name or ' ' in v_course:
        flag_str = False
    if v_score not in range(0, 1_001):
        flag_int = False
    if flag_int and flag_str:
        return True
    return False


def add_data_courses(a_name, a_course, a_score):
    if a_course not in courses.keys():
        courses[a_course] = {}
    if a_name not in courses[a_course].keys():
        courses[a_course][a_name] = a_score
    else:
        if courses[a_course][a_name] < a_score:
            courses[a_course][a_name] = a_score


def add_data_participants(p_name, p_course, p_score):
    if p_name not in individual_stats.keys():
        individual_stats[p_name] = {}
        individual_stats[p_name][p_course] = p_score
    else:
        individual_stats[p_name][p_course] = p_score

    if individual_stats[p_name][p_course] < p_score:
        individual_stats[p_name][p_course] = p_score


def get_data():
    data_input = input()
    while data_input != 'no more time':
        data_input = data_input.split(' -> ')
        if len(data_input) == 3:
            name, course, score = str(data_input[0]), str(data_input[1]), int(data_input[2])
            if validation(name, course, score):

                add_data_courses(name, course, score)
                add_data_participants(name, course, score)

        data_input = input()


courses = {}
individual_stats = {}
get_data()
print_results()
