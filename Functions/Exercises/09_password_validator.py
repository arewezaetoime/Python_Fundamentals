def pass_validation(some_pass):
    pass_is_valid = True
    if len(some_pass) < 6 or len(some_pass) > 10:
        pass_is_valid = False
        print('Password must be between 6 and 10 characters')
    if not some_pass.isalnum():
        print("Password must consist only of letters and digits")
        pass_is_valid = False
    digit_counter = 0
    for digit in some_pass:
        if digit.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        pass_is_valid = False
    return pass_is_valid


password_input = input()
password_is_valid = pass_validation(password_input)
if password_is_valid:
    print('Password is valid')