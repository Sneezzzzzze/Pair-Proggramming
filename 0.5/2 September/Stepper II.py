"""Stepper I"""
def main():
    """beom jai"""
    mmm = int(input())
    nnn = int(input())
    if mmm < nnn:
        for www in range(mmm, nnn+1):
            print(www)
    else:
        for www in range(mmm, nnn-1, -1):
            print(www)
main()
