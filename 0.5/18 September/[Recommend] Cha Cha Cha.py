"""[Recommend] Cha Cha Cha"""
import math
def main():
    """beom Hong"""
    working = int(input())
    total = 0
    for _ in range(working):
        hour = (math.ceil(float(input())))
        income = hour * 8720
        total += income
    print(total)
main()
