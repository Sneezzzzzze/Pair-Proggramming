"""GCD_v1"""
def main(aaa, bbb):
    """beom"""
    if bbb == 0:
        print(abs(aaa))
    else:
        main(bbb, aaa % bbb)
main(int(input()), int(input()))
