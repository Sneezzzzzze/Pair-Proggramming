"""Sequence VII"""

def main():
    """input"""
    rows = int(input())
    return rows
def up_midd_low(rows):
    """beom jai"""
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for i in range(rows-1, 0, -1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
up_midd_low(main())
