"""Roman"""
def main(roman, count=0):
    """beom help by mean"""
    romann = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900,
              'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for key, value in romann.items():
        count += value*roman.count(key)
        roman = roman.replace(key, "")
    print(count)
main(input())
