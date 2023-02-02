judge = {'Submissions': {}}

command = input()

while command != 'exam finished':
    split_command = command.split('-')
    if len(split_command) < 3:
        del judge[split_command[0]]
        command = input()
        continue

    person, language, points = split_command

    if language not in judge['Submissions'].keys():
        judge['Submissions'][language] = 0
    judge['Submissions'][language] += 1

    if person not in judge.keys():
        judge[person] = 0

    if judge[person] < int(points):
        judge[person] = int(points)

    command = input()
print('Results:')
for key, value in judge.items():
    if key == 'Submissions':
        continue
    print(f"{key} | {value}")
print('Submissions:')
for key, value in judge['Submissions'].items():
    print(f'{key} - {value}')