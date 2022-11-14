"""PickThem"""
def main():
    """beom home"""
    inp = input()
    inp = inp.replace(",", "").replace("[", "").replace("]", "").split()
    inp = [int(i) for i in inp]
    count = 0
    for i in inp:
        if i % 2 == 0:
            print(i)
            count += 1
    if count == 0:
        print("Nope")
main()
