"""SecondConverter"""

def main():
    """beom help by Saul Goodman"""
    kkk = int(input())
    sss = int(input())
    mmm = int(input())
    hhh = int(input())
    sec = kkk
    minit = sec // sss
    sec = sec % sss
    hour = minit // mmm
    minit = minit % mmm
    hour = hour % hhh
    print("%d:%d:%d"%(hour, minit, sec))
main()
