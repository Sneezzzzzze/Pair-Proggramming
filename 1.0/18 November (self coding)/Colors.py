"""Colors"""
def main():
    """beom"""
    color1 = input()
    color2 = input()
    color = ["Red", "Yellow", "Blue"]
    if color1 or color2 not in color:
        print("Error")
    else:
        if color1 == color[0] and color2 == color[1] or \
            color1 == color[1] and color2 == color[0]:
            print("Orange")
main()
