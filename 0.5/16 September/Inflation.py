"""Inflation"""
def main():
    """beom help by Saul Goodman"""
    nnn = float(input())*100
    kkk = int(input())
    for i in range(kkk):
        nnn = int(nnn) * 10381 // 10000
        i = i
    print("%d.%02d"%(nnn//100, (nnn%100)))
main()
