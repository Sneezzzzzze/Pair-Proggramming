"""Turnstile"""

def main():
    """beom help by Saul Goodman"""
    real = True
    inp = input()
    count = 0
    while inp != 'END':
        if inp == 'END':
            break
        if real == True:
            if inp == 'C':
                real = False
        else:
            if inp == 'P':
                count += 1
                real = True
        inp = input()
    print(count)
main()
