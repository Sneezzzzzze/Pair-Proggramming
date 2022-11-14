"""Median"""
def main():
    """beom"""
    num = int(input())
    iii = []
    for _ in range(1, num+1):
        inp = int(input())
        iii.append(inp)
        iii.sort()
    if num%2 == 1:
        print("%0.1f"%iii[(num-1)//2])
    else:
        ppp = ((iii[(num//2)-1])+iii[num//2])/2
        print("%0.1f"%ppp)
main()
