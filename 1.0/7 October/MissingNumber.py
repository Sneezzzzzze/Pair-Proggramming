"""MissingNumber"""
def amin():
    """beom"""
    num = int(input())
    iii = []
    while True:
        sss = int(input())
        if sss == 0:
            break
        iii.append(sss)
    for i in range(1, num+1):
        if i in iii:
            pass
        else:
            print(i)
amin()
