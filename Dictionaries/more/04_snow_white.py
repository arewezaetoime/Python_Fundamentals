d_colour = 'hat'
d_name = 'name'
d_phys = 'phys'
hat_len = 'hat_len'
result_list = []


def print_sorted_results():
    for dwarf in dwarf_dict:
        for name, phys in dwarf_dict[dwarf].items():
            result_list.append({hat_len: len(dwarf_dict[dwarf]), d_name: name, d_phys: phys, d_colour: dwarf})

    for d in sorted(result_list, key=lambda item: (-item[d_phys], -item[hat_len])):
        print(f"({d[d_colour]}) {d[d_name]} <-> {d[d_phys]}")


def add_dwarf_func(name, hat, physics):
    if hat not in dwarf_dict.keys():
        dwarf_dict[hat] = {}

    if name not in dwarf_dict[hat]:
        dwarf_dict[hat][name] = 0
    if dwarf_dict[hat][name] < physics:
        dwarf_dict[hat][name] = physics


def validation_of_the_data(d_name, d_hat, d_physics):
    # Here we check for forbidden symbols and range of the integers
    symbols_to_check = [' ', '<', ':', '>']
    for symbol in symbols_to_check:
        if symbol in d_name or symbol in d_hat:
            return False
    if d_physics in range(0, 2**31-1):
        return True


dwarf_dict = {}

dwarf_input = input()
while dwarf_input != 'Once upon a time':
    current_dwarf = dwarf_input.split(' <:> ')
    dwarf_name, hat_colour, dwarf_physics = str(current_dwarf[0]), str(current_dwarf[1]), int(current_dwarf[2])
    if validation_of_the_data(dwarf_name, hat_colour, dwarf_physics):
        # If validation of the data return True ,we pass the dwarf data to add function
        add_dwarf_func(dwarf_name, hat_colour, dwarf_physics)
    dwarf_input = input()

print_sorted_results()
