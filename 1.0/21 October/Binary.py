"""Binary"""
def main():
    """beom nat"""
    decimal_input = int(input())
    bainari = []
    decimal = decimal_input
    if decimal_input == 0:
        print(0)
    while decimal > 0:
        bainari.append(str(decimal % 2))
        decimal = int(decimal / 2)
    bainari.reverse()
    for i in bainari:
        print(i, end="")
main()
