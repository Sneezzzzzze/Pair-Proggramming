"""Sequence VIII"""


def main():
    """beom jai"""


_ = int(input())

for i in range(1, _+1):
    for k in range(_-i, 0, -1):
        print(" ", end="  ")
    for j in range(1, i+1):
        print("%02d" % j, end=" ")
    print()
main()
