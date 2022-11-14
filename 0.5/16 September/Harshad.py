"""Harshad"""
def main():
    """beom"""
    for _ in range(10):
        iii = int(input())
        sume = 0
        if iii == 0:
            print("No")
        else:
            if iii > 0:
                for digit in str(iii):
                    sume += int(digit)
            elif iii < 0:
                for digit in str(abs(iii)):
                    sume -= int(digit)
            if iii%sume == 0:
                print("Yes")
            else:
                print("No")
main()
