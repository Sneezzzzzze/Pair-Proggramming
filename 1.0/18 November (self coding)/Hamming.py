""" Hamming"""
def main(inp1, inp2):
    """beom"""
    lisst, lissst, count = [], [], 0
    for i in inp1:
        lisst.append(i)
    for j in inp2:
        lissst.append(j)
    for k in range(len(inp1)):
        if lisst[k] != lissst[k]:
            count += 1
    print(count)
main(input(), input())
