"""[Recommend] Squid Game 3 - Tug-of-War"""
def main():
    """beom Hong"""
    count = 0
    ooo = 0
    for _ in range(10):
        iii = int(input())
        count += iii
    for _ in range(10):
        eee = int(input())
        ooo += eee
    if count > ooo:
        print("B")
    elif count < ooo:
        print("A")
    elif count == ooo:
        print("AB")
main()
