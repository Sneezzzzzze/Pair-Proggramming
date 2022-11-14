"""[Recommend] Books"""
from math import ceil
def main():
    """beom help by Saul Goodman"""
    num_n, num_k, num_x, num_y = int(input()), int(input()), int(input()), int(input())
    day_count = 0
    for _ in range(num_n):
        sum_read = 0
        while sum_read < num_k:
            sum_read += ceil(((num_x+day_count)/(num_y+day_count)) * num_k)
            day_count += 1
    print(day_count)
main()
