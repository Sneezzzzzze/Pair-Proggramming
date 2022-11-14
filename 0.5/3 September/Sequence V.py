"""Sequence V"""
def main():
    """beom jai"""
    xxx = int(input())
    yyy = 0
    for _ in range(xxx, 0, -1):
        yyy += 1
        if yyy % 8 == 0:
            yyy = 1
            print()
        print(_, end=" ")
main()
