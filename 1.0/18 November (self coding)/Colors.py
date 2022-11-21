"""Colors"""
def main():
    """beom"""
    color1 = input().capitalize()
    color2 = input().capitalize()
    col = ["Red", "Blue", "Yellow"]
    if color1 not in col or color2 not in col:
        print("Error")
        return
    if color1 == color2:
        print(color1)
        return
    if color1 == "Red" and color2 == "Yellow" or color2 == "Red" and color1 == "Yellow":
        print("Orange")
    elif color1 == "Red" and color2 == "Blue" or color2 == "Red" and color1 == "Blue":
        print("Violet")
    elif color1 == "Yellow" and color2 == "Blue" or color2 == "Yellow" and color1 == "Blue":
        print("Green")
main()
