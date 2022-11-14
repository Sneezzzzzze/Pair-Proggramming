"""Elo"""
def main():
    """beom hong"""
    r_a = int(input())
    r_b = int(input())
    a_or_b = input()
    eaa = 1 / (1+(10**((r_b-r_a)/400)))
    ebb = 1 / (1+(10**((r_a-r_b)/400)))
    if a_or_b == "A":
        print("%.2f"%eaa)
    else:
        print("%.2f"%ebb)
main()
