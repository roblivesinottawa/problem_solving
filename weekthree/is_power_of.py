def is_power_of(n, base):
    if n < base and n == 1:
        return True
    elif n == 0:
        return False
    else:
        n = n / base

    return is_power_of(n , base)

print(is_power_of(8,2))
print(is_power_of(64,4))
print(is_power_of(70,10))