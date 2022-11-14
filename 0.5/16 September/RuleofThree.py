"""RuleofThree"""
def main():
    """beom help by Saul Goodman"""
    num = int(input())
    price, weight = float(input()), float(input())
    solve = price / weight
    for i in range(num-1):
        cal_price, cal_weight = float(input()), float(input())
        calculate = cal_price / cal_weight
        condi1 = calculate <= solve
        condi2 = calculate == solve and cal_price > price
        if condi1 and not condi2:
            price = cal_price
            weight = cal_weight
            solve = calculate
        i = i
    print("%.02f %.02f" % (price, weight))
main()
