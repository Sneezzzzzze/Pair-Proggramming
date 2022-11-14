"""[Recommend] PhoneNumber"""
def main():
    """beom"""
    phonenum = input()
    do_or_in = input()
    if len(phonenum) == 9 and do_or_in == "Domestic":
        print((phonenum[0:1]), end=" ")
        print((phonenum[1:5]), end=" ")
        print(phonenum[5:9], end="")
    elif len(phonenum) == 9 and do_or_in == "International":
        print_1 = phonenum.replace(phonenum[0:], "+66")
        print(print_1, end=" ")
        print((phonenum[1:5]), end=" ")
        print(phonenum[5:9], end="")

    if len(phonenum) == 10 and do_or_in == "Domestic":
        print((phonenum[0:2]), end=" ")
        print((phonenum[2:6]), end=" ")
        print(phonenum[6:10], end="")
    elif len(phonenum) == 10 and do_or_in == "International":
        print_2 = phonenum.replace(phonenum[0:], "+66")
        print(print_2+phonenum[1:2], end=" ")
        print((phonenum[2:6]), end=" ")
        print(phonenum[6:10], end="")


main()
