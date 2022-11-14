"""BrickBridge"""

def make_brige(aaa, bbb, ggg):
    """boem jai"""
    big_rock_check = bbb * 5
    if big_rock_check <= ggg:
        big_rock = bbb
    else:
        big_rock = ggg // 5

    big_rock_used = big_rock * 5
    goal = ggg - big_rock_used

    if goal > aaa:
        print("-1")
    else:
        print(goal)
make_brige(int(input()), int(input()), int(input()))
