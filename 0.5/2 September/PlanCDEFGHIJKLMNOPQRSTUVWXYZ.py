"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""


def ascen(num1, num2, num3):
    """dddd"""
    if True:
        if num1 >= num2 >= num3:
            print("%.2f, %.2f, %.2f" % (num1, num2, num3))
        elif num1 >= num3 >= num2:
            print("%.2f, %.2f, %.2f" % (num1, num3, num2))
        elif num2 >= num1 >= num3:
            print("%.2f, %.2f, %.2f" % (num2, num1, num3))
        elif num2 >= num3 >= num1:
            print("%.2f, %.2f, %.2f" % (num2, num3, num1))
        elif num3 >= num2 >= num1:
            print("%.2f, %.2f, %.2f" % (num3, num2, num1))
        elif num3 >= num1 >= num2:
            print("%.2f, %.2f, %.2f" % (num3, num1, num2))


def descen(num1, num2, num3):
    """ddddd"""
    if True:
        if num1 >= num2 >= num3:
            print("%.2f, %.2f, %.2f" % (num3, num2, num1))
        elif num1 >= num3 >= num2:
            print("%.2f, %.2f, %.2f" % (num2, num3, num1))
        elif num2 >= num1 >= num3:
            print("%.2f, %.2f, %.2f" % (num3, num1, num2))
        elif num2 >= num3 >= num1:
            print("%.2f, %.2f, %.2f" % (num1, num3, num2))
        elif num3 >= num2 >= num1:
            print("%.2f, %.2f, %.2f" % (num1, num2, num3))
        elif num3 >= num1 >= num2:
            print("%.2f, %.2f, %.2f" % (num2, num1, num3))


def main():
    """beom"""
    option = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if option == "Ascend":
        descen(num1, num2, num3)
    elif option == "Descend":
        ascen(num1, num2, num3)


main()
