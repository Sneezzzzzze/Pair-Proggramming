""" [Recommend] Temperature"""


def celsius(xxx, yyy):
    """celsius"""
    if yyy == "F":
        return (xxx * (9/5)) + 32
    elif yyy == "K":
        return xxx + 273.15
    elif yyy == "R":
        return (xxx + 273.15) * (9/5)
    else:
        return xxx


def fahrenheit(xxx, yyy):
    """Farenheit"""
    zzz = (xxx - 32) * (5/9)
    if yyy == "C":
        return zzz
    elif yyy == "K":
        return zzz + 273.15
    elif yyy == "R":
        return (zzz + 273.15) * 9/5
    else:
        return xxx


def kelvin(xxx, yyy):
    """Kelvin"""
    zzz = xxx - 273.15
    if yyy == "C":
        return zzz
    elif yyy == "F":
        return (zzz * 9/5) + 32
    elif yyy == "R":
        return (zzz + 273.15) * 9/5
    else:
        return xxx


def rankine(xxx, yyy):
    """Rankine"""
    zzz = (xxx - 491.67) * 5/9
    if yyy == "C":
        return zzz
    elif yyy == "F":
        return (zzz * 9/5) + 32
    elif yyy == "K":
        return zzz + 273.15
    else:
        return xxx


def main():
    """beom"""
    tem = float(input())
    choose1 = input().upper()
    choose2 = input().upper()
    if choose1 == "C":
        print("%.2f" % (celsius(tem, choose2)))
    elif choose1 == "F":
        print("%.2f" % (fahrenheit(tem, choose2)))
    elif choose1 == "K":
        print("%.2f" % (kelvin(tem, choose2)))
    elif choose1 == "R":
        print("%.2f" % (rankine(tem, choose2)))


main()
