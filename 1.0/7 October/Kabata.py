"""Kabata"""
def main():
    """beom"""
    num = int(input())
    for _ in range(num):
        inp = input()
        inq = inp.replace("bakka", "").replace("ta", "").replace("ka", "").replace("ba", "")
        if "bakaka" in inq or inq != "":
            print("no")
        if inq == "":
            print("yes")
        print(inq)
main()
