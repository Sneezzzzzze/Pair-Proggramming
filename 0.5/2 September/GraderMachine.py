"""GraderMachine"""
def main():
    """beom jai"""
    fir = int(input())
    las = int(input())
    if fir > las:
        if fir %2 == 1:
            fir += 1
        sume = 0
        print("pass : ", end="")
        for iii in range(fir, las-1, -2):
            print(iii, end=" ")
            sume = sume + iii
        print("\nSum :", sume, end="")
    else:
        if fir %2 == 1:
            fir += 1
        sume = 0
        print("pass : ", end="")
        for iii in range(fir, las+1, 2):
            print(iii, end=" ")
            sume = sume + iii
        print("\nSum :", sume, end="")

main()
