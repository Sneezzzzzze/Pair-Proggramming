"""CoPrimeV1"""
def main(inp_one, inp_two):
    """beom"""
    g_c_d = gcd(inp_one, inp_two)
    if g_c_d == 1:
        print("YES")
        print(g_c_d)
    else:
        print("NO")
        print(g_c_d)
def gcd(inp_one, inp_two):
    """Euclidean Algorithm for GCD"""
    if inp_one == 0:
        return inp_two
    return gcd(inp_two % inp_one, inp_one)
main(int(input()), int(input()))
