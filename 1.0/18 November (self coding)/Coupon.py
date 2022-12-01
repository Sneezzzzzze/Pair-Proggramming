"""Coupon"""
def main():
    """beom help by mean"""
    price = float(input())
    dis1 = input().split()
    dis2 = input().split()
    test1 = price - float(dis1[0]) if price >= float(dis1[1]) else price
    test2 = price - \
        (price * (float(dis2[0])/100)) if price >= float(dis2[1]) else price
    if test1 < test2:
        print('1 %.1f' % test1)
    elif test1 > test2:
        print('2 %.1f' % test2)
    elif test1 == test2 and test1 != price:
        # else = elif dis1[1] <= dis2[1]
        print('2 %.1f' % test2 if dis2[1] < dis1[1] else '1 %.1f' % test1)
    else:
        print('Nope')
#print('1 %.1f' %test1 if test1 < test2 else '2 %.1f' %test2)
main()
