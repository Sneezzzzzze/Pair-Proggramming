"""ATM"""
def main():
    """beom"""
    money_in_bank = int(input())
    while True:
        atm_service = input()
        if atm_service == "END":
            break
        else:
            atm_service = atm_service.split()
            if atm_service[0] == "D":
                money_in_bank += int(atm_service[1])
            elif atm_service[0] == "W":
                if money_in_bank < int(atm_service[1]):
                    money_in_bank = 0
                else:
                    money_in_bank -= int(atm_service[1])
    print(money_in_bank)
main()
