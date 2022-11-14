"""Matrix_MN"""
def main():
    """beom help by mean"""
    mmm = int(input())
    nnn = int(input())
    llist = []
    for _ in range(mmm):
        for _ in range(nnn):
            num = int(input())
            llist.append(num)
        print(*llist)
        llist.clear()
main()
