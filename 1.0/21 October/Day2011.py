"""Day2011"""
def main():
    """beom help by mean"""
    num_day = int(input())
    num_month = int(input())
    day = ['Saturday', 'Sunday', 'Monday',
           'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cal = (sum(month[:num_month-1]) + num_day) % 7 - 1
    print(day[cal])
main()
