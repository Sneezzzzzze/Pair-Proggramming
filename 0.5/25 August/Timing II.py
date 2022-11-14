"""Timing II"""
def main():
    """beom"""
    sec = int(input())
    seconds = sec
    minutes = seconds//60
    seconds = seconds % 60
    hours = minutes//60
    minutes = minutes % 60
    days = hours//24
    hours = hours % 24
    if len(str(days)) > 4:
        print("ERR_:__:__:__")
    else:
        print("%04d"%days, "%02d"%hours, "%02d"%minutes, "%02d"%seconds, sep=":")
main()
