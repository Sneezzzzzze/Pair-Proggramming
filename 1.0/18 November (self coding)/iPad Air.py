"""iPad Air"""
def apple_store():
    """welcome"""
    inp1 = input()
    inp2 = int(input())
    inp3 = input()
    color = ["Space Gray", "Silver", "Green", "Rose Gold", "Sky Blue"]
    memory = [64, 256]
    choose = ["Wi-Fi", "Wi-Fi + Cellular"]
    if inp1 in color and inp2 == memory[0] and inp3 == choose[0]:
        print(19900)
    elif inp1 in color and inp2 == memory[1] and inp3 == choose[0]:
        print(24900)
    elif inp1 in color and inp2 == memory[0] and inp3 == choose[1]:
        print(24400)
    elif inp1 in color and inp2 == memory[1] and inp3 == choose[1]:
        print(29400)
    else:
        print("Not Available")
apple_store()
