"""PickThemAgain"""
def main():
    """beom"""
    inp = input()
    uuu = []
    ooo = []
    iii = inp.split()
    for i in iii:
        if int(i) %3 == 0 or int(i) %5 == 0:
            uuu.append(i)
        else:
            ooo.append(i)
    uuu.reverse()
    if uuu == []:
        print("Nope")
    else:
        for j in uuu:
            print(j)
main()
