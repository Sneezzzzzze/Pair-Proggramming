"""ISBN"""
 
 
def main():
    """beom"""
    inp = input().replace("-", "")
    ans = ((10*int(inp[0]))+(9*int(inp[1]))+(8*int(inp[2]))+(7*int(inp[3])) +
           (6*int(inp[4]))+(5*int(inp[5]))+(4*int(inp[6]))+(3*int(inp[7]))+(2*int(inp[8])))
    final_ans = (-ans % 11)
    if inp[9] != "X":
        if final_ans == int(inp[9]):
            print("Yes")
        elif final_ans == 10:
            print("No", "X")
        else:
            print("No", final_ans)
    else:
        if final_ans == 10:
            print("Yes")
        else:
            print("No", "X")
 
 
main()