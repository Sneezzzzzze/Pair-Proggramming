"""Sequence XXX"""
def main():
    """beom help by Saul Goodman"""
    nnn = int(input())
    mmm = int(input())
    pics = [[' ' for i in range(nnn)] for i in range(nnn)]
    for i in range(nnn):
        for j in range(nnn):
            if i == j or i + j == nnn - 1 \
                    or j == 0 or i == 0 or j == nnn - 1 or i == nnn - 1:
                pics[i][j] = '*'
    for i in range(nnn):
        for k in range(mmm):
            for j in range(nnn):
                print(pics[i][j], end='')
            print(end=' ')
            k = k
        print()
main()
