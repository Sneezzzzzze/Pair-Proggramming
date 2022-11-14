"""CircularPrime"""
import math


def prime(n):
    """beom"""
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
    if c == 2:
        return 1
    else:
        return 0


def circular(n):
    """ beom """
    c, tmp = 0, n
    while tmp > 0:
        c += 1
        tmp //= 10
    num = n
    while prime(num) == 1:
        r = num % 10
        d = num//10
        num = int((math.pow(10, c-1)*r+d))
        if num == n:
            return 1
    return 0


p = 1
q = int(input())
add = 0
for i in range(p, q+1):
    if circular(i) == 1:
        add += i
print(add)
