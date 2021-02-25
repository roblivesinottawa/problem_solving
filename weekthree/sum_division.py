def sum_division(n):
    sum = 1
    i = 2
    if n == 0:
        return 0

    while i < 10:
        if n % i == 0:
            sum = sum + i
            print(sum)
        i = i + 1

    return f"sum: {sum}"

print(sum_division(20))