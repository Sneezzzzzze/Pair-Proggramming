"""Circular II"""
def main():
    """beom"""
    xxx = float(input())
    yyy = float(input())
    rrr = float(input())
    xnn = float(input())
    ynn = float(input())
    rrr2 = float(input())
    fun = ((xxx-xnn)**2 + (yyy-ynn)**2)**0.5
    if rrr + rrr2 > fun:
        print("Yes")
    elif rrr + rrr2 <= fun:
        print("No")
main()

