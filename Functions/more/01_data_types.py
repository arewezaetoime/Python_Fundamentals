def input_recognition(current_input, current_value):
    if current_input == 'int':
        int_func(current_value)

    elif current_input == 'real':
        float_func(current_value)

    elif current_input == 'string':
        string_func(current_value)


def int_func(some_int):
    print(f"{float(some_int) * 2:.0f}")


def float_func(some_float):
    print(f"{float(some_float) * 2:.2f}")


def string_func(some_string):
    final_string = '$' + some_string + '$'
    print(final_string)


type_of_input = input()
value = input()
input_recognition(type_of_input, value)