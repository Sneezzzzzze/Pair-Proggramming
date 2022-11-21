"""Heads and Legs"""
def main():
    """beom"""
    amount = int(input())
    leg = int(input())
    rabbit, lost = divmod(leg-(amount*2), 2)
    bird = amount - rabbit
    if rabbit >= 0 and bird >= 0 and lost == 0:
        print(rabbit, bird)
    else:
        print("Impossible")
main()
