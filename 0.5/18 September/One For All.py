"""One For All"""
def main():
    """beom help by Saul Goodman"""
    num = int(input())
    if num == 0:
        return 0
    all_name = ""
    for i in range(num):
        name = input()
        if i %2 == 0:
            symbol = "-"
        else:
            symbol = "*"
        all_name += symbol*i + name
    print('%s_%d' % (all_name, num))
main()
