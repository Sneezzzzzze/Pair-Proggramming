"""Sequence IX"""
def inp():
    xxx = int(input())
    return xxx
def haf_tri():
    """beom jai"""
xxx = inp()
for i in range(1, xxx+1):
    for k in range(xxx-i, 0, -1):
        print(" ", end="  ")
    for j in range(1, i+1):
        print("%02d" % j, end=" ")
    print()
eee = xxx-1
for i in range(1, eee + 1):
    for j in range(1, i + 1):
        print("%02d"%j, end=" ")
    print()
haf_tri()