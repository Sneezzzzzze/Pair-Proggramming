"""Sequence N"""
def printn(height):
    """beom help by mean"""
    for i in range(height):
        for j in range(height):
            if i == j or j == 0 or j == height-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
printn(int(input()))
