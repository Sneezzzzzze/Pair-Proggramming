"""FibonacciRecursionV2"""
def recur_fibo(nnn):
    """beom nat"""
    if nnn <= 1:
        return nnn
    return recur_fibo(nnn-1) + recur_fibo(nnn-2)
print(recur_fibo(int(input())))
