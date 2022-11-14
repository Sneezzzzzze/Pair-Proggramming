"""HowLong"""

def main():
    '''beom'''
    xxx = int(input())
    cou = 0
    if xxx < 0:
        for _ in str(xxx):
            cou += 1
        print(cou-1)
    elif xxx >= 0:
        for _ in str(xxx):
            cou += 1
        print(cou)
main()
