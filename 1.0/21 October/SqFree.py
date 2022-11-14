"""SqFree"""
def main():
    """beom"""
    inp = int(input())
    count = 0
    for i in range(1 ,inp+1):
        if i // (2**2) == 0:
            count += 1
    print(count)
main()
