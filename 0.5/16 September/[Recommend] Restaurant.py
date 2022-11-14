"""[Recommend] Restaurant"""

def main():
    """beom"""
    eat = float(input())
    need_to_eat_more = float(input())
    discount = float(input())
    yes_or_no = float(input())
    iii = eat + yes_or_no
    solution1 = eat + yes_or_no >= need_to_eat_more
    if solution1:
        iii = iii * (100 - discount) / 100
    no_offer = eat
    solution2 = eat >= need_to_eat_more
    if solution2:
        no_offer = no_offer * (100 - discount) / 100
    different = abs(iii - no_offer)
    solution1 = iii < no_offer
    solution2 = iii > no_offer
    if solution1:
        print("Yes %.3f" %different)
    elif solution2:
        print("No %.3f" % different)
    else:
        print("Yes")
main()
