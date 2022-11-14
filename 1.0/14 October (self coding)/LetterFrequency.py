"""LetterFrequency"""


def mostcommonletter():
    """beom"""
    line = input().lower().replace(" ", "")
    sentence = line
    letters = list(sentence)
    print(*(max(set(letters), key=letters.count)))
mostcommonletter()
