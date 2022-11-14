"""SurprisingVote"""


def main():
    """beom"""
    ala = float(input())
    highest = float(input())
    other = ala - highest
    if other > highest:
        other -= highest
        if highest - other <= 2:
            print("Not surprising")
        else:
            print("Surprising")
    elif highest <= 2:
        print("Not surprising")
    else:
        print("Surprising")


main()
