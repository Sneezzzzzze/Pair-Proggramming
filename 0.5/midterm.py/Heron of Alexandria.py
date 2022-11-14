"""Heron of Alexandria"""
def heron_of_alexandria():
    """beom"""
    import math
    aaa = float(input())
    bbb = float(input())
    ccc = float(input())
    sss = (aaa + bbb + ccc)/2
    area = math.sqrt((sss*(sss-aaa))*(sss-bbb)*(sss-ccc))
    print("%.3f"%area)
heron_of_alexandria()
