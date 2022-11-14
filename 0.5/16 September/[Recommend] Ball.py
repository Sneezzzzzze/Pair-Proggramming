"""[Recommend] Ball"""
def main():
    """beom hong"""
    height = float(input())
    count = 0
    bounce = height * (3 / 5)
    while bounce >= 0.01:
        count += 1
        bounce *= (3/5)
        if bounce < 0.01:
            break
    print(count)
main()
