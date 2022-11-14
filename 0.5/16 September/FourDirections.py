"""FourDirections"""
def main():
    '''beom help by Saul GOodman'''
    text1 = input()
    mat = [[]for i in range(5)]
    for i in text1:
        if i == 'U':
            mat = arr_up(mat)
        elif i == 'D':
            mat = arr_down(mat)
        elif i == 'R':
            mat = arr_right(mat)
        elif i == 'L':
            mat = arr_left(mat)

    for i in mat:
        for j in i:
            print(j, end=' ')
        print()
def arr_left(mat):
    "beom"
    mat[0].append('  *  ')
    mat[1].append(' *   ')
    mat[2].append('*****')
    mat[3].append(' *   ')
    mat[4].append('  *  ')
    return mat
def arr_right(mat):
    "beomm"
    mat[0].append('  *  ')
    mat[1].append('   * ')
    mat[2].append('*****')
    mat[3].append('   * ')
    mat[4].append('  *  ')
    return mat
def arr_up(mat):
    "beommm"
    mat[0].append('  *  ')
    mat[1].append(' *** ')
    mat[2].append('* * *')
    mat[3].append('  *  ')
    mat[4].append('  *  ')
    return mat
def arr_down(mat):
    "beommmm"
    mat[0].append('  *  ')
    mat[1].append('  *  ')
    mat[2].append('* * *')
    mat[3].append(' *** ')
    mat[4].append('  *  ')
    return mat
main()
