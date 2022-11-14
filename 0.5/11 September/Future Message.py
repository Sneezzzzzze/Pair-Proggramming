"""Future Message"""
def main(message):
    """ beom gun """
    if message.isnumeric():
        print("Number")
    elif message.isupper():
        print("Uppercase")
    elif message.islower():
        print("Lowercase")
    elif message.istitle():
        print("Title")
    elif message.isspace():
        print("Space")
    else:
        print("Other")
main(input())
