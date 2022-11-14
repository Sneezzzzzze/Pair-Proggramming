""" PSCP """
def seq_(num):
    """ Sequence XI """
    for i in range(1, num+1):
        for j in range(i):
            print("%02d" %(j+1), end=" ")
        for j in range(num-i):
            print("%02d" % (i), end=" ")
        for j in range(num-i, 0, -1):
            print("%02d" %(i), end=" ")
        for j in range(i-2, -1, -1):
            print("%02d" % (j+1), end=" ")
        print()
    for i in range(num-1, 0, -1):
        for j in range(i):
            print("%02d" % (j+1), end=" ")
        for j in range(num - i):
            print("%02d" % (i), end=" ")

        for j in range(num - i, 0, -1):
            print("%02d" % (i), end=" ")
        for j in range(i-2, -1, -1):
            print("%02d" % (j+1), end=" ")
        print()
seq_(int(input()))
