def length(user):
    if 3 < len(user) < 16:
        return True
    return False


def chars(user):
    for char in user:
        if not (char.isalnum() or char == '_' or char == '-'):
            return False
    return True


def redundant_sym(user):
    if ' ' in user:
        return False
    return True


def validation(usernames):
    if length(usernames) and chars(usernames) and redundant_sym(usernames):
        return True
    return False


usernames_input = input().split(', ')
for current_user in usernames_input:
    if validation(current_user):
        print(current_user)
