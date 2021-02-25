
# print numbers 1 through 7
number  = 1
while number <= 7:
    print(number, end=" ")
    number += 1


# print out each letter
def show_letters(word):
    for letter in word:
        print(letter)

show_letters("hello")

# 
def digits(n):
    """this function returns how many digits a number has"""
    count = 0
    if n == 0:
        return 1
    while n > 0:
        count += 1
        n = n // 10 # floor division returns the digits of a number
    return count

print(digits(25)) # 2

# 
def multiplication_table(start, stop):
    """"this function prints out a multiplication table"""
    for x in range(1, 4):
        for y in range(1, 4):
            print(str(x*y), end=" ")
        print()

multiplication_table(1, 3) 

# 
def counter(start, stop):
    """this function counts down from start to stop when start is bigger than stop, and 
        counts up from start to stop otherwise.    
    """
    x = start
    if start > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x != stop:
                return_string += ","
            x -= 1
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x != stop:
                return_string += ","
            x += 1
    return return_string

print(counter(1, 10)) # counting up: 1,2,3,4,5,6,7,8,9,10
print(counter(2,1)) #counting down: 2,1
print(counter(5)) #counting up: 5

# 
def even_nums(max):
    return_str = ""
    for n in range(0, max+1):
        if n != 0 and n % 2==0:
            return_str += str(n) + " "
    return return_str.strip()


print(even_nums(6)) # 2 4 6
print(even_nums(10)) # 2 4 6 8 10
print(even_nums(1))
print(even_nums(3)) # 2
print(even_nums(10))

# 

for x in range(1, 10, 3):
    print(x) # 1,4,7

# 
for x in range(10):
  for y in range(x):
    print(y) # 8


