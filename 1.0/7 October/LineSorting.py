"""LineSorting"""
def main():
    """beom"""
    beomlist = []
    line = int(input())
    for _ in range(1, line+1):
        word = input()
        beomlist.append(word)
    beomlist.sort(key=len)
    for j in beomlist:
        print(j)
main()
