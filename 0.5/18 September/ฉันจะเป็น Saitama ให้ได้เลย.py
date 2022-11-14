"""ฉันจะเป็น Saitama ให้ได้เลย"""
import math
def main():
    """beom"""
    push_up = int(input())
    situp = int(input())
    looknang = int(input())
    running = int(input())
    amount_push_up = int(input())
    amount_situp = int(input())
    amount_runnning = int(input())
    amount_looknang = int(input())
    aaa = math.ceil(push_up / amount_push_up)
    bbb = math.ceil(situp / amount_situp)
    ccc = math.ceil(looknang / amount_looknang)
    ddd = math.ceil(running / amount_runnning)
    if aaa > bbb and aaa > ccc and aaa > ddd:
        print(aaa)
    elif bbb > aaa and bbb > ccc and bbb > ddd:
        print(bbb)
    elif ccc > aaa and ccc > bbb and ccc > ddd:
        print(ccc)
    elif ddd > aaa and ddd > bbb and ddd > ccc:
        print(ddd)
    elif aaa == bbb == ccc == ddd:
        print(aaa)
main()
