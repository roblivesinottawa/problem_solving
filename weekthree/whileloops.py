def attempts(n):
# always initilize a variable
    x = 0
    while x <= n: #condition
        print(f"attempt {str(x)}")
        x += 1 # increment the value so as not to get an infinite loop
    print(f"done")

attempts(5)
