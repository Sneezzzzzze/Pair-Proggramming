"""Duplicate I"""
def main():
    """beom"""
    seta = set()
    setb = set()
    mmm = int(input())
    nnn = int(input())
    for _ in range(1, mmm+1):
        inp1 = input()
        seta.add(inp1)
    for _ in range(1, nnn+1):
        inp2 = input()
        setb.add(inp2)
    if seta&setb == set():
        print("Nope")
    else:
        setc = (seta&setb)
        setc = sorted(setc)
        setc = reversed(setc)
        for i in setc:
            print(i)
main()
