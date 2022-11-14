"""BTSMRT"""
def main():
    """beom"""
    whatday = input()
    age = float(input())
    height = float(input())
    if whatday == "Children Day" and age < 14 and height <= 140:
        print("FREE")
    elif whatday == "Senior Day" and age >= 60:
        print("FREE")
    elif whatday == "Normal Day" and age < 14 and height < 90:
        print("FREE")
    elif whatday == "Senior Day" and age < 14 and height < 90:
        print("FREE")
    else:
        print("PAY")
main()
