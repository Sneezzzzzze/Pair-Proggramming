"""Resistor"""


def main():
    """beom"""
    inp1, inp2 = input(), input()
    inp3, inp4 = input(), input()
    num = {"Black": 0, "Brown": 1, "Red": 2, "Orange": 3,
           "Yellow": 4, "Green": 5, "Blue": 6, "Purple": 7,
           "Grey": 8, "White": 9}
    num2 = {"Black": 0, "Brown": 1, "Red": 2, "Orange": 3,
            "Yellow": 4, "Green": 5, "Blue": 6, "Purple": 7,
            "Grey": 8, "White": 9}
    multiplier = {"Black": 1, "Brown": 10, "Red": 10**2, "Orange": 10**3,
                  "Yellow": 10**4, "Green": 10**5, "Blue": 10**6, "Purple": 10**7,
                  "Gold": 0.1, "Silver": 0.01}
    tolerance = {"Brown": 1/100, "Red": 2/100, "Green": 0.5/100, "Blue": 0.25/100,
                 "Purple": 0.10/100, "Grey": 0.05/100, "Gold": 5/100, "Silver": 10/100}
    if inp1 not in num or inp2 not in num2 or inp3 not in multiplier or inp4 not in tolerance:
        print("Error")
    else:
        ans1 = str(num[inp1]), str(num2[inp2])
        ans = "".join(ans1)
        print("%.4f" % (
            (int(ans)*multiplier[inp3]) - (int(ans)*multiplier[inp3])*tolerance[inp4]))
        print("%.4f" % (
            (int(ans)*multiplier[inp3]) + (int(ans)*multiplier[inp3])*tolerance[inp4]))


main()
