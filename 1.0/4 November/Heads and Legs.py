"""Heads and Legs"""
def main():
    """beom"""
    amount = int(input())
    leg = int(input())
    rabbit = int((leg-(amount*2))/2)
    bird = amount - rabbit
    ans = rabbit, bird
    if (amount != rabbit + bird) or (amount == float) or (leg == float) or (rabbit < 0) or (bird < 0):
        print("Impossible")
    else:
        print(rabbit, bird)
main()
