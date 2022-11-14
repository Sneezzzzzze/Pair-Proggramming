"""BreachTheDoor"""
import re
def main():
    """beom"""
    inp = input()
    inp = re.sub(r"[^a-zA-Z]", " ", inp)
    inp = inp.split(" ")
    llist = []
    for i in inp:
        if len(i) > 6:
            llist.append(i)
    print(*llist)
main()
