"""BloodDonation"""
def main(age, weight, have_you_ever):
    """beom"""
    if age == 17 or (70 >= age >= 60):
        commit = input()
    if ((age == 17 or (70 >= age >= 60)) and commit == "False")\
            or age < 17 or age > 70 or weight < 45 or (have_you_ever == 0 and age > 55):
        print("No")
    else: print("Yes")
main(int(input()), int(input()), int(input()))
