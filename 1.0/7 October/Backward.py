"""Backward"""
def main():
    """beom home"""
    sss = []
    inp = input()
    while inp != "NULL":
        sss.append(inp)
        inp = input()
    sss.reverse()
    for i in sss:
        print(i)
main()
