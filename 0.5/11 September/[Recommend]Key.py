"""Key"""
def main(text, total):
    """ beom help by mean"""
    for i in text:
        i = int(i)
        total += i
    last_three = int(text[-3:])*10
    pre_key = int(str(total + last_three))
    key = int(str(total + last_three)[-4:])
    if key < 1000 and pre_key < 10000:
        key += 1000
    print("%04d" % key)
main(input(), 0)
