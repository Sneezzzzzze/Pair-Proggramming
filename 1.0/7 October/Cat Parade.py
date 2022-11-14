"""Cat Parade"""
def main():
    """beom help by mean"""
    listone = []
    listtwo = []
    check = []
    while True:
        typeip = input()
        if typeip == 'END':
            break
        if typeip == "IT'S A DOG":
            listone.pop()
        elif ',' in typeip:
            typeip = typeip.split(', ')
            listone.extend(typeip)
        else:
            listone.append(typeip)
    listtwo = listone.copy()
    listone.sort()
    for i in listone:
        if i in check:
            continue
        else:
            print(i, listtwo.index(i) + 1, listone.count(i))
        check.append(i)
main()
