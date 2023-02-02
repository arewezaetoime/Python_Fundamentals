starting_string = input()
lst = starting_string.split(' ')
rev = []
for num in lst:
    new_rev = int(num)
    new_rev *= -1
    rev.append(new_rev)
print(rev)
