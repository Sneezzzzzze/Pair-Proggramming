"""temperature"""
def main():
    """beom"""
    inp = float(input())
    choose_tem_unit = input()
    choose_tem_unit_two = input()
    return inp, choose_tem_unit, choose_tem_unit_two
def c():
    """if c """
    inp, choose_tem_unit, choose_tem_unit_two = main()
    if choose_tem_unit == "C":
        if choose_tem_unit_two == "K":
            return "%.2f"%(inp+273.15)
        elif choose_tem_unit_two == "F":
            return "%.2f"%((inp*9/5)+32)
        else:
            return"%.2f"%((inp+273.15)*(9/5))
    return c()
def f():
    """if f"""
    inp, choose_tem_unit, choose_tem_unit_two = main()
    if choose_tem_unit == "F":
        if choose_tem_unit_two == "C":
            return "%.2f"%(inp/((9/5)+32))
def choose():
    """ """
    choose_tem_unit= main()
    if choose_tem_unit == "C":
        print(c())
choose()