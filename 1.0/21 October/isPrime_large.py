"""isPrime_large"""
from math import sqrt
def main():
    """beom"""
    inp = int(input())
    if inp == 1:
        print("No")
    else:
        if sqrt(inp) == True:
            print("No")
        else:
            print("Yes")
main()
