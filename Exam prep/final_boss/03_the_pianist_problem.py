n_pieces = int(input())
piano_collection = {}

for current_piece in range(n_pieces):
    piece, composer, key = input().split('|')
    piano_collection[piece] = [composer, key]

command = input()
while command != 'Stop':
    current_command = command.split('|')
    if current_command[0] == 'Add':
        piece, composer, key = current_command[1], current_command[2], current_command[3]
        if piece not in piano_collection.keys():
            piano_collection[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif current_command[0] == 'Remove':
        piece = current_command[1]
        if piece in piano_collection.keys():
            del piano_collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif current_command[0] == 'ChangeKey':
        piece, new_key = current_command[1], current_command[2]
        if piece in piano_collection.keys():
            values = piano_collection[piece]
            old_key = values.pop()
            piano_collection[piece].append(new_key)
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

for piece, value in piano_collection.items():
    print(f"{piece} -> Composer: {value[0]}, Key: {value[1]}")
