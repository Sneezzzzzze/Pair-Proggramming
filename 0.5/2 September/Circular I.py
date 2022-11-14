"""Circular I"""


def main():
    """beom jai"""
    xxx = float(input())
    yyy = float(input())
    rrr = float(input())
    xnn = float(input())
    ynn = float(input())
    if ((xxx-xnn)**2 + (yyy-ynn)**2)**0.5 <= rrr:
        print("Yes")
    else:
        print("No")


main()
