money_list = input().split(', ')
number_of_beggars = int(input())
earned_beggars = []
money_list_as_digits = []
for digit in money_list:
    money_list_as_digits.append(int(digit))
starting_index = 0
while starting_index < number_of_beggars:
    collected_beggar = 0
    for current_beggar in range(starting_index, len(money_list_as_digits), number_of_beggars):
        collected_beggar += money_list_as_digits[current_beggar]
    earned_beggars.append(collected_beggar)
    starting_index += 1
print(earned_beggars)
