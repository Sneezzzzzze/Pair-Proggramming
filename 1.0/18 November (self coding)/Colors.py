"""Colors"""
def main():
    """beom"""
    color1 = input().title()
    color2 = input().title()
    if color1 == "Red" and color2 == "Yellow" or color2 == "Red" and color1 == "Yellow":
        print("Orange")
    elif color1 == "Red" and color2 == "Blue" or color2 == "Red" and color1 == "Blue":
        print("Violet")
    elif color1 == "Yellow" and color2 == "Blue" or color2 == "Yellow" and color1 == "Blue":
        print("Green")
    else:
        print("Error")
main()
