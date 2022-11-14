"""Bigframe"""
def main():
    """beom hong"""
    message1 = input().strip()
    message2 = input().strip()
    message3 = input().strip()
    message4 = input().strip()
    message5 = input().strip()
    highest = max(len(message1), len(message2), len(message3),\
    len(message4), len(message5)) + 4
    print(("*" * highest))
    print("* %s" %message1, end="")
    print(" " * (highest - 3 - len(message1)), end="")
    print("*")
    print("* %s" %message2, end="")
    print(" " * (highest - 3 - len(message2)), end="")
    print("*")
    print("* %s" %message3, end="")
    print(" " * (highest - 3 - len(message3)), end="")
    print("*")
    print("* %s" %message4, end="")
    print(" " * (highest - 3 - len(message4)), end="")
    print("*")
    print("* %s" %message5, end="")
    print(" " * (highest - 3 - len(message5)), end="")
    print("*")
    print(("*" * highest))
main()
