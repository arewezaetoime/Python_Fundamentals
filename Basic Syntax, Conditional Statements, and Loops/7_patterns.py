length = int(input())

for i in range(1, length + 1):
    i *= '*'
    print(i)
for j in range(length - 1, 0, -1):
    j *= '*'
    print(j)
