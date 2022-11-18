"""Area"""
def main():
    """beom"""
    count = 0
    for _ in range(int(input())):
        inp = input().replace(" ", "")
        count += len(inp)
    print(count)
main()
