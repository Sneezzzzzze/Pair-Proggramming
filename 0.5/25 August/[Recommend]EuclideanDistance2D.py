"""EuclideanDistance2D"""
import math


def main():
    """beom"""
    qqone = float(input())
    qqtwo = float(input())
    ppone = float(input())
    pptwo = float(input())
    print(math.sqrt(((qqone-ppone)**2) + ((qqtwo-pptwo))**2))


main()
