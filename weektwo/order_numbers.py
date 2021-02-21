def order_numbers(n1, n2):
    if n2 > n1:
        return n1, n2
    return n2, n1

smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)