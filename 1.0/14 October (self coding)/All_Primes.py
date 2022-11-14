"""All_Primes"""
def main():
    """beom"""
    inp = int(input())
    count = 0
    for i in range(1, inp+1):
        for j in range(2, i+1):
            if i%j == 0:
                if i == j:
                    count += 1
                break
    print(count)
main()
