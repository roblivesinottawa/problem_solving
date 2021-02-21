# name = 'Rob'
# number = len(name) * 9
# print(f"hello {name}. Your lucky number is {number}")
# name1 = 'Vick'
# number1 = len(name) * 9
# print(f"hello {name1}. Your lucky number is {number1}")


# refactor above code

def lucky_number():
    name = input("enter name: ")
    number = len(name) * 9
    return name, number

output = lucky_number()
print(output)

# or like this:

def lucky(name):
    number = len(name) * 9
    return f"hello {name}. your lucky number is {str(number)}"

print(lucky("Rob"))
