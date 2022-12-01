"""Rungame"""
def main():
    """beom help by mean"""
    num = (input().split())
    if num == []:
        print(0)
    else:
        count = abs(int(num[0]))
        for i in range(len(num)-1):
            count += abs(int(num[i]) - int(num[i+1]))
        print(count)
main()
