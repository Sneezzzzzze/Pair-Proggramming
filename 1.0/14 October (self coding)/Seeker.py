"""Seeker"""
import re
def main(string1):
    """beom"""
    ans = [int(x.group()) for x in re.finditer(r'\d+', string1)]
    print(sum(ans))
main(input())
