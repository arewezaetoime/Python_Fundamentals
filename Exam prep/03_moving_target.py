def strike(targets, index, radius):
    pass


def add(targets, index, value):
    targets.insert(value, index)
    return targets


def shoot(targets, index, power):
    targets[index] -= power
    if targets[index] <= 0:
        targets.pop(index)
    return targets


def moving_targets(targets):
    while True:
        command = input()
        if command == 'End':
            print('|'.join(targets))
            break
        command = command.split()
        index = int(command[1])
        value = int(command[2])
        if command[0] == 'Add':
            if index <= len(targets):
                add(targets, index, value)
            else:
                print(f"Invalid placement!")
        elif command[0] == 'Shoot':
            if index <= len(targets):
                shoot(targets, index, value)
        elif command[0] == 'Strike':
            if index <= len(targets) and


sequence_of_targets = list(map(int, input().split()))
moving_targets(sequence_of_targets)