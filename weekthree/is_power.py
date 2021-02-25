def is_power(n):
    if n == 0:
        return False
    while n % 2 == 0:
        n /= 2
    if n == 1:
        return True
    return False

print(is_power(8))