"""Bill"""
def pay():
    """beom hong"""
    paid = int(input())
    ser_charge = paid * 0.1
    total = 0
    if ser_charge > 1000:
        paid += 1000
        total = paid + (paid * (7 / 100))
        print("%.2f"% total)
    elif ser_charge < 50:
        paid += 50
        total = paid + (paid * (7 / 100))
        print("%.2f"% total)
    else:
        price = paid + ser_charge
        total = price + (price * (7 / 100))
        print("%.2f"% total)
pay()
