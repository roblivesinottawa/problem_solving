def find_product(n=10):
    """this function finds the product of a number, whcih is the multiplication of all integers from 1 to n"""
    product = 1

    for n in range(1, n):
        product = product * n
    return product

print(find_product())
    

