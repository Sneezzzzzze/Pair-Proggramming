"""WeightStation"""
def main():
    """beom"""
    average_weight = float(input())
    weight1 = float(input())
    weight2 = float(input())
    weight3 = float(input())
    weight4 = (average_weight*4) - (weight1 + weight2 + weight3)
    if weight1 + weight2 + weight3 + weight4 > 15000:
        print("Overweight")
    elif weight1 < average_weight*0.5 or weight1 > average_weight*1.5:
        print("Unbalance")
    elif weight2 < average_weight*0.5 or weight2 > average_weight*1.5:
        print("Unbalance")
    elif weight3 < average_weight*0.5 or weight3 > average_weight*1.5:
        print("Unbalance")
    elif weight4 < average_weight*0.5 or weight4 > average_weight*1.5:
        print("Unbalance")
    else:
        print("Pass %.2f"%weight4)
main()
