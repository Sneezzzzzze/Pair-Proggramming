"""BloodDonation"""
def main():
    """beom"""
    age = int(input())
    weight = int(input())
    have_you_ever = int(input())
    if age == 17 or age == 60 <= 70:
        commit = input()
    if age < 17 or weight < 45 or (have_you_ever == 0 and age <= 55):
        print("No")
    else:
        print("Yes")
main()