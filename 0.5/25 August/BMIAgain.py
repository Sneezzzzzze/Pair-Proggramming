"""BMIAgain"""


def main():
    """beom"""
    weight = float(input())
    height = float(input())
    bmi = (weight / (height/100)**2)
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    elif 25 <= bmi < 30:
        print("Overweight")
    else:
        print("Obese")


main()
