"""LargestNumber"""

def main():
    """beom"""
    num1 = input()
    num2 = input()
    num3 = input()

    taw1 = int(num1 + num2 + num3)
    taw2 = int(num1 + num3 + num2)
    taw3 = int(num2 + num1 + num3)
    taw4 = int(num2 + num3 + num1)
    taw5 = int(num3 + num1 + num2)
    taw6 = int(num3 + num2 + num1)

    temp = 0
    temp = check(taw1, temp)
    temp = check(taw2, temp)
    temp = check(taw3, temp)
    temp = check(taw4, temp)
    temp = check(taw5, temp)
    temp = check(taw6, temp)
    print(temp)


def check(num1, num2):
    """Titan Saul GOodman"""
    if num1 > num2:
        return num1
    return num2

main()
