def prime(n):
    factor = 2
    while factor <= n: #while 2 is less than or equal to 100
        if n % factor == 0: #if 100 is divisible by 2 without a remainder
            print(factor) #print the factor
            n = n / factor
        else:
            factor += 1
    return "done"

print(prime(20))