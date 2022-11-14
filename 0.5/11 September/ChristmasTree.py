"""ChristmasTree"""
def lea():
    """ beom """
    leaf = int(input())
    wood = int(input())
    base_size = 0
    for i in range(leaf):
        for _ in range(leaf-i-1):
            print(" ", end="")
        for _ in range(2*i+1):
            print("*", end="")
        base_size = ((i*2)+1)
        print()
    for _ in range(wood):
        print('---'.center(base_size+1))
lea()
