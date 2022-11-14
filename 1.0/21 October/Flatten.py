"""Flatten"""
import json
def main():
    """beom nat"""
    inp = json.loads(input())
    inplist = []
    while True:
        if inp == []:
            break
        lay = inp.pop()
        if isinstance(lay, int):
            inplist.append(lay)
        else:
            inp.extend(lay)
    print(sorted(inplist, reverse=True))
main()
