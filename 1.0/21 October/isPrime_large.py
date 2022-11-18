'''isPrime_large'''
def main():
    '''beom help by mean'''
    num = int(input())
    ans = 'YES'
    if num == 1:
        ans = 'NO'
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            ans = 'NO'
    print(ans)
main()
