def printSum():
    values = [23, 45, 78, 98, 34] # create a list of random values

    sum = 0 #initialize the variable sum
    length = 0 #initialize 

    for value in values: 
        sum += value #add the current value to sum
        print(sum)
        length += 1 # add the current value to length
        print(length)
    print("Total Sum: " + str(sum) + " - Average: " + str(sum / length))

printSum()

