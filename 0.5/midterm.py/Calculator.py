"""Calculator"""
def calculator(num):
    """beom"""
    count = 0
    if num != 1:
        for _ in range(1, num+1):
            total = len(str(_))+1
            count += total
        print(count)
    else:
        print(1)
calculator(int(input()))
