"""Compound Interest"""
def compound_interest(principle, rate, time):
    """beom"""
    ans = principle * ((1 + rate/100)**time)
    print("%.2f"%ans)
compound_interest(int(input()), float(input()), int(input()))
