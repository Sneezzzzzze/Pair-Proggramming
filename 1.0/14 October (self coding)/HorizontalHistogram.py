"""HorizontalHistogram"""
def main():
    """beom help by mean"""
    word = input()
    tmpup = {}
    tmplow = {}
    for i in word:
        if i.isupper():
            tmpup[i] = word.count(i)
            # tmp.update({key: value})
        elif i.islower():
            tmplow[i] = word.count(i)
    sort_tmplow = sorted(tmplow.items(), key=lambda x: x[0])
    sort_tmpup = sorted(tmpup.items(), key=lambda x: x[0])
    cal = sort_tmplow+sort_tmpup
    for i in cal:
        tmp = ''
        for j in range(1, i[1]+1):
            if j % 5 == 0 and i[1] != j:
                tmp += '-|'
            elif j % 5 != 0 or i[1] == j:
                tmp += '-'
        print('%s : %s' % (i[0], tmp))
main()
