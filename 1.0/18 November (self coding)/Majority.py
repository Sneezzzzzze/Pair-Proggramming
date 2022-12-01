"""Majority"""
def main():
    """beom"""
    candidate = int(input())
    selector = int(input())
    llist = []
    ans = []
    for _ in range(1, selector + 1):
        num = int(input())
        llist.append(num)
    for j in range(1, candidate + 1):
        ans.append(llist.count(j))
    if (max(ans)) > (selector/2):
        print((ans.index(max(ans))+1), max(ans))
    else:
        print(0, max(ans))
main()
