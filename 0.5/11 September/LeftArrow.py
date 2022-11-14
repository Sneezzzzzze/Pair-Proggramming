"""LeftArrow"""
def main():
    """ beom"""
    wide = int(input())
    height = int(input())
    for _ in range(((height-1)//2)-1, -1, -1):
        print(" "*_, "*"*wide)
    print("*"*wide)
    for _ in range((height-1)//2):
        print(" "*_, "*"*wide)
main()
