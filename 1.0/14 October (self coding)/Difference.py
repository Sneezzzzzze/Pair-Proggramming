"""Difference"""
def main():
    """beom"""
    seta, setb = set(), set()
    nnn, mmm = int(input()), int(input())
    for _ in range(nnn):
        nn2 = int(input())
        seta.add(nn2)
    for _ in range(mmm):
        mm2 = int(input())
        setb.add(mm2)
    print(*sorted(seta - setb)) # * เอา เครื่องหมายออก
main()
