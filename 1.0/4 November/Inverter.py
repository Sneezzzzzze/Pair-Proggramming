"""Inverter"""
def main():
    """beom help by mean"""
    num = input()
    ans = ""
    for i in num:
        if i == "0":
            ans += "1"
        elif i == "1":
            ans += "0"
    if any(i == "1" for i in ans):
        zero = ans.index("1")
        print(ans[zero:])
main()
