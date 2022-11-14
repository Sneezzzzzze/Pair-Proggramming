'''Impostor'''
from json import loads
def main():
    '''beom help by my friends'''
    charac = {}
    characdaeth = []
    while True:
        characinp = input()
        if characinp == 'Start':
            break
        charac.update(loads(characinp))
    charac = dict(sorted(charac.items(), key=lambda x: x[0]))
    charac_copy = charac.copy()
    while True:
        charac_daethinp = input()
        characdaeth.append(charac_daethinp)
        if charac_daethinp == 'End':
            break
    die_die_die = {}
    for i in charac.items():
        if i[0] in characdaeth:
            die_die_die[i[0]] = i[1]
            charac_copy.pop(i[0])
    conut = 0
    for value in charac_copy.values():
        if value == 'Impostor':
            conut += 1
    print(conut, 'Impostor Remains\n***Alive***')

    for i in charac_copy:
        print(i, ':', charac_copy[i])
    print('***Dead***')
    for i in die_die_die:
        print(i, ':', die_die_die[i])
main()
