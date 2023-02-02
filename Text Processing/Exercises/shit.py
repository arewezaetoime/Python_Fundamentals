rage_input = input()
current_cut = ''
final_rage = ''
unique_symbols = ''
multiplication = ''
for char in rage_input:
    if not char.isdigit():
        current_cut += char
    else:
        multiplication += char


print(f"Unique symbols used: {len(set(unique_symbols))}")
print(final_rage)

