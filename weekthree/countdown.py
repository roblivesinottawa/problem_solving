def count_down(start_num):
    current = 5
    while current > 0:
        print(current)
        current -= 1
    print("zero")

count_down(5)


def print_range(start, end):
    n = start

    while n <= end:
        print(n)
        n += 1

print_range(1, 5)