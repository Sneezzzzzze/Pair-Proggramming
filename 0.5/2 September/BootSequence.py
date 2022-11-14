"""BootSequence"""


def main():
    """beom"""
    inp = int(input())
    print("1", end="")
    for www in range(2, inp+1):
        print("_%d" % www, end="")


main()
