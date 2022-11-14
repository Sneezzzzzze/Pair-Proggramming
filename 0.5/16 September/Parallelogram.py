"""Parallelogram"""
def main():
    """beom help by saul Goodman"""
    text = input()
    len_of_text = len(text)
    space = len_of_text - 1
    text_left = 1
    for _ in range(len_of_text - 1):
        print(" " * space, end="")
        print(text[:text_left])
        space -= 1
        text_left += 1

    for i in range(len_of_text):
        print(text[i:])
main()
