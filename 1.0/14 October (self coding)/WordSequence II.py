"""WordSequence II"""
def main():
    """beom help by mean"""
    text_one = input()
    text_two = input()
    length = len(text_one)
    if len(text_two) > len(text_one):
        length = len(text_two)
    for i in range(length+1):
        print(text_two[:i] + text_one[i:])
main()
