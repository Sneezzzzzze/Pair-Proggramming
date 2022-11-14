"""[Recommend] Diginity"""
def main():
    """beom"""
    while True:
        nnn = int(input())
        if nnn == 0:
            break
        if len(str(nnn)) == 1:
            print(nnn)
        elif len(str(nnn)) > 1:
            while True:
                count = 0
                for i in str(nnn):
                    count += int(i)
                if len(str(nnn)) == 1:
                    break
                nnn = count
            print(count)
main()
