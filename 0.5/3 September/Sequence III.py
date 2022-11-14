"""Sequence III"""
def main():
    """beom jai"""
    xxx = int(input())
    for _ in range(xxx):
        for _ in range(_+1, xxx+1):
            _ += 1
            print(_, end=" ")
        print()
        xxx = xxx + 1
main()
