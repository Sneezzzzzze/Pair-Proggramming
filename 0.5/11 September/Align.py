"""Align"""
def main(size, alignment, text):
    """beom_help by mean"""
    if alignment == 'left':
        print(text)
    elif alignment == 'center':
        left_chk = size - len(text)
        if (left_chk % 2) == 1:
            text = ' ' + text
        print(text.center(size))
    elif alignment == 'right':
        print("{msg:>{length}}".format(length=size, msg=text))
main(int(input()), input(), input())
