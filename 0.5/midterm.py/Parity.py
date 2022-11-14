"""Parity"""
def main(num, even_or_odd):
    """beom"""
    if num == "0000000" and even_or_odd == "Even":
        print(num+"0")
    elif num == "0000000" and even_or_odd == "Odd":
        print(num+"1")
    change = num.replace("0", "")
    size = len(change)
    if size %2 == 1 and even_or_odd == "Odd":
        print(num+"0")
    elif size %2 == 1 and even_or_odd == "Even":
        print(num+"1")
    elif size %2 == 0 and even_or_odd == "Odd":
        print(num+"1")
    elif size %2 == 0 and even_or_odd == "Even":
        print(num+"0")
main(input(), input())
