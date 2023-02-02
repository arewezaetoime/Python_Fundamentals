def length_pass(some_pass):
    if len(some_pass) in range(6, 11):
        return True
    else:
        return 'Password must be between 6 and 10 characters'


def letter_digits_checker(some_pass):
    if some_pass.isalnum():
        return True
    else:
        return 'Password must consist only of letters and digits'


def digits_checker(some_pass):
    counter = 0
    for digit in some_pass:
        if digit.isdigit():
            counter += 1
    if counter < 2:
        return 'Password must have at least 2 digits'
    else:
        return True


def validator(param1, param2, param3):
    if param1 and param2 and param3:
        return 'Password is valid'


password_input = input()
print(length_pass(password_input), letter_digits_checker(password_input), digits_checker(password_input))


