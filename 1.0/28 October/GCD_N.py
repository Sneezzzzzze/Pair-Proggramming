"""GCD_N"""
import math
def main():
    """beom"""
    inp = int(input())
    for _ in range(inp):
        find = int(input())
        x = math.gcd(find)
    print(x)
main()