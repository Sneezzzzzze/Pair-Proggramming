"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def again():
    """beom help by mean"""
    vowels = 'aeiou'
    words = input().replace('.', '').split()
    words.sort()
    check = True
    for i in words:
        count = 0
        for j in vowels:
            if j in i:
                count += i.count(j)
        if count > 1:
            print(i)
            check = False
    if check:
        print('Nope')
again()
