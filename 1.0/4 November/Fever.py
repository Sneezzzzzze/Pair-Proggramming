"""Fever"""
 
 
def main():
    """beom"""
    temperature = float(input())
    if 36 <= temperature < 38:
        print("No Fever")
    elif 38 <= temperature < 39:
        print("Mild Fever")
    elif 39 <= temperature < 40:
        print("High Fever")
    elif 40 <= temperature:
        print("Very High Fever")
    else:
        print("hypothermia")
 
 
main()