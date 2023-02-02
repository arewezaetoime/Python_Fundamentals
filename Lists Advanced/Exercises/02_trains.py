# def add(lst, people):
#     last_wagon = len(lst) - 1
#     lst[last_wagon] = lst[last_wagon] + int(people)
#     return lst


# def insert(lst, index, people):
#     index = int(index)
#     lst[index] = lst[index] + int(people)
#     return lst


# def leave(lst, index, people):
#     index = int(index)
#     lst[index] = lst[index] - int(people)
#     return lst


wagons = input()
train = [x * 0 for x in range(int(wagons))]
train_new = train
while True:
    command = input().split()
    if 'End' in command:
        print(train)
        break
    if command[0] == 'add':
        # train = add(train, command[1])
        last_wagon = len(train) - 1
        train[last_wagon] = train[last_wagon] + int(command[1])
    if command[0] == 'insert':
        # train = insert(train, command[1], command[2])
        index = int(command[1])
        train[index] = train[index] - int(command[2])
    if command[0] == 'leave':
        # train = leave(train, command[1], command[2])
        index = int(command[1])
        train[index] = train[index] - int(command[2])
