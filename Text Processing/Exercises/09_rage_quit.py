rage_input = input()
current_cut = ''
final_rage = ''
unique_symbols = ''
multiplicator = ''
for index in range(len(rage_input)):

    if rage_input[index].isdigit():
        for number in range(index, len(rage_input)):
            if not rage_input[number].isdigit():
                break
            else:
                multiplicator += rage_input[number]
        for _ in range(int(multiplicator)):
            final_rage += current_cut.upper()
        current_cut = ''
        multiplicator = ''
    else:
        current_cut += rage_input[index]
        unique_symbols += rage_input[index].upper()

print(f"Unique symbols used: {len(set(unique_symbols))}")
print(final_rage)

#         times_to_loop = int(rage_input[index])
#         for times in range(times_to_loop - 1):
#             # print(rage_input[:index].upper(), end='')
#             final_rage += rage_input[:index].upper()
#     else:
#         final_rage += rage_input[index].upper()
# print(final_rage)
