"""TheFunctionWithin"""


def funcf(xxx):
    """function_f"""
    return 2*xxx


def funcg(xxx):
    """function_g"""
    return (3*(xxx**4)) - xxx**3 + (2*(xxx**2)) + 10


def funch(xxx, yyy, zzz):
    """function_h"""
    return ((zzz + xxx)**2) - (xxx*yyy) + yyy**2


def funci(aaaa, bbbb, cccc, dddd):
    """function_i"""
    return ((aaaa**2) + (bbbb**2) - (cccc**2)) / ((dddd**2) - ((2*aaaa)*dddd) + (2*aaaa))


def main(aaa, bbb, ccc, ddd):
    """beom neo"""
    print(funcf(funcf(aaa)))
    print(funcg(funcf(aaa-bbb)))
    print(funch(funcf(aaa+bbb), funcf(aaa+ccc), funcg(funcf((ddd**2)))))
    one = (funch(funcf(aaa+bbb), funcf(aaa-ccc), funcg(funcf((ddd**2)))))
    two = (funcg(funcf(aaa-bbb)))
    three = funcf(funcf(funcf(funcf(funcf(ccc)))))
    four = ddd**8
    print(funci(one, two, three, four))
main(float(input()), float(input()), float(input()), float(input()))
