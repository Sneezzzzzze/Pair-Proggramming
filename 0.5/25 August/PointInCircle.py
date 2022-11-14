"""PointInCircle"""


def main():
    """beom"""
    xxx = float(input())
    yyy = float(input())
    rrr = float(input())
    xnn = float(input())
    ynn = float(input())
    if ((xxx-xnn)**2 + (yyy-ynn)**2) <= rrr**2:
        print(True)
    else:
        print(False)


main()
