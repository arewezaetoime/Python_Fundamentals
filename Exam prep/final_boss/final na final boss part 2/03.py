def get_dict(our_list, our_dict):
    for pair in our_list:
        current_pair = pair.split(': ')
        word, definition = current_pair[0], current_pair[1]
        if word not in our_dict.keys():
            our_dict[word] = []
        if definition not in our_dict[word]:
            our_dict[word].append(definition)
    return our_dict


def test_func(dict, words):
    for current_word in words:
        if current_word in dict.keys():
            print(f'{current_word}:')
            for definition in dict[current_word]:
                print(f" -{definition}")
        else:
            continue


def handover(our_dict):
    print(' '.join(our_dict))


list_with_words = input().split(' | ')
words_for_testing = input().split(' | ')
command = input()
our_dict = {}

get_dict(list_with_words, our_dict)

if command == 'Test':
    test_func(our_dict, words_for_testing)
elif command == 'Hand Over':
    handover(our_dict)
