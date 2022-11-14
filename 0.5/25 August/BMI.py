"""BMI"""
def main():
    """beom neo"""
    name_1 = input()
    weight = float(input())
    height = float(input())
    bmi = (weight / (height/100)**2)
    print(name_1 + "'s", " BMI = "+"%.2f"%bmi)
main()
main()
main()
main()
main()
