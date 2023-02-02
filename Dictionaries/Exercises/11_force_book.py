our_dict = {}

command = input()
while command != 'Lumpawaroo':
    flag = False
    if " | " in command:
        force_input = command.split(' | ')
        force_side, force_user = force_input
        for value in our_dict.values():
            if force_user in value:
                flag = True
                break
        if not flag:
            if force_side not in our_dict.keys():
                our_dict[force_side] = [force_user]
            else:
                our_dict[force_side].append(force_user)

    elif ' -> ' in command:
        force_input = command.split(' -> ')
        force_user, force_side = force_input
        for key, value in our_dict.items():
            if force_user in value:
                our_dict[key].pop(value.index(force_user))
                break
        if force_side not in our_dict.keys():
            our_dict[force_side] = [force_user]
        else:
            our_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    command = input()
for side, users in our_dict.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(our_dict[side])}")
        for user in users:
            print(f"! {user}")


# if force_side not in our_dict.keys() and force_user not in our_dict.values():
#     our_dict[force_side] = []
#     our_dict[force_side].append(force_user)
# for user in our_dict.values():
#     if force_user in user:
#         flag = False
# if flag:
#     our_dict[force_side].append(force_user)
#
# if force_user in our_dict[force_side]:
#     command = input()
#     continue