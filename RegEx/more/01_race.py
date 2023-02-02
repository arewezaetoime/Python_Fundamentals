import re

list_of_racers = input().split(', ')
pattern = r'[a-zA-Z0-9]'
pattern_name = r'[a-zA-Z]'
pattern_digits = r'\d'
racers_dict = {}
current_line = input()
while current_line != 'end of race':
    total_ran = 0
    result = re.findall(pattern, current_line)
    raw_string = ''.join(result)
    runner = ''.join(re.findall(pattern_name, raw_string))
    kilometres_ran = re.findall(pattern_digits, raw_string)
    distance = [int(a) for a in kilometres_ran]
    if runner in list_of_racers:
        if runner not in racers_dict.keys():
            racers_dict[runner] = sum(distance)
        else:
            racers_dict[runner] += sum(distance)
    current_line = input()

racers_sorted = sorted(racers_dict.items(), key=lambda x: x[1], reverse=True)
print(f'1st place: {racers_sorted[0][0]}')
print(f'2nd place: {racers_sorted[1][0]}')
print(f'3rd place: {racers_sorted[2][0]}')
