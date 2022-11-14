"""isprime_small"""
def main():
    """beom"""
    inp = int(input())
    if inp > 1:
        for i in range(2, inp):
            if (inp % i) == 0:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")
main()
