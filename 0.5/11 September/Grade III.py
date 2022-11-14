"""Grade III"""


def main():
    """ beom gun """
    gra, total, out, count = int(input()), 0, "", 0
    for _ in range(gra):
        total += sub(float(input()))
    avg = "%.06f" % float(total/gra)
    for i in avg:
        out += i
        count += 1
        if count > 3:
            break
    print(out)


def sub(score: float) -> float:
    """help_by_mean"""
    return_data = 0
    if score < 60:
        return_data = 0
    elif score < 65:
        return_data = 0.5
    elif score < 70:
        return_data = 1
    elif score < 75:
        return_data = 1.5
    elif score < 80:
        return_data = 2
    elif score < 85:
        return_data = 2.5
    elif score < 90:
        return_data = 3
    elif score < 95:
        return_data = 3.5
    elif score <= 100:
        return_data = 4
    return return_data

main()
