""" Donut"""
def donutt():
    """beom goodman"""
    aaa = int(input())
    bbb = int(input())
    ccc = int(input())
    ddd = int(input())
    promotion = ddd//(bbb+ccc)
    donut = ddd - (bbb + ccc)*promotion
    if donut >= bbb:
        promotion += 1
        price = (aaa*(bbb*promotion))
        donut_ = ((ccc + bbb)*promotion)
    else:
        price = (aaa*(bbb*promotion)) + (donut * aaa)
        donut_ = ((ccc + bbb)*promotion) + donut
    print(price, donut_)
donutt()
