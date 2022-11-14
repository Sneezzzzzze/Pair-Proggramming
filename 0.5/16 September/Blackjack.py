"""Blackjack"""
def main():
    """beom help by Saul Goodman"""
    count = 0
    treu_flase = False
    num = int(input())
    for i in range(num):
        text_inp = input()
        if text_inp == 'A':
            treu_flase = True
        count = cal_point(text_inp, count)
        i = i

    if treu_flase == True and count > 21:
        count -= 10
    print(count)

def cal_point(card, point):
    '''card'''
    if card == 'J' or card == 'Q' or card == 'K':
        point += 10
    elif card.isnumeric():
        point += int(card)
    else:
        if point > 10:
            point += 1
        else:
            point += 11
    return point
main()
