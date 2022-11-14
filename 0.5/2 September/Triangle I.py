"""Triangle I"""


def main():
    """beom_help_by_meeeeen"""
    aaa = float(input())
    bbb = float(input())
    ccc = float(input())
    if (aaa**2 + bbb**2)**0.5 == ccc:
        print("Yes")
    elif (aaa**2 + ccc**2)**0.5 == bbb:
        print("Yes")
    elif (bbb**2 + ccc**2)**0.5 == aaa:
        print("Yes")
    else:
        print("No")


main()
