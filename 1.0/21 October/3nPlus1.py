"""3nPlus1"""
def three_n_plus_one():
    """beom help by mean"""
    while True:
        inp = int(input())
        tmp = 1
        if inp == 0:
            tmp += 1
            break
        while inp != 1:
            if inp % 2 == 0:
                inp //= 2
                tmp += 1
            elif inp % 2 == 1:
                inp = inp*3+1
                tmp += 1
        print(tmp)
three_n_plus_one()
