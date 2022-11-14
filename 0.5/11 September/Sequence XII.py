"""Sequence XII"""
def main():
    """beom help by mean"""
    line = int(input())
    for i in range(line):
        for j in range(i, -1, -1):
            print("%02d"% (line - j), end=" ")
        for j in range((line-1) - i):
            print("%02d"% ((line-1) - j), end=" ")
        # Prints the upper right side
        for j in range((line-1) - i, 0, -1):
            print("%02d"% ((line+1) - j), end=" ")
        for j in range(i):
            print("%02d"% (line - j - 1), end=" ")
        print()
    for i in range(line-2, -1, -1):
        for j in range(i, -1, -1):
            print("%02d"% (line - j), end=" ")
        for j in range((line-1) - i):
            print("%02d"% ((line-1) - j), end=" ")
        for j in range((line-1) - i, 0, -1):
            print("%02d"% ((line+1) - j), end=" ")
        for j in range(i):
            print("%02d"% (line - j - 1), end=" ")
        print()
main()
