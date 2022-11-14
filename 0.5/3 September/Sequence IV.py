"""SequenceIV"""


def main():
    """beom jai"""
    xxx = int(input())
    yyy = xxx
    for i in range(0, xxx**2, yyy):
        for _ in range(i, xxx):
            _ += 1
            print(_, end=" ")
        print()
        xxx = xxx + yyy


main()
