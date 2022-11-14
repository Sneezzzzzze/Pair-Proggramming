"""Meteorite"""
def meteorite():
    """beom"""
    aaa = float(input())
    bbb = int(input())
    ccc = float(input())
    boom = 0
    rocket = 0
    while aaa >= ccc:
        ddd = bbb**boom
        boom += 1
        rocket += ddd
        aaa = aaa / bbb
    print(int(rocket))
meteorite()
