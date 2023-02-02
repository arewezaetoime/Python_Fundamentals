coordinates_input = input()

store_list = []
while coordinates_input:
    store_list.append(int(coordinates_input))
    coordinates_input = input()

print(store_list)
line_list = []
for i in range(0, len(store_list), 2):
    line = abs(store_list[i] + store_list[i + 1])
    line_list.append(line)
print(line_list)

if line_list[0] + line_list[1] < line_list[2] + line_list[3]:
    print(f"({store_list[4]} - {store_list[5]})")
    print(f"({store_list[6]} - {store_list[7]})")
else:
    print(f"({store_list[0]} - {store_list[1]})")
    print(f"({store_list[2]} - {store_list[3]})")