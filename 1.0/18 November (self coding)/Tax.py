"""Tax"""
def main():
    """beom help by mean"""
    year = int(input())
    cc_car = int(input())
    year_dic = {6:10, 7:20, 8:30, 9:40}
    if cc_car > 1801:
        ans = (600 * 0.5) + ((1800 - 600) * 1.5) + ((cc_car - 1800) * 4)
    elif 601 < cc_car <= 1800:
        ans = (600 * 0.5)+((cc_car - 600) * 1.5)
    else:
        ans = (cc_car * 0.5)
    if year in year_dic:
        ans = ans - (ans*(year_dic[year]/100))
    elif year >= 10:
        ans /= 2
    print("%.2f"%ans)
main()
