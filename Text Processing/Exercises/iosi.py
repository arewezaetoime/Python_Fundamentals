def ticket_validation(ticket):
    if len(ticket) == 20:
        return True
    return False


def check_winning(current_ticket):
    winning_symbols = ['@', '#', '$', '^']
    left_side_ticket = current_ticket[:10]
    right_side_ticket = current_ticket[10:]
    multiplicator_left = 0
    multiplicator_right = 0
    current_symbol = ''
    current_match_left = ''
    current_match_right = ''
    matches = []
    for symbol in winning_symbols:
        for multiplicator in range(len(left_side_ticket), 5, -1):
            if symbol * multiplicator in left_side_ticket:
                multiplicator_left += multiplicator
                current_symbol += symbol
                current_match_left += symbol * multiplicator
                matches.append(symbol * multiplicator)
                break
        for multiplicator_two in range(len(right_side_ticket), 5, -1):
            if symbol * multiplicator_two in right_side_ticket:
                multiplicator_right += multiplicator_two
                current_match_right += symbol * multiplicator_two
                matches.append(symbol * multiplicator_two)
                break

    if 10 > len(current_match_left) > 6 and 10 > len(current_match_right) > 6:
        if current_match_left in current_match_right or current_match_right in current_match_left:
            uninterrupted_match_length = min(matches)
            return f'''"ticket "{current_ticket}" - {len(uninterrupted_match_length)}{current_symbol}"'''
    elif current_match_left in right_side_ticket or current_match_right in left_side_ticket:
        uninterrupted_match_length = min(matches)
        return f'''"ticket "{current_ticket}" - {len(uninterrupted_match_length)}{current_symbol} Jackpot!"'''
    elif len(current_match_left) >= 6 or len(current_match_right) >= 6 and \
            current_match_left not in right_side_ticket or current_match_right not in left_side_ticket:
        return f'''"ticket "{current_ticket}" - no match"'''


tickets_input = [ticket.strip() for ticket in input().split(',')]
if len(tickets_input) in range(0, 100):
    for ticket in tickets_input:
        if ticket_validation(ticket):
            print(check_winning(ticket))
        else:
            print('invalid ticket')
