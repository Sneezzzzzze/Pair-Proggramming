"""Tax"""
def main():
    """beom"""
    year = int(input())
    cc_car = int(input())
    oil = {
        1<= cc_car <= 600: 0.5,
        601 <= cc_car <= 1800: 1.50,
        cc_car > 1801: 4.00
    }
    discount = {
        year < 6: year,
        year == 6: 10/100,
        year == 7: 20/100,
        year == 8: 30/100,
        year == 9: 40/100,
        year == 10: 50/100
    }
    oil[cc_car]