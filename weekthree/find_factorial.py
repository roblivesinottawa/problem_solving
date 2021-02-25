def factorial(n):
    """thi function calculates the factorial on n"""
    result = 1
    for x in range(n):
        # print(f"x = {x}")
        result = result * (n - x) # at first iteration: result = 1 * 10 = 10. second: 10 * 9 = 90. third: 90 * 8 = 720...
        # print(result)
    return result

# print(factorial(4)) # 4 * 3 * 2 * 1
print(factorial(10))


# recursive factorial

def fact(n):
    print(f"factorial called with {str(n)}")
    if n < 2:
        print("returning 1")
        return 1
    return n * fact(n - 1)


print(fact(4))




