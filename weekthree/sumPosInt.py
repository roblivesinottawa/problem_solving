def sum_positive_numbers(n):
    """this function returns the sum of all positive integers between n and 1"""
    if n < 1: #the base case is being smaller than 1
        return n
    return n + sum_positive_numbers(n-1) # the recursive case is adding this number to the sum of nums smaller than this one

print(sum_positive_numbers(-1)) # this will return n
print(sum_positive_numbers(6)) #this will return 1+2+3+4+5+6