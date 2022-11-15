"""isPrime_large"""
from math import sqrt
def main():
    """beom"""
    inp = int(input())
    if inp == 1:
        print("NO")
    else:
        if sqrt(inp) == True:
            print("NO")
        else:
            print("YES")
main()
