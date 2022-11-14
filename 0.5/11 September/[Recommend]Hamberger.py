"""Hamberger"""

def main():
    """ beom gun"""
    left = int(input())
    right = int(input())
    print(("|"*left) + ("*"*((left+right)*2)) + ("|"*right))

main()
