card_sign = input()

if card_sign == 'J' or card_sign == 'Q' or card_sign == 'K' or card_sign == 'A':

    # first we print the number cards
    for i in range(2, 11):
        print(f'{i} of spades, {i} of clubs, {i} of hearts, {i} of diamonds')

    # then we print special ones
    if card_sign == 'J':
        print('J of spades, J of clubs, J of hearts, J of diamonds')
    elif card_sign == 'Q':
        print('J of spades, J of clubs, J of hearts, J of diamonds')
        print('Q of spades, Q of clubs, Q of hearts, Q of diamonds')
    elif card_sign == 'K':
        print('J of spades, J of clubs, J of hearts, J of diamonds')
        print('Q of spades, Q of clubs, Q of hearts, Q of diamonds')
        print('K of spades, K of clubs, K of hearts, K of diamonds')
    else:  # this case is for A
        print('J of spades, J of clubs, J of hearts, J of diamonds')
        print('Q of spades, Q of clubs, Q of hearts, Q of diamonds')
        print('K of spades, K of clubs, K of hearts, K of diamonds')
        print('A of spades, A of clubs, A of hearts, A of diamonds')
else:  # the input is a string number
    for i in range(2, int(card_sign)+1):
        print(f'{i} of spades, {i} of clubs, {i} of hearts, {i} of diamonds')
