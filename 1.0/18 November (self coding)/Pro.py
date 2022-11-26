"""Pro"""
def main():
    """beom"""
    comex = int(input())
    pay = int(input())
    price = int(input())
    ifcome = int(input())
    cal1 = (ifcome//comex)*(pay*price)
    ans = cal1 + (ifcome % comex*price)
    print(ans)
main()
