def memory_game(elements):
    moves_counter = 0
    matching_elements = 0
    while True:
        command = input()
        if command == 'end' and len(elements) > 0:
            print(f"Sorry you lose :(\n{' '.join(elements)}")
            break
        if command == 'end':
            break
        if len(elements) == 0:
            print(f"You have won in {moves_counter} turns!")
            break
        moves_counter += 1
        command = command.split()
        index_one = int(command[0])
        index_two = int(command[1])
        if index_one == index_two or index_one < 0 or index_two < 0:
            middle_index = len(elements) // 2
            penalty = f"-{moves_counter}a"
            elements.insert(middle_index, penalty)
            elements.insert(middle_index, penalty)
            print(f"Invalid input! Adding additional elements to the board")
            continue

        if elements[index_one] == elements[index_two]:
            matching_element1 = elements.pop(index_one)
            elements.pop(index_two - 1)
            print(f"Congrats! You have found matching elements - {matching_element1}!")

        if elements[index_one] != elements[index_two]:
            print("Try again!")


sequence_of_elements = input().split()
memory_game(sequence_of_elements)
