"""Tuple's Sad life"""
def main():
    """beom home"""
    inp = input()
    xxx = inp.split()
    yyy = tuple(xxx)
    inp2 = input()
    zzz = yyy.index(inp2)
    for _ in range(yyy.count(inp2)):
        print((str(zzz)+" ")*(yyy.count(inp2)))
main()
