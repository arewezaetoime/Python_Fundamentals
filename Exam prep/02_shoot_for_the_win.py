def reduce_values(targets, index):
    special_value = targets[index]
    targets[index] = -1

    for i in range(len(targets)):
        if targets[i] == -1:
            continue
        if targets[i] > special_value:
            targets[i] -= special_value
        else:
            targets[i] += special_value
    return targets


def shoot_for_the_win(targets):
    shot_targets = 0

    while True:
        command = input()
        if command == 'End':
            print(f"Shot targets: {shot_targets} -> {' '.join([str(target) for target in targets])}")
            break

        index = int(command)
        if 0 <= index < len(targets) and targets[index] != -1:
            shot_targets += 1
            reduce_values(targets, index)


sequence_targets = list(map(int, input().split()))
shoot_for_the_win(sequence_targets)