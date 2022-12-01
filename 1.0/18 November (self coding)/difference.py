"""Difference"""
import json
def main():
    """beom help by mean"""
    lista = json.loads(input().replace("'", '"'))
    listb = json.loads(input().replace("'", '"'))
    seta = set(lista)
    setb = set(listb)
    ans1 = seta - setb
    ans2 = setb - seta
    dct1 = {}
    dct2 = {}
    ans = {}
    cha = True
    for i in ans1:
        ans[i] = lista.count(i)
    for i in ans2:
        ans[i] = listb.count(i)
    for i in lista:
        if i not in dct1:
            dct1[i] = lista.count(i)
    for i in listb:
        if i not in dct2:
            dct2[i] = listb.count(i)
    for key in dct1:
        if key in dct2 and dct1[key] != dct2[key]:
            ans[key] = abs(dct1[key] - dct2[key])
            cha = False
    for i in sorted(ans):
        print(i, ans[i])
    if cha:
        print('ONAJI DAYO!')
main()
