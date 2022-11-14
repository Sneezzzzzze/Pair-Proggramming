"""Safe"""
def main():
    """beom help by mean"""
    code, unlock = input(), input()
    count = 0
    for i in range(len(code)):
        aaa, bbb = ord(code[i]), ord(unlock[i])
        call_aaa = abs(aaa - bbb)
        call_aaa_min = abs(26 - call_aaa)
        count += min(call_aaa, call_aaa_min)
    print(count)
main()
