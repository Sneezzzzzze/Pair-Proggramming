"""Divide3Or5"""
def main():
    """ beom nat"""
    aaa = 0
    num = int(input())
    for i in range(1, num+1):
        if i % 3 == 0 or i % 5 == 0:
            aaa += i
    print(aaa)
main()
