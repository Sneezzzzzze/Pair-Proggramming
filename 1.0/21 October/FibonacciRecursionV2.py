"""FibonacciRecursionV2"""
def fibo(n):
    """beom nat"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(int(input())))
