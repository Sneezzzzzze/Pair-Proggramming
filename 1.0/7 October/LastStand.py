"""LastStand"""
def main():
    """beom"""
    inp = input()
    inf = inp.replace("[", "").replace("]", "").replace(",", " ")
    inf = str(inf).split()
    for i in inf:
        print((i)[-1]) #มี print อยู่ แล้ว print จากหลัง
main()
