"""Day I"""


def main():
    """beom jai"""
    # ยกเว้นปีที่หารด้วย 100 ลงตัวและหารด้วย 900 แล้วไม่เหลือเศษเป็น 200 หรือ 600
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Yes")
    else:
        print("No")

main()
