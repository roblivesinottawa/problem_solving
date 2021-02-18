def find_average(total, files):
    """calculates the average size"""
    return total / files
  

total = ["2048", "4357", "97658", "125", "8"]
converted_total = ''.join(total) #converting list into string
new_total = int(converted_total)
files = 5

average = find_average(new_total, files)
print(f"the average size is {str(average)}")
