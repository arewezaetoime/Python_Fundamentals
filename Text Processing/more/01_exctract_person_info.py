n = int(input())
info_dict = {}

for _ in range(n):
    line = input()
    name = ''
    age = ''
    for i in range(0, len(line)):
        # Here we start to collect name letters if they are present.
        if line[i] == '@':
            for name_letter in range(i + 1, len(line)):
                if line[name_letter] == '|':
                    break
                else:
                    name += line[name_letter]
        # Here we start to collect age digits if they are present at all.
        if line[i] == '#':
            for age_digit in range(i + 1, len(line)):
                if line[age_digit] == '*':
                    break
                else:
                    age += line[age_digit]
    # Here we add our results to a new dictionary record.
    info_dict[name] = age
# Here we start printing the results.
for person, age in info_dict.items():
    print(f"{person} is {age} years old.")

# text = 'dsdA'
# index = text.index('A')     -------- To try it out !!!!!!! Another approach.
# print(index)