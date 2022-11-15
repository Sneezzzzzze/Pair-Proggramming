"""Heads and Legs"""
def main():
    """beom"""
    amount = int(input())
    leg = int(input())
    rabbit = int((leg-(amount*2))/2)
    bird = amount - rabbit
    ans = rabbit, bird
    if (amount != rabbit + bird)  or \
    (rabbit < 0) or (bird < 0) or \
    (rabbit == float) or (bird == float):
    else:
        print(rabbit, bird)
main()
