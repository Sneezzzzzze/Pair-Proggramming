"""Run Length Decoding"""
def main():
    """beom hepl by mean"""
    encoded, length = input(), ''
    for i in encoded:
        if i.isnumeric():
            length += i
        elif i.isalpha():
            print(i * int(length), end="")
            length = ''
main()
