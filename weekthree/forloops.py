"""
sum = 0
sum = 0 + (1*1) = 1
sum = 1 + (2*2) = 5
sum = 5 + (3*3) = 14
sum = 14 + (4*4) = 30
sum = 30 + (5*5) = 55
...

"""


def square(n):                        
    return n * n                            

def sum_squares(x):
    sum = 0
    for n in range(1, x):
        sum += square(n)
        print(sum)
    return sum

result = sum_squares(11)
print(result)

# refactored
def summedSquares(n):
    sum = 0
    for i in range(1 + n+1):
        sum += (i*i)
        print(sum)
    return sum

print(summedSquares(10))